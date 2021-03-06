%define name		samtools
%define release		1
%define version 	0.1.20
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		SAM (Sequence Alignment/Map) format for storing large nucleotide sequence alignments
License: 		MIT|http://seqanswers.com/wiki/SAMtools
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.bz2
Patch0:			env-perl.patch
Prefix: 		%{installroot}
Group: 			Bioinformatics/Alignment
AutoReq:		yes
Url:			http://samtools.sourceforge.net/

%global __requires_exclude ^perl

Requires:	opt-perl(Carp)
Requires:	opt-perl(Data::Dumper)
Requires:	opt-perl(File::Spec)
Requires:	opt-perl(Getopt::Long)
Requires:	opt-perl(Getopt::Std)
Requires:	opt-perl(List::Util)
Requires:	opt-perl(constant)
Requires:	opt-perl(strict)
Requires:	opt-perl(warnings)

%description
SAM (Sequence Alignment/Map) format is a generic format for storing large
nucleotide sequence alignments.  SAM Tools provide various utilities for
manipulating alignments in the SAM format, including sorting, merging, indexing
and generating alignments in a per-position format.

Main package comes with perl scripts 


%prep
%setup -q
%patch -p1 -P 0 

%build
make -j `nproc`
make -j `nproc` razip 

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_includedir}/bam
mkdir -p %{buildroot}%{_libdir}
cp samtools razip bcftools/bcftools %{buildroot}%{_bindir}
cp *.h %{buildroot}%{_includedir}/bam
cp *.a %{buildroot}%{_libdir}
cp ./misc/*.pl %{buildroot}%{_bindir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc AUTHORS
%doc COPYING
%doc NEWS
%{_includedir}
%defattr(755,root,root,755)
%{_libdir}
%{_bindir}
