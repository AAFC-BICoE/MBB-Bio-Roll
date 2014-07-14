
%define name		Eigen
### define _topdir	 	/home/rpmbuild/rpms/Eigen 
%define release		2
%define version 	3.1.1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 

BuildRoot:		%{buildroot}
Summary: 		For linear algebra computations.
License: 		MPL2
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		eigen-eigen-43d9075b23ef.tar.gz
Prefix: 		/opt/bio
Group: 			Development/Tools
URL:			http://eigen.tuxfamily.org/index.php?title=Main_Page
AutoReq:		yes

%description
Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.

%prep
%setup -qn eigen-eigen-43d9075b23ef

%build
mkdir build_dir
cd build_dir
cmake .. -DCMAKE_INSTALL_PREFIX=%{installroot}
cmake . -DEIGEN_INCLUDE_INSTALL_DIR=%{installroot}/include


%install
cd build_dir
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755) 
%{installroot}
