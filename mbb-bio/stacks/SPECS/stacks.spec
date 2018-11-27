### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/stacks
%define name			stacks
%define release			1 
%define version			1.35
%define installroot		/opt/bio/%{name}
%define buildroot		%{_topdir}/%{name}-%{version}-root
%define _prefix			%{installroot}

Summary:   Stacks is a software pipeline for building loci from short-read sequences, such as those generated on the Illumina platform. 
Name: 		%{name}
Version:	%{version}
Release:	%{release}
Source:		%{name}-%{version}.tar.gz
License:	GNU GPL-3.0
Packager:	Xie Qiu <xie.qiu@agr.gc.ca>
Group:		Development/Libraries
BuildRoot:	%{buildroot}
Prefix:		%{_prefix}
Vendor:		Julian Catchen <jcatchen@illinois.edu>, Angel Amores <amores@uoregon.edu >, Paul Hohenlohe <hohenlohe@uidaho.edu >, Bill Cresko <wcresko@uoregon.edu >
Url:		http://catchenlab.life.illinois.edu/stacks/
AutoReq:	yes

BuildRequires:	samtools
BuildRequires:	opt-sparsehash

Requires:	opt-perl(DBI)
Requires:	opt-perl(File::Spec)
Requires:	opt-perl(File::Temp)
Requires:	opt-perl(Net::SMTP)
Requires:	opt-perl(POSIX)
Requires:	opt-perl(Spreadsheet::WriteExcel)
Requires:	opt-perl(constant)
Requires:	opt-perl(strict)

%global __requires_exclude ^perl

%description
Stacks is a software pipeline for building loci from short-read sequences, such as those generated on the Illumina platform. Stacks was developed to work with restriction enzyme-based data, such as RAD-seq, for the purpose of building genetic maps and conducting population genomics and phylogeography. 

%prep
%setup -q -n %{name}-%{version}

%build
sh autogen.sh

BAM_CONFIG=$(rpm -ql samtools | grep 'samtools/include/bam$' | head -n1)
BAM_LIB=$(rpm -ql samtools | grep 'samtools/lib$' | head -n1)
SPHASH_CONFIG=$(rpm -ql opt-sparsehash | grep 'sparsehash/include$' | head -n1)

./configure --prefix=%{_prefix} --enable-bam --with-bam-include-path=$BAM_CONFIG --with-bam-lib-path=$BAM_LIB --enable-sparsehash --with-sparsehash-include-path=$SPHASH_CONFIG

make -j`nproc`

%install
mkdir -p $RPM_BUILD_ROOT%{_prefix}
make install DESTDIR=$RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_datarootdir}
%defattr(755,root,root,755)
%{_bindir}

