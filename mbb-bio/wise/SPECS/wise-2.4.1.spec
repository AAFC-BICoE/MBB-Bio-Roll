
%define name			wise
%define src_name		wise
%define release		1
%define version 	2.4.1
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	Wise2 is a package focused on comparisons of biopolymers, commonly DNA sequence and protein sequence. 
License: 		Open Source, Multiple (BSD, GPL, 
Name: 			%{name}
Version: 		%{version}
Packager:   Glen Newton <glen.newton@agr.gc.ca>
Release: 		%{release}
Source: 		%{src_name}%{version}.tar.gz
Patch0:         %{name}_%{version}.patch
Prefix: 		/opt/bio
Group: 			Applications/BioInformatics/Alignment
URL:			https://www.ebi.ac.uk/~birney/wise2/
AutoReq:		yes

%description
Wise2 is a package focused on comparisons of bio polymers, commonly DNA sequence and protein sequence. There are many other packages which do this, probably the best known being BLAST package (from NCBI) and the Fasta package (from Bill Pearson). 

Wise2 is now a collection of algorithms which generally differ from
the usualy, ``standard'' bioinformatics comparison methods. Probably
the most used algorithm in Wise2 is genewise, which is the
comparison of DNA sequence at the level of its protein
translation. This comparison allows the simultaneous prediction of say
gene structure with homology based alignment. However Wise2 has a number
of other methods which I hope will also appeal to users - promoterwise
for comparing upstream regions, genomewise as a ``protein gene finisher''
tool for combining disparate evidence strands and scanwisep as a
fast but sensitive search method.

%prep
%setup -qn wise2.4.1


%build
cd src
find . -name makefile -exec sed -i 's/glib-config --cflags/pkg-config --libs glib-2.0 --cflags/' {} \;
sed -i 's/getline/getline_new/' HMMer2/sqio.c
find . -name makefile -exec sed -i 's/glib-config --libs/pkg-config --libs glib-2.0/' {} \;
sed -i 's/isnumber/isdigit/' models/phasemodel.c
make clean
make -pipe --jobs=`nproc` all

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/bin
cp src/bin/* $RPM_BUILD_ROOT%{installroot}/bin
strip $RPM_BUILD_ROOT%{installroot}/bin/*

%files
%defattr(755,root,root,755)
%{installroot}
