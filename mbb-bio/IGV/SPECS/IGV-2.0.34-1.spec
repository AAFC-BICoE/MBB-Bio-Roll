# This is a sample spec file for wget

%define name		IGV
### define _topdir	 	/home/rpmbuild/rpms/IGV
%define release		1
%define version 	2.0.34
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 
%define __jar_repack	0

BuildRoot:		%{buildroot}
Summary: 		IGV
License: 		GNU LGPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tgz
Prefix: 		/opt/bio
URL:			http://www.broadinstitute.org/igv/
Group: 			Development/Tools
AutoReq:		yes

%description
The Integrative Genomics Viewer (IGV) is a high-performance visualization tool for interactive exploration of large, integrated genomic datasets. It supports a wide variety of data types, including array-based and next-generation sequence data, and genomic annotations.

%prep
%setup -q

%build
#jar already created, nothing to build 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
cp igv.jar  $RPM_BUILD_ROOT%{installroot}/

%files
%defattr(755,root,root)
%{installroot}
