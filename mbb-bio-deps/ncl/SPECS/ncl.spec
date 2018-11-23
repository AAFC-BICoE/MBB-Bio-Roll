%define debug_package	%{nil}
%define name		opt-ncl
%define src_name	ncl
%define release		1
%define version 	2.1.18
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/lib/%{src_name}
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

BuildRoot:		%{buildroot}
Summary: 		NEXUS Class Library (NCL)
License: 		GPLv2
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz
Prefix: 		%{_prefix}
Group: 			Development/Tools
AutoReq:		yes
Url: http://ncl.sourceforge.net/

%description
The Nexus Class Library (NCL) is a C++ library for interpreting data files
created according to the NEXUS file format used in phylogenetic systematics and
molecular evolution.

%prep
%setup -q -n %{src_name}-%{version}

%build
./configure --prefix=%{_prefix}
make -pipe --jobs=`nproc`

%install
mkdir -p %{buildroot}%{_prefix}
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%doc AUTHORS
%doc COPYING
%doc NEWS
%{_includedir}
%defattr(755,root,root,755)
%{_libdir}
%{_bindir}
