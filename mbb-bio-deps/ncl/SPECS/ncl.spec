### define _topdir	 	/home/rpmbuild/rpms/ncl
%define debug_package	%{nil}
%define name		opt-ncl
%define src_name	ncl
%define release		1
%define version 	2.1.18
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/lib/%{src_name}

BuildRoot:		%{buildroot}
Summary: 		NEXUS Class Library (NCL)
License: 		GPL2
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz
#Patch:			%{name}.%{version}.patch
Prefix: 		%{installroot}
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
./configure --prefix=%{installroot}
make -pipe --jobs=`nproc` prefix=%{installroot}

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
#make install DESTDIR=$RPM_BUILD_ROOT
#make install prefix=%{installroot}
make install prefix=$RPM_BUILD_ROOT%{installroot}
strip $RPM_BUILD_ROOT%{installroot}/bin/*


%files
%defattr(644,root,root,755)
%{installroot}/include
%{installroot}/lib
%defattr(755,root,root,755)
%{installroot}/bin
