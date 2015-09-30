
%define name		BEAST2

%define release		1
%define version 	v2
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 

BuildRoot:		%{buildroot}
Summary: 		Bayesian evolutionary analysis by sampling trees
License: 		Lesser GPL|https://code.google.com/p/beast-mcmc
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		BEAST.v2.3.1.tar.bz2
Packager:	        Glen Newton <glen.newton@agr.gc.ca>
Prefix: 		/opt/bio
Group: 			Applications/BioInformatics/Phylogenetics
AutoReq:		yes
URL:                    http://beast2.org/

%description
BEAST is a cross-platform program for Bayesian MCMC analysis of molecular sequences. It is entirely orientated towards rooted, time-measured phylogenies inferred using strict or relaxed molecular clock models. It can be used as a method of reconstructing phylogenies but is also a framework for testing evolutionary hypotheses without conditioning on a single tree topology. BEAST uses MCMC to average over tree space, so that each tree is weighted proportional to its posterior probability. We include a simple to use user-interface program for setting up standard analyses and a suit of programs for analysing the results. 

Bouckaert, R., Heled, J., Kühnert, D., Vaughan, T., Wu, C-H., Xie, D., Suchard, MA., Rambaut, A., & Drummond, A. J. (2014). BEAST 2: A Software Platform for Bayesian Evolutionary Analysis. PLoS Computational Biology, 10(4), e1003537. doi:10.1371/journal.pcbi.1003537 

Book: http://www.cs.auckland.ac.nz/~remco/BEASTBook/ComputationalEvolutionBook140115.pdf
Wiki: http://www.beast2.org/wiki/index.php/Main_Page


%prep
%setup -qn BEAST.v2.3.1

%build

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
cp -r *  $RPM_BUILD_ROOT%{installroot}

%files
%defattr(0755,root,root) 
%{installroot}
