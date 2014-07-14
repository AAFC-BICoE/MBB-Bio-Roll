# This is a  spec file for The Hoard Memory Allocator

### define _topdir	 	/home/rpmbuild/rpms/hoard
%define name		hoard
%define release		1
%define version 	3.8
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary:	hoard is The Hoard memory allocator
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
URL:            http://www.hoard.org/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPL-2|http://www.hoard.org	
AutoReq:	yes

%description
The Hoard memory allocator is a fast, scalable, and memory-efficient memory
allocator for Linux, Solaris, Mac OS X, and Windows. Hoard is a drop-in
replacement for malloc that can dramatically improve application performance,
especially for multithreaded programs running on multiprocessors and multicore
CPUs.

%prep
%setup -q

%build
cd src
make linux-gcc-x86-64

%install
mkdir -p    %{buildroot}%{installroot}
cp src/libhoard.so %{buildroot}%{installroot}

%files
%defattr(755,root,root)
%{installroot}
