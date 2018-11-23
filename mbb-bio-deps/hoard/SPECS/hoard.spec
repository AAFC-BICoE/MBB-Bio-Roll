%define name		opt-hoard
%define src_name	hoard
%define release		1
%define version 	3.12
%define installroot	/opt/bio/lib/%{src_name}
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

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
mkdir -p  %{buildroot}%{_libdir}
cd src
# PREFIX must be set to _libdir because Makefile is custom
make Linux-gcc-x86_64-install PREFIX=%{buildroot}%{_libdir}
cp -r include %{buildroot}%{_includedir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc COPYING
%doc AUTHORS
%doc README.md
%{_includedir}
%defattr(755,root,root,755)
%{_libdir}
