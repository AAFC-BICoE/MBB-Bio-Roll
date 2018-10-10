# This is a  spec file for The Hoard Memory Allocator

### define _topdir	 	/home/rpmbuild/rpms/hoard
%define name		opt-hoard
%define src_name	hoard
%define release		1
%define version 	3.12
%define installroot	/opt/bio/lib/%{src_name}

BuildRoot:	%{buildroot}
Summary:	hoard is The Hoard memory allocator
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{src_name}-%{version}.tar.gz
Source1: 	heap-layers.tar.gz
URL:            http://www.hoard.org/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPLv2	
AutoReq:	yes

%description
The Hoard memory allocator is a fast, scalable, and memory-efficient memory
allocator for Linux, Solaris, Mac OS X, and Windows. Hoard is a drop-in
replacement for malloc that can dramatically improve application performance,
especially for multithreaded programs running on multiprocessors and multicore
CPUs.

%prep
%setup -q -a 0 -n Hoard-%{version}
%setup -q -T -D -a 1 -n Hoard-%{version}
mv Heap-Layers/ src/

%build
cd src
make -j 4 Linux-gcc-x86_64

%install
mkdir -p    %{buildroot}%{installroot}
cp src/libhoard.so %{buildroot}%{installroot}

%files
%defattr(755,root,root)
%{installroot}
