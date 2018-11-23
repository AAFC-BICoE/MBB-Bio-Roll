%define name	    	opt-glibc
%define src_name	glibc
%define release     	1
%define version     	2.24
%define installroot 	/opt/bio/lib/%{src_name}
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

Summary:        The GNU C Library is the standard system C library for all GNU systems, and is an important part of what makes up a GNU system.  
License: 	GPLv2
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{src_name}-%{version}.tar.bz2
Prefix: 	%{_prefix}
Group:          Development/Libraries	
AutoReq:	yes
Url:            https://www.gnu.org/software/libc
Packager: 	Iyad Kandalaft <Iyad.Kandalaft@agr.gc.ca>

BuildRequires: gd-devel libpng-devel zlib-devel
#BuildRequires: nss-devel
BuildRequires: libselinux-devel >= 1.33.4-3
# For the docs
BuildRequires: texinfo

BuildRequires: audit-libs-devel >= 1.1.3, sed >= 3.95, gettext 
#BuildRequires:  libcap-devel, gettext
BuildRequires: /bin/ps, /bin/kill, /bin/awk
#BuildRequires: systemtap-sdt-devel
BuildRequires: gcc >= 4.1.0-0.17
BuildRequires: binutils >= 2.19.51.0.10
# Not required as we're not building the nscd service
#BuildRequires: systemd

%description
The glibc package contains standard libraries which are used by
multiple programs on the system. In order to save disk space and
memory, as well as to make upgrading easier, common system code is
kept in one place and shared between programs. This particular package
contains the most important sets of shared libraries: the standard C
library and the standard math library. Without these two libraries, a
Linux system will not function.

%prep
%setup -q -n %{src_name}-%{version}

%build
BUILDDIR=%{name}-build
mkdir $BUILDDIR
pushd $BUILDDIR
export LD_RUN_PATH=%{_prefix}/lib:$LD_RUN_PATH
../configure --prefix=%{_prefix}
make -j`nproc` -pipe

%install
mkdir -p %{buildroot}%{_prefix}
make install DESTDIR=%{buildroot} -C %{name}-build

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc COPYING*
%{_includedir}
%{_datadir}
%defattr(755,root,root,755)
%{_libdir}
%{_libexecdir}
%{_bindir}
%{_sbindir}
