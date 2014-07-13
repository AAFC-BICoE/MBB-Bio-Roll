# This is a  spec file for boost
# Note: the following rpm packages are supposed to be installed before
# installing boost:
# bzip2-1.0.5-7.el6_0.x86_64.rpm 
# bzip2-devel-1.0.5-7.el6_0.x86_64.rpm
# bzip2-libs-1.0.5-7.el6_0.x86_64.rpm

### define _topdir	 	/home/rpmbuild/rpms/boost
%define name		boost
%define release		1
%define version 	1_47_0
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	boost is C++ library
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}_%{version}.tar.gz
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        Unknown
AutoReq:	yes

%description
boost is a C++ library.


%prep
%setup -q -n %{name}_%{version}

%build
mkdir -p %{buildroot}%{installroot}
./bootstrap.sh --prefix=%{buildroot}%{installroot}
./bjam --prefix=%{buildroot}%{installroot} 

%install
./bjam install --prefix=%{buildroot}%{installroot}

%files
%defattr(-,root,root)
%{installroot}
