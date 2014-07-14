#define the environmental variable $JMODELTEST_HOME as /opt/bio/jModelest 

%define name		jmodeltest
### define _topdir	 	/home/rpmbuild/rpms/jModelTest 
%define release		1
%define version 	2.1.1
%define timestamp	20120731 
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 
%define __jar_repack	0
%define debug_package	%{nil}


BuildRoot:		%{buildroot}
Summary: 		HPC selection of models of nucleotide substitution
License: 		GNU GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}-%{timestamp}.tar.gz
Prefix: 		/opt/bio
URL:			http://code.google.com/p/jmodeltest2/
Group: 			Development/Tools
AutoReq:		yes

%description
jModelTest is a tool to carry out statistical selection of best-fit models of nucleotide substitution. It implements five different model selection strategies: hierarchical and dynamical likelihood ratio tests (hLRT and dLRT), Akaike and Bayesian information criteria (AIC and BIC), and a decision theory method (DT). It also provides estimates of model selection uncertainty, parameter importances and model-averaged parameter estimates, including model-averaged tree topologies. jModelTest 2 includes High Performance Computing (HPC) capabilities and additional features like new strategies for tree optimization, model-averaged phylogenetic trees (both topology and branch lenght), heuristic filtering and automatic logging of user activity. 

%prep
%setup -q

%build
#jar already created, nothing to build 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r *  $RPM_BUILD_ROOT%{installroot}
rm $RPM_BUILD_ROOT%{installroot}/exe/phyml/PhyML_3.0_macOS_i386  
rm $RPM_BUILD_ROOT%{installroot}/exe/phyml/PhyML_3.0_linux32
rm $RPM_BUILD_ROOT%{installroot}/exe/phyml/PhyML_3.0_win32.exe
rm $RPM_BUILD_ROOT%{installroot}/*.bat   

%files
%defattr(644,root,root,755)
%{installroot}
%attr (0755,root,root) %{installroot}/runjmodeltest-gui.sh
%attr (0755,root,root) %{installroot}/exe/phyml/PhyML_3.0_linux64
%attr (0755,root,root) %{installroot}/runjmodeltest-cluster.sh

