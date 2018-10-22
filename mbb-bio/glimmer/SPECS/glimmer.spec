%define name		glimmer
%define release		2
%define version 	3.02b
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	Glimmer is a system for finding genes in microbial DNA, especially the genomes of bacteria, archaea, and viruses.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}302b.tar.gz
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>
URL:            http://cbcb.umd.edu/software/glimmer/
Prefix: 	%{installroot}
Group: 		Bioinformatics/Gene Finding
License:        Open Source
AutoReq:	yes

%description
Glimmer is a system for finding genes in microbial DNA, especially the genomes
of bacteria, archaea, and viruses. Glimmer (Gene Locator and Interpolated Markov
ModelER) uses interpolated Markov models (IMMs) to identify the coding regions
and distinguish them from noncoding DNA. The IMM approach, described in our
Nucleic Acids Research paper on Glimmer 1.0 and in our subsequent paper on
Glimmer 2.0, uses a combination of Markov models from 1st through 8th-order,
weighting each model according to its predictive power. 
Glimmer uses 3-periodic nonhomogenous Markov models in its IMMs.  Glimmer was
the primary microbial gene finder used at The Institute for Genomic Research
(TIGR), where it was first developed, and has been used to annotate the complete
genomes of over 100 bacterial species from TIGR and other labs. Glimmer3
predictions are available for all NCBI RefSeq bacterial genomes at their ftp
site. 

%prep
%setup -q -n %{name}3.02/src

%build
make -j `nproc`

%install
mkdir -p %{buildroot}%{installroot}
rm ../bin/test
cp -r ../bin %{buildroot}%{installroot}

%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc ../LICENSE
%doc glim302notes.pdf
%defattr(755,root,root,755)
%{installroot}/bin

