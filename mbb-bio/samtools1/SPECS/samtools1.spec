%define name            samtools1
%define src_name	samtools
%define release         1
%define version         1.9
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define installroot	/opt/bio/%{name}
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

BuildRoot:		%{buildroot}
Summary:		SAM (Sequence Alignment/Map) format for storing large nucleotide sequence alignments
License:		MIT
Name:			%{name}
Version:		%{version}
Release:		%{release}
Source0:		%{src_name}-%{version}.tar.bz2
Prefix:			%{installroot}
Group:			Bioinformatics/Alignment
AutoReq:		yes
Url:			http://samtools.sourceforge.net/

Provides:		libhts.so.1()(64bit) = %{version}
Provides:		libhts.so.2()(64bit)

Requires:		opt-perl(Carp)
Requires:		opt-perl(Data::Dumper)
Requires:		opt-perl(Digest::MD5)
Requires:		opt-perl(File::Find)
Requires:		opt-perl(File::Path)
Requires:		opt-perl(File::Spec)
Requires:		opt-perl(File::Spec::Functions)
Requires:		opt-perl(File::Temp)
Requires:		opt-perl(Getopt::Long)
Requires:		opt-perl(Getopt::Std)
Requires:		opt-perl(IO::Handle)
Requires:		opt-perl(List::Util)
Requires:		opt-perl(constant)
Requires:		opt-perl(strict)
Requires:		opt-perl(warnings)

%global __requires_exclude ^perl

%description
SAM (Sequence Alignment/Map) format is a generic format for storing large
nucleotide sequence alignments.  SAM Tools provide various utilities for
manipulating alignments in the SAM format, including sorting, merging, indexing
and generating alignments in a per-position format.

%prep
%setup -qn %{src_name}-%{version}

%build
aclocal; autoconf;
./configure --prefix=%{installroot}
make -j`nproc`

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
make install DESTDIR=%{buildroot} prefix=%{installroot}
cd htslib*
make install DESTDIR=%{buildroot} prefix=%{installroot}

%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc AUTHORS
%doc NEWS 
%{_includedir}
%{_datadir}
%defattr(755,root,root,755)
%{_libdir}
%{_bindir}

