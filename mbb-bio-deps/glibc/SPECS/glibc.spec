%define name	    	opt-glibc
%define srcname		glibc
%define release     	1
%define version     	2.18
%define installroot 	/opt/bio/lib/%{srcname}

Summary:        The GNU C Library is the standard system C library for all GNU systems, and is an important part of what makes up a GNU system.  
License: 	GPLv2
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{srcname}-%{version}.tar.bz2
Prefix: 	/opt/bio/lib
Group:          Development/Libraries	
AutoReq:	yes
Url:            https://www.gnu.org/software/libc
Packager: 	Iyad Kandalaft <Iyad.Kandalaft@agr.gc.ca>

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
%setup -q -n %{srcname}-%{version}

%build
BUILDDIR=%{name}-build
mkdir $BUILDDIR
pushd $BUILDDIR
../configure --prefix=%{installroot}
make -j`nproc`
popd

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install install_root=$RPM_BUILD_ROOT -C %{name}-build

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/lib
