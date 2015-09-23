### %define _topdir	        /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/glibc-2.14
%define name	    	glibc-2.14
%define release     	1
%define version     	2.14
%define installroot 	/opt/bio/lib/%{name}

Summary:        The GNU C Library is the standard system C library for all GNU systems, and is an important part of what makes up a GNU system.  
License: 	GPLv2
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	glibc-%{version}.tar.bz2
Prefix: 	/opt/bio/lib
Group:          Development/Libraries	
AutoReq:	yes
Url:            http://ftp.gnu.org/gnu/glibc/glibc-2.14.tar.bz2
Packager: 	Alex MacLean <alex.maclean@agr.gc.ca>

%description
The GNU C Library is the standard system C library for all GNU systems,
and is an important part of what makes up a GNU system.  It provides the
system API for all programs written in C and C-compatible languages such
as C++ and Objective C; the runtime facilities of other programming
languages use the C library to access the underlying operating system.

In GNU/Linux systems, the C library works with the Linux kernel to
implement the operating system behavior seen by user applications.
In GNU/Hurd systems, it works with a microkernel and Hurd servers.

The GNU C Library implements much of the POSIX.1 functionality in the
GNU/Hurd system, using configurations i[34567]86-*-gnu.

%prep
%setup -q -n glibc-2.14

%build
mkdir ../%{name}-build
cd ../%{name}-build
../%{name}/configure --prefix=%{installroot}
make -j24

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cd ../%{name}-build
make install install_root=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/lib
