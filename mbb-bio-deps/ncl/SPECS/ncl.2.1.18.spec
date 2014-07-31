### define _topdir	 	/home/rpmbuild/rpms/ncl
%define debug_package %{nil}
%define name		ncl
%define release		cl1
%define version 	2.1.18
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 		NEXUS Class Library (NCL)
License: 		GPL2
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
#Patch:			%{name}.%{version}.patch
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes
Url: http://ncl.sourceforge.net/

%description
The Nexus Class Library (NCL) is a C++ library for interpreting data files
created according to the NEXUS file format used in phylogenetic systematics and
molecular evolution.

%prep
%setup -q

%build
./configure --disable-shared  --prefix=/opt/bio/ncl
make -pipe --jobs=`nproc`  prefix=%{installroot}

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
#make install DESTDIR=$RPM_BUILD_ROOT
#make install prefix=%{installroot}
make install prefix=$RPM_BUILD_ROOT%{installroot}
strip $RPM_BUILD_ROOT%{installroot}/bin/*


%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
