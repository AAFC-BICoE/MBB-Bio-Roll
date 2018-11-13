%define name		Ray
%define release		1
%define version 	2.3.1
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define installroot	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		Parallel de novo genome assemblies for parallel DNA sequencing
License: 		GPLv3,LGPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.bz2
Prefix: 		%{_prefix}
URL:			http://denovoassembler.sourceforge.net/
Group: 			Bioinformatics/Assembly
AutoReq:		yes

%description
Ray is a parallel software that computes de novo genome assemblies with next-generation sequencing data.

%prep
%setup -q

%build
make -j 

%install
mkdir -p %{buildroot}%{_bindir}
cp Ray %{buildroot}%{_bindir}

%files
%defattr(644,root,root,755)
%doc Documentation/*
%doc AUTHORS
%doc LICENSE.txt
%defattr(755,root,root,755)
%{_bindir}
