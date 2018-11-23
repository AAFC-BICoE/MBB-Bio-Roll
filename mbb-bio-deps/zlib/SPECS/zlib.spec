%define name		opt-zlib
%define src_name	zlib
%define release		1
%define version 	1.2.11
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define installroot	/opt/bio/lib/%{src_name}
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

Summary: 	The compression and decompression library
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	MIT
Source: 	%{src_name}-%{version}.tar.gz
Prefix: 	%{_prefix}
Group: 		System Environment/Libraries
URL: 		http://www.zlib.net/
AutoReqProv:	yes

%description
Zlib is a general-purpose, patent-free, lossless data compression
library which is used by many different programs.

%package devel
Summary: Header files and libraries for Zlib development
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The zlib-devel package contains the header files and libraries needed
to develop programs that use the zlib compression and decompression
library.

%package static
Summary: Static libraries for zlib development
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
The zlib-static package includes static libraries needed
to develop programs that use the zlib compression and
decompression library.

%prep
%setup -q -n %{src_name}-%{version}

%build
./configure --prefix=%{_prefix}
make --jobs=`nproc`

%check
make test

%install
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%doc README ChangeLog FAQ
%defattr(755,root,root,755)
%{prefix}/lib/libz.so.*

%files devel
%defattr(644,root,root,755)
%doc README doc/algorithm.txt test/example.c
%{_includedir}/zlib.h
%{_includedir}/zconf.h
%{_mandir}/man3/zlib.3*
%{_libdir}/pkgconfig/zlib.pc
%defattr(755,root,root,755)
%{_libdir}/libz.so

%files static
%doc README
%defattr(755,root,root,755)
%{_libdir}/libz.a

