### define _topdir	 	/home/rpmbuild/rpms/beagle-lib
%define name		opt-lmdb
%define	src_name	lmdb
%define release		1
%define version 	0.9.22
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/lib/%{src_name}
%define	_prefix		%{installroot}


BuildRoot:		%{buildroot}
Summary: 		MLightning Memory-Mapped Database Manager
License: 		OLDAP-2.8
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source:         	LMDB_%{version}.tar.gz
Prefix: 		%{installroot}
Group:          	Productivity/Databases/Tools
AutoReq:		yes
Url:			http://symas.com/mdb/
Packager:		Iyad Kandalaft <iyad.kandalaft@canada.ca>

BuildRequires:		perl-Exporter

%description
LMDB is a Btree-based database management library with an API similar
to BerkeleyDB. The library is thread-aware and supports concurrent
read/write access from multiple processes and threads. The DB
structure is multi-versioned, and data pages use a copy-on-write
strategy, which also provides resistance to corruption and eliminates
the need for any recovery procedures. The database is exposed in a
memory map, requiring no page cache layer of its own.

%prep
%setup -qn %{src_name}-LMDB_%{version}/libraries/liblmdb

%build
make -j `nproc` # %{?_smp_mflags} V=1 SOVERSION=%{version} CFLAGS="%{optflags}"

%install
make install DESTDIR="%{buildroot}" prefix=%{installroot}

%files
%defattr(-,root,root)
%doc CHANGES
%doc COPYRIGHT
%doc LICENSE
%dir %{installroot}
%{_bindir}
%doc %{_mandir}
%_includedir
%{installroot}/lib
