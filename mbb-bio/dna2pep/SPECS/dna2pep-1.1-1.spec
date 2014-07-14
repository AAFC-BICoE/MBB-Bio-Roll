#This is a sample spec file for wget
# TODO: Add documentation 
#
### define _topdir	 	/home/rpmbuild/rpms/dna2pep
%define name		dna2pep
%define release		1
%define version 	1.1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}


BuildRoot:		%{buildroot}
Summary: 		Full featured computational translation of DNA to peptide.
License: 		GNU GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tgz
Prefix: 		/opt/bio
Group: 			Development/Tools
URL:			http://www.cbs.dtu.dk/services/VirtualRibosome/download.php
AutoReq:		no
#Requires:		python

%description
dna2pep - full featured computational translation of DNA to peptide.
(The program behind the "Virtual Ribosome" webserver.)

%prep
%setup -q

%build
#already compiled

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp dna2pep.py $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
