
%define name		ncbi-blast
%define release		cl1
%define version 	2.2.31+
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}+

BuildRoot:	%{buildroot}
Summary: 		BLAST+ is a new suite of BLAST tools that utilizes the NCBI C++ Toolkit
License: 		Public Domain
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}-src.tar.bz2
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes
URL:			ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/

%description
The new BLAST command-line applications, compared to the current BLAST tools, demonstrate substantial speed improvements for long queries as well as chromosome length database sequences. We have also improved the user interface of the command-line applications.

%prep

%setup  -qn ncbi-blast-2.2.31+-src


%build
export NPROC=`nproc`;export NTHREADS=`expr 2 \* $NPROC`;cd c++; ./configure --without-boost; make -j ${NTHREADS}
# nothing to do; using precompiled executables


%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -R * $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
