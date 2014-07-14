# This is a  spec file for gff2ps

### define _topdir	 	/home/rpmbuild/rpms/gff2ps
%define name		gff2ps
%define release		1
%define version 	v0.98d
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	gff2ps is a program for visualizing annotations of genomic sequences.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}_%{version}.gz
Patch0:         %{name}-%{version}-%{release}.patch0
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://genome.crg.es/software/gfftools/GFF2PS.html
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GNU GPL
AutoReq:	yes

%description
gff2ps is a program for visualizing annotations of genomic sequences. The
program takes as input the annotated features on a genomic sequence in GFF
format, and produces a visual output in PostScript. It can be used in a very
simple way, because it assumes that the GFF file itself carries enough
formatting information, but it also allows through a number of options and/or a
configuration file, for a great degree of customization. 

%prep
%setup -q -T -c -n gff2ps-v0.98d
gunzip -c ../../SOURCES/gff2ps_v0.98d.gz > gff2ps
%patch -P 0 -p1

%build

%install
mkdir -p %{buildroot}%{installroot}
cp gff2ps %{buildroot}%{installroot}

%files
%defattr(755,root,root)
%{installroot}
