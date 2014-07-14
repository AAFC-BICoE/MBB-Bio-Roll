### define _topdir	 	/home/rpmbuild/rpms/samtools
%define name		samtools
%define release		1
%define version 	0.1.19
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 		SAM (Sequence Alignment/Map) format for storing large nucleotide sequence alignments
License: 		MIT|http://seqanswers.com/wiki/SAMtools
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.bz2
Source1: 		%{name}-0.1.19.tar.bz2
Patch0:			samtools-0.1.19.patch
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes
Url:                   http://samtools.sourceforge.net/

%description
SAM (Sequence Alignment/Map) format is a generic format for storing large
nucleotide sequence alignments.  SAM Tools provide various utilities for
manipulating alignments in the SAM format, including sorting, merging, indexing
and generating alignments in a per-position format.

Main package comes with perl scripts 


%prep
%setup -q
%setup -T -a 1 -D -c samtools-0.1.19
%patch -p1 -P 0 

%build
make; make razip 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
mkdir -p $RPM_BUILD_ROOT%{installroot}/include/bam
mkdir -p $RPM_BUILD_ROOT%{installroot}/lib
mkdir -p $RPM_BUILD_ROOT%{installroot}/perl
cp samtools razip bcftools/bcftools $RPM_BUILD_ROOT%{installroot}
cp *.h $RPM_BUILD_ROOT%{installroot}/include/bam
cp *.a $RPM_BUILD_ROOT%{installroot}/lib
cp ./misc/*.pl $RPM_BUILD_ROOT%{installroot}/perl


%files
%defattr(644,root,root,755)
%dir %attr(755,root,root) %{installroot}
%{installroot}/include
%{installroot}/lib
%attr(755,root,root) %{installroot}/samtools
%attr(755,root,root) %{installroot}/bcftools
%attr(755,root,root) %{installroot}/razip 
%attr(755,root,root) %{installroot}/perl 


