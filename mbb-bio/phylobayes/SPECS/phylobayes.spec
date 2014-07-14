### define _topdir	 	/home/rpmbuild/rpms/phylobayes
%define name		phylobayes
%define release		cl1
%define version 	3.3b
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}

BuildRoot:		%{buildroot}
Summary: 		Phylogenetic reconstruction using infinite mixtures	
License: 		GPL
URL:			http://megasun.bch.umontreal.ca/People/lartillot/www/index.htm
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
PhyloBayes (Lartillot et al, 2009) is a Bayesian Monte Carlo Markov Chain (MCMC) sampler for phylogenetic reconstruction. Compared to other phylogenetic MCMC samplers, the main distinguishing feature of PhyloBayes is the underlying probabilistic model, CAT (Lartillot and Philippe, 2004). CAT is an infinite mixture model accounting for site-specific amino-acid or nucleotide preferences. It is well suited to phylogenomic studies using large multigene alignments.


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
