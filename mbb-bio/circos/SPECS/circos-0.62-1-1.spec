# This is a  spec file for circos
# Note: additional perl modules are required to be installed  
# in order for the circos rpm package to be installed.

### define _topdir	 	/home/rpmbuild/rpms/circos
%define name		circos
%define release		1
%define version 	0.62
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	Circo is a flexible and automatable circular data visualization.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}-1.tgz
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://circos.ca/software/download/circos
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPL-2|https://code.google.com/p/circos	
AutoReq:	yes

%description
Circos is a program for the generation of publication-quality, circularly
composited renditions of genomic data and related annotations.  Circos is
particularly suited for visualizing alignments, conservation and intra and
inter-chromosomal relationships.  Also, Circos is useful to visualize any type
of information that benefits from a circular layout. Thus, although it has been
designed for the field of genomics, it is sufficiently flexible to be used in
other data domains.

%prep
%setup -q -n circos-0.62-1

%build

%install
mkdir -p %{buildroot}%{installroot}
cp -r bin data error etc example fonts lib tiles %{buildroot}%{installroot}

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/data/karyotype/parse.karyotype
%{installroot}/data/karyotype/assembly/parse.assembly
%{installroot}/example/run
