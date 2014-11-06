# This is a  spec file for gmap-gsnap

%define name		gmap-gsnap
%define release		1
%define version 	2014.10.22
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	GMAP is a Genomic Mapping and Alignment Program for mRNA and EST Sequences, and GSNAP is a Genomic Short-read Nucleotide Alignment Program.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-2014-10-22.tar.gz
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://research-pub.gene.com/gmap
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        Free for non-commercial use
AutoReq:	yes

%description
GMAP: A Genomic Mapping and Alignment Program for mRNA and EST Sequences, and
GSNAP: Genomic Short-read Nucleotide Alignment Program.

%prep
%setup -q -n gmap-2014-10-22

%build
./configure --prefix=%{installroot} --with-gmapdb=%{installroot}/share/gmapdb MAX_READLENGTH=500 PERL="/usr/bin/env perl"
make

%install
mkdir -p %{buildroot}%{installroot}
cp COPYING NOTICE %{buildroot}%{installroot}
find ./util -executable -type f -exec cp '{}' %{buildroot}%{installroot} \;
find ./src -executable -type f -exec cp '{}' %{buildroot}%{installroot} \;
rm %{buildroot}%{installroot}/*.in

%files
%defattr(755,root,root,755)
%{installroot}
%defattr(644,root,root,755)
%{installroot}/COPYING
%{installroot}/NOTICE
