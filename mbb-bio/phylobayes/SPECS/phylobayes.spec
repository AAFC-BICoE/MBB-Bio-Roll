%define name		phylobayes
%define release		1
%define version 	4.1c
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		Phylogenetic reconstruction using infinite mixtures	
License: 		GPL
URL:			http://megasun.bch.umontreal.ca/People/lartillot/www/index.htm
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.tar.gz
Prefix: 		%{_prefix}	
Group: 			Bioinformatics/Phylogenetics
AutoReq:		yes

%description
PhyloBayes (Lartillot et al, 2009) is a Bayesian Monte Carlo Markov Chain (MCMC) sampler for phylogenetic reconstruction. Compared to other phylogenetic MCMC samplers, the main distinguishing feature of PhyloBayes is the underlying probabilistic model, CAT (Lartillot and Philippe, 2004). CAT is an infinite mixture model accounting for site-specific amino-acid or nucleotide preferences. It is well suited to phylogenomic studies using large multigene alignments.

%prep
%setup -q -n %{name}%{version}

%build
mkdir bin
pushd sources
make -j`nproc` PROGSDIR='../bin'

%install
mkdir -p %{buildroot}%{_bindir} 
cp -r bin/* %{buildroot}%{_bindir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%defattr(755,root,root,755)
%{_bindir}
