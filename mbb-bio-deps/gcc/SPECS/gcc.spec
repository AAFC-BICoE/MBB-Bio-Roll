%define name		opt-gcc
%define src_name	gcc
%define release		1
%define version 	8.2.0
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/gnu-tools
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	A GNU tool for automatically configuring source code
License:    	GPLv2+ and GFDL
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{src_name}-%{version}.tar.xz
Prefix: 	%{_prefix}
Group: 		Development/Tools
URL:		http://www.gnu.org/software/autoconf/autoconf.html	
AutoReq:	yes
AutoProv:	yes
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>

BuildRequires:	gmp-devel >= 4.2
BuildRequires:	mpfr-devel >= 2.4.0
BuildRequires:	libmpc-devel >= 0.8.0

%description
The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Java, Ada, and Go, as well as libraries for these languages (libstdc++, libgcj,...). GCC was originally written as the compiler for the GNU operating system. The GNU system was developed to be 100% free software, free in the sense that it respects the user s freedom.

%prep
%setup -q -n %{src_name}-%{version}

%build
unset LIBRARY_PATH CPATH C_INCLUDE_PATH PKG_CONFIG_PATH CPLUS_INCLUDE_PATH INCLUDE
mkdir build
cd build
../configure  --prefix=%{_prefix} --enable-languages=ada,c,c++,fortran,go,objc,obj-c++,brig,jit,lto --enable-threads=posix --enable-static --enable-shared --enable-bootstrap --enable-shared-libgcc --enable-host-shared --disable-multilib --with-system-zlib --enable-plugin --enable-initfini-array --disable-libgcj --enable-gnu-indirect-function --with-tune=generic
export LD_RUN_PATH=%{_libdir}
make -j`nproc`

%install
unset LIBRARY_PATH CPATH C_INCLUDE_PATH PKG_CONFIG_PATH CPLUS_INCLUDE_PATH INCLUDE
cd build
make install -j`nproc` DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc COPYING*
%doc MAINTAINERS
%{_includedir}/*
%{_infodir}/*.info
%{_datadir}/%{src_name}-%{version}
%{_mandir}/man1/*
%{_mandir}/man7/*
%defattr(755,root,root,755)
%{_prefix}/lib/libgccjit.so*
%{_prefix}/lib/gcc/
%{_libdir}/*
%{_libexecdir}/gcc
%{_bindir}/*

