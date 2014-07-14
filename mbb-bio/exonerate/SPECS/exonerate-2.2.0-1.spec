#This is a sample spec file for wget
# TODO: Add documentation 
#
### define _topdir	 	/home/rpmbuild/rpms/exonerate
%define name		exonerate
%define release		1
%define version 	2.2.0
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define debug_package 	%{nil} 


BuildRoot:		%{buildroot}
Summary: 		exonerate
License: 		GNU GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tgz
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		no

%description
 exonerate is a generic tool for pairwise sequence comparison.
 It allows you to align sequences using a many alignment models, using either exhaustive dynamic programming, or a variety of heuristics. 


%prep
%setup -q

%build
#already compiled

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r bin $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
