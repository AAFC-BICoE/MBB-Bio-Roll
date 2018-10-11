
%define name		BEAST2
%define src_name	beast2
%define release		1
%define version 	2.5.1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 

BuildRoot:		%{buildroot}
Summary: 		Bayesian evolutionary analysis by sampling trees
License: 		Lesser GPL|https://code.google.com/p/beast-mcmc
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-v%{version}.tar.gz
Patch0:			build.xml.patch
Packager:	        Glen Newton <glen.newton@agr.gc.ca>
Prefix: 		%{installroot}
Group: 			Applications/BioInformatics/Phylogenetics
AutoReq:		yes
URL:                    http://beast2.org/

BuildRequires:		java-1.8.0-openjdk-devel
Requires:		java >= 1:1.8.0

%description
BEAST is a cross-platform program for Bayesian MCMC analysis of molecular sequences. It is entirely orientated towards rooted, time-measured phylogenies inferred using strict or relaxed molecular clock models. It can be used as a method of reconstructing phylogenies but is also a framework for testing evolutionary hypotheses without conditioning on a single tree topology. BEAST uses MCMC to average over tree space, so that each tree is weighted proportional to its posterior probability. We include a simple to use user-interface program for setting up standard analyses and a suit of programs for analysing the results. 

Bouckaert, R., Heled, J., Kühnert, D., Vaughan, T., Wu, C-H., Xie, D., Suchard, MA., Rambaut, A., & Drummond, A. J. (2014). BEAST 2: A Software Platform for Bayesian Evolutionary Analysis. PLoS Computational Biology, 10(4), e1003537. doi:10.1371/journal.pcbi.1003537 

Book: http://www.cs.auckland.ac.nz/~remco/BEASTBook/ComputationalEvolutionBook140115.pdf
Wiki: http://www.beast2.org/wiki/index.php/Main_Page

%prep
%setup -qn %{src_name}-%{version}
%patch0

%build
unset JAVA_HOME
ant linux

%install
mkdir -p %{buildroot}%{installroot}/
cd release/Linux/beast
cp -r . %{buildroot}%{installroot}
rm %{buildroot}%{installroot}/bin/*
for i in bin/*; do
	mv $i %{buildroot}%{installroot}/${i}2
done

%files
%defattr(0644,root,root,0755) 
%dir %{installroot}
%{installroot}/examples
%{installroot}/images
%{installroot}/lib
%{installroot}/LICENSE.txt
%{installroot}/README.txt
%{installroot}/templates
%defattr(0755,root,root,0755)
%{installroot}/bin


