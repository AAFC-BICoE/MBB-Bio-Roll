# This is a  spec file for saps

##define _topdir	 	/home/rpmbuild/rpms/saps
%define name		saps
%define release		2	
%define version 	1996
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	SAPS is a Statistical Analysis of Protein Sequences.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}.sspa.tar.gz
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GNU GPL
URL:		http://brendelgroup.org/bioinformatics2go/
AutoReq:	yes

%description
SAPS (Statistical Analysis of Protein Sequences) evaluates by statistical
criteria a wide variety of protein sequence properties. A full description of
the methods is given in the paper: Methods and  algorithms for statistical
analysis of protein sequences (1992). The output is organized in the following
sections: file name, sequence printout, compositional analysis, charge
distributional analysis (charge  clusters;  high scoring  (un)charged segments;
charge runs and patterns), distribution of other amino acid types (high scoring
hydrophobic and transmembrane segments; cysteine spacings), repetitive
structures (in the amino acid alphabet and in a 11-letter reduced alphabet),
multiplets (counts, spacings, and clusters in the amino acid and charge
alphabets), periodicity analysis, spacing analysis. Each section is annotated
below under its section title.

%prep
%setup -q -n SAPS.SSPA

%build
cd src
make

%install
mkdir -p %{buildroot}%{installroot}
cp -r * %{buildroot}%{installroot}
rm -r %{buildroot}%{installroot}/src
rm %{buildroot}%{installroot}/saps.1
rm %{buildroot}%{installroot}/sspa.1

%files
%defattr(755,root,root,755)
%{installroot}
%defattr(644,root,root,755)
%{installroot}/include
%{installroot}/README
%{installroot}/RECA_ECOLI
%{installroot}/sspa.doc
%{installroot}/testdnapro
%{installroot}/testout_dflag
%{installroot}/testpro
%{installroot}/RECA_BACSU
%{installroot}/saps.doc
%{installroot}/sspaout
%{installroot}/testout
%{installroot}/testout_dna
