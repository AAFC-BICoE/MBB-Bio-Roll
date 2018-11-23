%define name		opt-libtool
%define release		1
%define version 	2.4.6
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/gnu-tools
%define _prefix		%{installroot}
%define	_libdir		%{_prefix}/lib

BuildRoot:	%{buildroot}
Summary: 	The GNU Portable Library Tool
License:    	GPLv2+ and LGPLv2+ and GFDL
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	libtool-%{version}.tar.gz
Prefix: 	%{_prefix}
Group: 		Development/Tools
URL:		http://www.gnu.org/software/m4
AutoReqProv:	yes
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>

Provides:	libtool

BuildRequires: autoconf, automake, texinfo
Requires: opt-autoconf, opt-automake, sed, tar

BuildRequires: libstdc++-devel, gcc-gfortran
Requires: gcc

%description
GNU Libtool is a set of shell scripts which automatically configure UNIX and
UNIX-like systems to generically build shared libraries. Libtool provides a
consistent, portable interface which simplifies the process of using shared
libraries.

If you are developing programs which will use shared libraries, but do not use
the rest of the GNU Autotools (such as GNU Autoconf and GNU Automake), you
should install the libtool package.

The libtool package also includes all files needed to integrate the GNU
Portable Library Tool (libtool) and the GNU Libtool Dynamic Module Loader
(ltdl) into a package built using the GNU Autotools (including GNU Autoconf
and GNU Automake).

%package ltdl
Summary:  Runtime libraries for GNU Libtool Dynamic Module Loader
Group:    System Environment/Libraries
Provides: %{name}-libs = %{version}-%{release}
License:  LGPLv2+
Provides: libtool-ltdl

%description ltdl
The libtool-ltdl package contains the GNU Libtool Dynamic Module Loader, a
library that provides a consistent, portable interface which simplifies the
process of using dynamic modules.

These runtime libraries are needed by programs that link directly to the
system-installed ltdl libraries; they are not needed by software built using
the rest of the GNU Autotools (including GNU Autoconf and GNU Automake).


%package ltdl-devel
Summary: Tools needed for development using the GNU Libtool Dynamic Module Loader
Group:    Development/Libraries
Requires: %{name}-ltdl = %{version}-%{release}
License:  LGPLv2+

%description ltdl-devel
Static libraries and header files for development with ltdl.

%prep
%setup -n libtool-%{version} -q

%build
./configure --prefix=%{_prefix}
make -j

%install
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root)
%{_infodir}/libtool.info*
%{_mandir}/man1/libtool.1*
%{_mandir}/man1/libtoolize.1*
%{_bindir}/libtool
%{_bindir}/libtoolize
%{_datadir}/aclocal/*.m4
%exclude %{_datadir}/libtool/libltdl
%{_datadir}/libtool/

%files ltdl
%defattr(-,root,root)
%doc libltdl/COPYING.LIB
%{_libdir}/*

%files ltdl-devel
%defattr(-,root,root)
%doc libltdl/README
%{_datadir}/libtool/libltdl
%{_includedir}/ltdl.h
%{_includedir}/libltdl
