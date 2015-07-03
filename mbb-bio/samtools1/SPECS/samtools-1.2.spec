### define _topdir              /home/rpmbuild/rpms/samtools1
%define name            samtools1
%define release         1
%define version         1.2
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:      %{buildroot}
Summary:                SAM (Sequence Alignment/Map) format for storing large nucleotide sequence alignments
License:                MIT|http://seqanswers.com/wiki/SAMtools
Name:                   %{name}
Version:                %{version}
Release:                %{release}
Source0:                samtools-1.2.tar.bz2
Prefix:                 /opt/bio
Group:                  Development/Tools
AutoReq:                yes
Url:                    http://samtools.sourceforge.net/

%description
SAM (Sequence Alignment/Map) format is a generic format for storing large
nucleotide sequence alignments.  SAM Tools provide various utilities for
manipulating alignments in the SAM format, including sorting, merging, indexing
and generating alignments in a per-position format.

%prep
%setup -qn samtools-1.2

%build
make

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
mkdir -p $RPM_BUILD_ROOT%{installroot}/include/bam
mkdir -p $RPM_BUILD_ROOT%{installroot}/lib
mkdir -p $RPM_BUILD_ROOT%{installroot}/perl
cp samtools $RPM_BUILD_ROOT%{installroot}
cp *.h $RPM_BUILD_ROOT%{installroot}/include/bam
cp *.a $RPM_BUILD_ROOT%{installroot}/lib
cp ./misc/*.pl $RPM_BUILD_ROOT%{installroot}/perl

%files
%defattr(644,root,root,755)
%dir %attr(755,root,root) %{installroot}
%{installroot}/include
%{installroot}/lib
%attr(755,root,root) %{installroot}/samtools
%attr(755,root,root) %{installroot}/perl

%post
mkdir -p %{installroot}/bin
echo '#/bin/bash' > %{installroot}/bin/samtools1
echo 'pushd `dirname $0` > /dev/null' >> %{installroot}/bin/samtools1
echo 'SCRIPTPATH=`pwd -P`' >> %{installroot}/bin/samtools1
echo 'popd > /dev/null' >> %{installroot}/bin/samtools1
echo '$SCRIPTPATH/../samtools $@' >> %{installroot}/bin/samtools1
chmod +x %{installroot}/bin/samtools1
