### define _topdir	 	/home/rpmbuild/rpms/phylobayesmpi
%define name			phylobayesmpi
%define release		1
%define version 	1.4e
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	A Bayesian software for phylogenetic reconstruction using mixture models, MPI
License: 		GPL3
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Packager:	Glen Newton <glen.newton@grc.gc.ca>
Prefix: 		/opt/bio
Url:                    http://megasun.bch.umontreal.ca/People/lartillot/www/downloadmpi.html
Group: 			Development/Tools
AutoReq:		yes

%description
PhyloBayes-MPI is a Bayesian Markov chain Monte Carlo (MCMC) sampler for phyloge-
netic inference exploiting a message-passing-interface system for multi-core computing. The
program will perform phylogenetic reconstruction using either nucleotide, protein, or codon
sequence alignments. Compared to other phylogenetic MCMC samplers, the main distin-
guishing feature of PhyloBayes is the use of non-parametric methods for modeling among-site
variation in nucleotide or amino-acid propensities.


%prep
%setup -q

%build
cd sources
make

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r data/* $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
