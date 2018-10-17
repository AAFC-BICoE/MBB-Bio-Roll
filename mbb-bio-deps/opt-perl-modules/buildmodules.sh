#!/bin/bash

# This script reads a file of CPAN module names (and options) to build and install
# Summary: 
#  buildmodules.sh modulefile
#
# RPM-versions of these modules. It uses cpantorpm.  The following modules must be 
# installed (through CPAN) for this to work the first time
# 	1. LWP::Simple
#	2. YAML
#	3. App::CPANtoRPM
#
#  The format of a line in the list of module files:
#   ModuleName  [rpmname] [{buildoption[:arg]}] [{buildoption[:arg]}] 
#	buildoption is any option understood by cpantorpm
#   
#   Examples:
#	YAML
#	LWP  libwww-perl
#       Text::Glob {--build-type:make}
#	 
cleanup()
{
	module unload opt-perl
}

sighandler()
{
	cleanup
	exit 0
}

unset PERL5LIB
MYPATH="`( cd \"$MY_PATH\" && pwd )`"
# Ensure that perl builds use default values when prompting for user input
export PERL_MM_USE_DEFAULT=1

module load opt-perl
trap 'sighandler' QUIT
trap 'sighandler' INT

	echo $WORKDIR
if [ -z "${WORKDIR}" ]; then 
	WORKDIR=/home/rpmbuild/rpmbuild
fi

# Create the working on localdisk and symlink to it if it does not exist
if [ ! -e $WORKDIR ]; then
	mkdir /tmp/rpmbuild
	ln -s /tmp/rpmbuild $WORKDIR
fi

echo -e "Checking for duplicate perl modules in $1"
if [ $(sort $1 | cut -f 1 -d ' ' | uniq -d | wc -l) -ne 0 ] ; then
	echo -e "Please remove the duplicate modules:"
	sort $1 | cut -f 1 -d ' ' |  uniq -d
	cleanup
	exit 1
fi

while read mod
do
	# Skip  comment lines in the module file
	if echo $mod | grep -q '^\s*#' ; then
		continue
	fi

	# Remove comments from module lines if present
#	$mod=$(echo $mod | sed 's/#.*$//')

	# Parse the line to figure out the module name and options
	read -r -a modinfo <<< $mod
	buildflags=""
	modperl=${modinfo[0]}
	rpmname=$(echo $modperl | sed 's/::/-/g')
	pkgfiles=""
	nelem=${#modinfo[@]}
	let nelem=${nelem}-1
	if [ ${nelem}  -gt 0 ]; then
		for i in `seq 1 ${nelem}`; do
			elem=${modinfo[$i]}
			echo $elem | grep -q '{'
			if [ $? -eq 0 ]; then
				bp=$(echo $elem | sed -e 's/^{//' -e 's/}$//')
#				echo $bp | grep -q '%files'
				echo "Buid parameter: $bp"
				if [[ $bp == %files* ]]; then
					echo -e "Setting pkgfiles: $bp"
					pkgfiles=$bp
				else
#				if [ $? -ne 0 ]; then
					bp=$(echo $bp | sed -e 's/:/ /')
					bp=$(echo $bp | sed -e 's#$CWD#'$MYPATH'#')
					buildflags="$buildflags $bp"
					echo ">> Build flags: $buildflags"
				fi
			else
				rpmname=$elem
			fi
		done
	fi
	echo -e ">> $modperl $rpmname $buildflags $pkgfiles"

	SPECFILE=${WORKDIR}/SPECS/opt-perl-${rpmname}.spec
	# If the SPECFILE does not exist or is zero size, then generate a new SPECFILE
	if [ ! -f $SPECFILE ] || [ ! -s $SPECFILE ]; then
		echo -e "Generating SPEC file"
		## Create the SPEC file for this RPM. Try twice. It's perl, don't ask why
		retries=2
		for i in `seq 1 $retries`; do	
			/usr/bin/yes | /opt/perl/bin/cpantorpm  $buildflags --add-require "opt-perl" --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only $modperl
			if [ $? -eq 0 ]; then break; fi
		done
		if [ $? -ne 0 ]; then code=$?; cleanup; exit $code; fi

		echo -e "Fixing SPEC file to use opt-perl"
		# Fix-up the  cpantorpm-generated spec file.
		/bin/sed -i -e "s#^%setup -T -D#%setup #" -e 's#perl/lib/perl5#perl/lib#g' $SPECFILE
		SPECFILETMP=$SPECFILE.$$
		awk -- '/Provides:[[:space:]]+perl/{print gensub("perl","opt-perl",1);next} /Requires:[[:space:]]+perl/{print gensub("perl","opt-perl",1);next} {print}' $SPECFILE > $SPECFILETMP
		awk -f remrequires $SPECFILETMP > $SPECFILE
		if [ $? -ne 0 ]; then
			code=$?
			cleanup
			exit $code
		fi
		if [ "x$pkgfiles" != "x" ]; then
			echo "overriding files in package spec ${SPECFILE}"
			perl -pi -e 'if ( $replace and ( eof or m/^%(?!defattr|wdoc|config|attr|verify|docdir|dir)/ ) ) { $replace=0; print qq('$pkgfiles'\n\n); } if ( m/^%files/ ) { $replace=1; } if ( $replace ) { $_=""; }' $SPECFILE
#			sed -i -e "s#%files#$pkgfiles#" $SPECFILE

		fi
		BUILDRPM=true
	else
		echo -e "SPEC file exists.  Not generating a new one."
		BUILDRPM=false
	fi

	# Download the source tarball for this RPM
	SOURCEFILE=$(perl -ne 'm#^\s*Source\d+:.+/(.+)$# && print $1' ${SPECFILE})
	if [ ! -f ${WORKDIR}/SOURCES/$SOURCEFILE ]; then
		echo -e "Downloading source file from CPAN."
		(cd ${WORKDIR}/SOURCES; /opt/perl/bin/cpan -g $modperl)
	else
		echo -e "Source file exists.  Skipping downlaod."
	fi

	
	RPMVER=$(perl -ne 'm#^\s*Version:\s*([A-z0-9.]+)$# &&  print $1' ${SPECFILE})
	rpm="opt-perl-${rpmname}"

	# Build the RPM
	if [ "$BUILDRPM" == false ] && ls ${WORKDIR}/RPMS/*/${rpm}-${RPMVER}* &>>/dev/null; then
		echo -e "The SPEC file was not regenerated and the RPM ${rpm}-${RPMVER} exists.  Skipping rebuild."
	else
		echo "Building the RPM"
		rpmbuild -ba ${WORKDIR}/SPECS/${rpm}.spec
		if [ $? -ne 0 ]; then
			code=$?
			cleanup
			exit $code
		fi
	fi

	# Install the just-built module. This is to satisfy dependencies for subsequent
	# builds
	if ! rpm -q $rpm-${RPMVER} &>>/dev/null ; then
		if [ ! -f ${WORKDIR}/Makefile ]; then 
			echo -e "Installing RPM using yum -y install"
			#find ${WORKDIR}/RPMS -type f -name "${rpm}-*" -exec sudo yum -y install {} \; -print
			sudo yum -y install ${WORKDIR}/RPMS/*/${rpm}-${RPMVERS}*.rpm
			YUMSTATUS=$?
		else
			pushd ${WORKDIR}
			echo -e "Installing RPM using yum local repo"
			make createlocalrepo
			sudo yum -c yum.conf -y install ${rpm}
			YUMSTATUS=$?
			popd
		fi
		if [ $YUMSTATUS -ne 0 ]; then
			echo "Yum install failed.  Please fix the issue with the RPM before proceeding."
			cleanup
			exit $YUMSTATUS
		fi
	else
		echo "RPM is already installed. Skipping"
	fi
done < $1
cleanup
