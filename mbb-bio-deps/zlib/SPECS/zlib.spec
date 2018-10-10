%define name		opt-zlib
%define src_name	zlib
%define release		1
%define version 	1.2.11
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/lib/%{src_name}

Summary: 	The compression and decompression library
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	MIT
Source: 	%{src_name}-%{version}.tar.gz
Prefix: 	/opt/bio/lib/%{src_name}
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
./configure --prefix=%{installroot}
make --jobs=`nproc`

%check
make test

%install
make install DESTDIR=%{buildroot}

%files
%doc README ChangeLog FAQ
%{prefix}/lib/libz.so.*

%files devel
%doc README doc/algorithm.txt test/example.c
%{prefix}/include/zlib.h
%{prefix}/include/zconf.h
%{prefix}/lib/libz.so
%{prefix}/lib/pkgconfig/zlib.pc
%{prefix}/share/man/man3/zlib.3*

%files static
%doc README
%{prefix}/lib/libz.a

