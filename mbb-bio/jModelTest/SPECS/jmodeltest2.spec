%define name		jmodeltest2
%define release		1
%define version 	2.1.10
%define timestamp	20160303
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		HPC selection of models of nucleotide substitution
License: 		GNU GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}r%{timestamp}.tar.gz
Patch0:			use-env-phyml.patch
Patch1:			isolate-exec-script.patch
Prefix: 		%{_prefix}
URL:			http://code.google.com/p/jmodeltest2/
Group: 			Bioinformatics/Modeling
AutoReq:		yes

BuildRequires:		ant
BuildRequires:		java-sdk >= 1:1.8.0
Requires:		java >= 1:1.8.0
Requires:		phyml

%description
jModelTest is a tool to carry out statistical selection of best-fit models of nucleotide substitution. It implements five different model selection strategies: hierarchical and dynamical likelihood ratio tests (hLRT and dLRT), Akaike and Bayesian information criteria (AIC and BIC), and a decision theory method (DT). It also provides estimates of model selection uncertainty, parameter importances and model-averaged parameter estimates, including model-averaged tree topologies. jModelTest 2 includes High Performance Computing (HPC) capabilities and additional features like new strategies for tree optimization, model-averaged phylogenetic trees (both topology and branch lenght), heuristic filtering and automatic logging of user activity. 

%prep
%setup -q -n %{name}-%{version}r%{timestamp}
%patch0 -p 1
%patch1 -p 1

%build
ant jar

%install
mkdir -p %{buildroot}%{_bindir}

cp dist/runjmodeltest-gui.sh %{buildroot}%{_bindir}
mv dist/jModelTest.jar %{buildroot}%{_prefix}
mv dist/conf dist/lib %{buildroot}%{_prefix}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc COPYING
%doc README.md
%{_prefix}/lib
%{_prefix}/conf
%{_prefix}/jModelTest.jar
%defattr(755,root,root,755)
%{_bindir}
