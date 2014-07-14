# This is a  spec file for Glimmer

### define _topdir	 	/home/rpmbuild/rpms/glimmer
%define name		glimmer
%define release		2
%define version 	3.02
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	Glimmer is a system for finding genes in microbial DNA, especially the genomes of bacteria, archaea, and viruses.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}302.tar.gz
Patch0:		%{name}-%{version}-%{release}.patch0
Patch1:         %{name}-%{version}-%{release}.patch1
Patch2:         %{name}-%{version}-%{release}.patch2
Patch3:         %{name}-%{version}-%{release}.patch3
Patch4:         %{name}-%{version}-%{release}.patch4
Patch5:         %{name}-%{version}-%{release}.patch5
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://cbcb.umd.edu/software/glimmer/
Prefix: 	/opt/bio
Group: 		Development/Tools
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
%setup -q -n glimmer3.02/src
%patch -P 0 -p2
%patch -P 1 -p2
%patch -P 2 -p2
cd ..
pwd
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1

%build
make

%install
mkdir -p %{buildroot}%{installroot}
rm ../bin/test
cp -r ../bin %{buildroot}%{installroot}
cp -r ../scripts %{buildroot}%{installroot}

%files
%defattr(755,root,root,755)
%{installroot}

