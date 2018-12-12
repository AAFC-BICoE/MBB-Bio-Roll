%define name		FastTree
%define release		1
%define version		2.1.10
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		FastTree
License: 		Public Domain|http://www.microbesonline.org/fasttree/FastTree.c	
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz 
Prefix: 		%{installroot}
Group: 			Development/Tools
AutoReq:		yes

%description
inferring approximately-maximum-likelihood trees for large multiple sequence alignments.

%prep
%setup -q 

%build
gcc -Wall -O3 -finline-functions -funroll-loops -o FastTree -lm FastTree.c

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/bin
cp FastTree $RPM_BUILD_ROOT%{installroot}/bin

%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc ChangeLog
%defattr(755,root,root)
%{installroot}/bin/FastTree
