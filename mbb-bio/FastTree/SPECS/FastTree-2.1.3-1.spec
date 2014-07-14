# This is a sample spec file for wget
# TODO: Add documentation 
#
### define _topdir	 	/home/rpmbuild/rpms/FastTree
%define name		FastTree
%define release		1
%define version		2.1.3	
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}


BuildRoot:		%{buildroot}
Summary: 		FastTree
License: 		Public Domain|http://www.microbesonline.org/fasttree/FastTree.c	
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz 
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
inferring approximately-maximum-likelihood trees for large multiple sequence alignments.

%prep
%setup -q 

%build
gcc -Wall -O3 -finline-functions -funroll-loops -o FastTree -lm %{name}-%{version}.c

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp FastTree $RPM_BUILD_ROOT%{installroot}


%files
%defattr(755,root,root)
%{installroot}
