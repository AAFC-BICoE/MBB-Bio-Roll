
%define name		ncbi-blast
%define release		1
%define version 	2.7.1+
%define	lmdb_version	0.9.22
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}+

BuildRoot:	%{buildroot}
Summary: 		BLAST+ is a new suite of BLAST tools that utilizes the NCBI C++ Toolkit
License: 		Public Domain
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}-src.tar.gz
Patch0:			env-perl.patch
Patch1:			env-python.patch
Prefix: 		%[installroot}
Group: 			Bioinformatics/Alignment	
AutoReq:		yes
URL:			https://blast.ncbi.nlm.nih.gov/Blast.cgi

BuildRequires:		mesa-libOSMesa-devel
BuildRequires:		opt-lmdb
BuildRequires:		opt-perl
BuildRequires:		opt-python-3
BuildRequires:		bzip2-devel	
BuildRequires:		zlib-devel

Requires:	opt-perl(Archive::Tar)
Requires:	opt-perl(Digest::MD5)
Requires:	opt-perl(File::Temp)
Requires:	opt-perl(File::stat)
Requires:	opt-perl(Getopt::Long)
Requires:	opt-perl(List::MoreUtils)
Requires:	opt-perl(Net::FTP)
Requires:	opt-perl(Pod::Usage)
Requires:	opt-perl(constant)
Requires:	opt-perl(strict)
Requires:	opt-perl(warnings)

Provides:	libncbi_xloader_genbank-dll.so()(64bit)
Provides:	libncbi_xreader-dll.so()(64bit)
Provides:	libncbi_xreader_cache-dll.so()(64bit)
Provides:	libncbi_xreader_id1-dll.so()(64bit)
Provides:	libncbi_xreader_id2-dll.so()(64bit)


%global __requires_exclude ^perl

%description
The new BLAST command-line applications, compared to the current BLAST tools, demonstrate substantial speed improvements for long queries as well as chromosome length database sequences. We have also improved the user interface of the command-line applications.

%prep

%setup -qn %{name}-%{version}-src/c++
%patch0 -p2
%patch1 -p2

%build

LMDB=$(dirname $(dirname $(rpm -ql opt-lmdb | grep -e 'lmdb.so$' | head -n 1)))
PERL=$(dirname $(dirname $(rpm -ql opt-perl | grep -e 'bin/perl$' | head -n 1)))
PYTHON=$(dirname $(dirname $(rpm -ql opt-python-3 | grep -e 'python3.6$' | head -n 1)))
./configure --prefix=%{installroot}  --with-openmp --with-64 \
        --with-check --with-hard-runpath --with-lfs --with-mysql --with-mesa --with-sge=$SGE_ROOT \
        --with-boost --with-z --with-bz2 --with-lmdb=$LMDB --with-perl=$PERL --with-python=$PYTHON

make -j `nproc`

%install
make install prefix=%{buildroot}%{installroot}

%files
%defattr(-,root,root)
%dir %{installroot}
%{installroot}/*

