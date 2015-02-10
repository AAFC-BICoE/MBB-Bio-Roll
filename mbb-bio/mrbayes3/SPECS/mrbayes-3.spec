# This is a sample spec file for wget
# TODO: Add documentation 
#
### define _topdir	 	/home/rpmbuild/rpms/mrbayes
%define name		mrbayes3
%define release		2
%define version 	3.2.4
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}


BuildRoot:		%{buildroot}
Summary: 		A free software program which performs Bayesian inference of phylogeny. 
License: 		GNU GPL
URL:			http://mrbayes.sourceforge.net/
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		mrbayes-%{version}.tar.bz2
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
MrBayes is a program for Bayesian inference and model choice across a wide range of phylogenetic and evolutionary models. MrBayes uses Markov chain Monte Carlo (MCMC) methods to estimate the posterior distribution of model parameters.
Local Use:
 Need to set LD_LIBRARY_PATH to: /opt/openmpi/lib:/opt/bio/beagle-lib-2/lib

%prep
%setup -qn mrbayes-%{version} 

%build
cd ./src 
autoconf 
./configure --with-beagle=/opt/bio/beagle-lib-2 --enable-mpi 
#./configure --with-beagle=no --enable-mpi 
make -j

%install
cd ./src
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp mb ${RPM_BUILD_ROOT}%{installroot}



%files
%defattr(755,root,root,755)
%{installroot}
