%define name		opt-gcc
%define src_name	gcc
%define release		1
%define version 	8.2.0
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/gnu-tools

BuildRoot:	%{buildroot}
Summary: 	A GNU tool for automatically configuring source code
License:    	GPLv2+ and GFDL
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{src_name}-%{version}.tar.xz
Prefix: 	%{installroot}
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
./configure --prefix=/opt/gnu-tools/ --disable-multilib --enable-static
make prefix=%{installroot} -j `nproc`

%install
unset LIBRARY_PATH CPATH C_INCLUDE_PATH PKG_CONFIG_PATH CPLUS_INCLUDE_PATH INCLUDE
make install -j 12 prefix=%{buildroot}%{installroot}

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,) 
%{installroot}/bin/*
