# This is a  spec file for Elph

### define _topdir	 	/home/rpmbuild/rpms/ELPH
%define name		ELPH
%define release		1
%define version 	1.0.1
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	ELPH is a general-purpose Gibbs sampler for finding motifs in a set of DNA or protein sequences.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://www.cbcb.umd.edu/software/ELPH/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        Artistic License
AutoReq:	yes

%description
ELPH is a general-purpose Gibbs sampler for finding motifs in a set of DNA or
protein sequences. The program takes as input a set containing anywhere from a
few dozen to thousands of sequences, and searches through them for the most
common motif, assuming that each sequence contains one copy of the motif. We
have used ELPH to find patterns such as ribosome binding sites (RBSs) and exon
splicing enhancers (ESEs). See below for instructions on downloading the
complete system, including source code.  

%prep
%setup -q -n ELPH/sources

%build
make

%install
mkdir -p %{buildroot}%{installroot}
cp ./elph  %{buildroot}%{installroot}

%files
%defattr(755,root,root)
%{installroot}
