# This is a  spec file for Critica

### define _topdir	 	/home/rpmbuild/rpms/critica
%define name		critica
%define release		1
%define version 	105
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	Critica (Coding Region Identification Tool Invoking Comparative Analysis) is a microbial gene finder.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}%{version}.tar.gz
Patch0:		%{name}%{version}-%{release}.patch0
Patch1:         %{name}%{version}-%{release}.patch1
Patch2:         %{name}%{version}-%{release}.patch2
Patch3:         %{name}%{version}-%{release}.patch3
Patch4:         %{name}%{version}-%{release}.patch4
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://www.ttaxus.com/software.html
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GNU GPL
AutoReq:	yes

%description
Critica (Coding Region Identification Tool Invoking Comparative Analysis) is a
microbial gene finder that combines traditional approaches to the problem with a
novel comparative analysis. If, in a nucleotide alignment, a pair of ORFs can be
found in which the conceptual translated products are more conserved than would
be expected from the amount of conservation at the nucleotide level, this is
evolutionary evidence that the DNA sequences are protein coding. Regions found
by this method are used to generate traditional dicodon frequencies for further
analysis. Critica thus is not dependent on (often erroneous) sequence
annotations, which many other algorithms base their training sets upon, and uses
comparative information in a more biologically meaningful way than a simple
similarity search. Critica was used in the Archeoglobus fulgidus and Aquifex
aeolicus genome projects and is still in use by several groups.

%prep
%setup -q -n critica105
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1

%build
make

%install
mkdir -p %{buildroot}%{installroot}
cp addlongorfs critica dicodontable empirical-matrix extractcoding intergenic lookat motiffind removeoverlaps reportscore scanblastpairs translate %{buildroot}%{installroot}
pwd
cp -r scripts %{buildroot}%{installroot}

%files
%defattr(755,root,root)
%{installroot}
