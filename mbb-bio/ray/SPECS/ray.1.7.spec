# This is a sample spec file for wget

### define _topdir	 	/home/rpmbuild/rpms/ray
%define name			Ray
%define release		cl1
%define version 	1.7
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 		Parallel de novo genome assemblies for parallel DNA sequencing
License: 		GNU GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		/opt/bio
URL:			http://denovoassembler.sourceforge.net/
Group: 			Development/Tools
AutoReq:		yes

%description
Ray is a parallel software that computes de novo genome assemblies with next-generation sequencing data.

%prep
%setup -q

%build
make PREFIX=$RPM_BUILD_ROOT%{installroot}

%install
make install

%files
%defattr(755,root,root)
%{installroot}
