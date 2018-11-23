%define name		opt-eigen
%define	src_name	eigen
%define release		2
%define version 	3.3.5
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/lib/%{src_name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		For linear algebra computations.
License: 		MPL2
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-v%{version}.tar.gz
Prefix: 		%{_prefix}
Group: 			Development/Tools
URL:			http://eigen.tuxfamily.org/index.php?title=Main_Page
AutoReq:		yes

%description
Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.

%prep
%setup -q -n %{src_name}-%{src_name}-b3f3d4950030

%build
mkdir build && cd build
cmake ../ -DCMAKE_INSTALL_PREFIX=%{_prefix} -DINCLUDE_INSTALL_DIR=%{_includedir} -DCMAKE_BUILD_TYPE=Release
make -j`nproc`

%install
cd build
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755) 
%dir %{_prefix}
%doc COPYING.*
%{_includedir}
%{_datadir}
%defattr(755,root,root,755)
