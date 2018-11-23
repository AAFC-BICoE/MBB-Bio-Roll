%define name		opt-sparsehash
%define src_name	sparsehash
%define release		1
%define version 	2.0.2
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/lib/%{src_name}
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

BuildRoot:		%{buildroot}
Summary: 		An extremely memory-efficient hash_map implementation
License: 		Open Source
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz
Prefix: 		/opt/bio/lib
Group: 			Development/Libraries
URL:			sdaf
AutoReq:		yes

%description
An extremely memory-efficient hash_map implementation. 2 bits/entry overhead! The SparseHash library contains several hash-map implementations, including implementations that optimize for space or speed.
These hashtable implementations are similar in API to SGI's hash_map class and the tr1 unordered_map class, but with different performance characteristics. It's easy to replace hash_map or unordered_map by sparse_hash_map or dense_hash_map in C++ code.
They also contain code to serialize and unserialize from disk. 

%prep
%setup -q -n %{src_name}-%{version}

%build
#./configure --prefix=%{Prefix}/gdal
./configure --prefix=%{_prefix}
make -j`nproc`

%install
make install DESTDIR=%{buildroot} 
mv %{buildroot}%{_prefix}/share/doc/%{src_name}-%{version} %{buildroot}%{_docdir}/%{name}-%{version}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%doc NEWS
%{_includedir}
%defattr(755,root,root,755)
%{_libdir}
