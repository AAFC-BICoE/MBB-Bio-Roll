%ifarch x86_64
%define java_arch amd64
%else
%define java_arch %{_arch}
%endif


#### TODO CHANGE THE TOPDIR
### define _topdir         /home/rpmbuild/rpms/R3
%define name		R3
%define version		3.1.3
%define release		1
%define installroot     /opt/R/%{name}/%{version}

Name: %{name} 
Version: %{version} 
Release: %{release} 
Summary: A language for data analysis and graphics
URL: http://www.r-project.org
Source0: R-%{version}.tar.gz 
License: GPLv2+
Packager:	Glen Newton <Glen.Newton@agr.gc.ca>
Group: Applications/Engineering
BuildRoot: %{_topdir}/%{name}-%{version}-root
BuildRequires: gcc-gfortran
BuildRequires: gcc-c++, texinfo-tex 
BuildRequires: libpng-devel, libjpeg-devel, readline-devel
BuildRequires: tcl-devel, tk-devel, ncurses-devel
BuildRequires: blas >= 3.0, pcre-devel, zlib-devel
BuildRequires: lapack-devel
BuildRequires: libSM-devel, libX11-devel, libICE-devel, libXt-devel
BuildRequires: bzip2-devel, libXmu-devel, cairo-devel, libtiff-devel
BuildRequires: gcc-objc, pango-devel

%description
This is a metapackage that provides both core R userspace and 
all R development components.

R is a language and environment for statistical computing and graphics. 
R is similar to the award-winning S system, which was developed at 
Bell Laboratories by John Chambers et al. It provides a wide 
variety of statistical and graphical techniques (linear and
nonlinear modelling, statistical tests, time series analysis,
classification, clustering, ...).

R is designed as a true computer language with control-flow
constructions for iteration and alternation, and it allows users to
add additional functionality by defining new functions. For
computationally intensive tasks, C, C++ and Fortran code can be linked
and called at run time.

%package R-core
Summary: The minimal R components necessary for a functional runtime
Group: Applications/Engineering
Requires: xdg-utils, cups
Requires: perl, sed, gawk, tetex-latex, less, vim-minimal


%description R-core
A language and environment for statistical computing and graphics.
R is similar to the award-winning S system, which was developed at
Bell Laboratories by John Chambers et al. It provides a wide
variety of statistical and graphical techniques (linear and
nonlinear modelling, statistical tests, time series analysis,
classification, clustering, ...).

R is designed as a true computer language with control-flow
constructions for iteration and alternation, and it allows users to
add additional functionality by defining new functions. For
computationally intensive tasks, C, C++ and Fortran code can be linked
and called at run time.

%package -n R-devel
Summary: Files for development of R packages
Group: Applications/Engineering
%description -n R-devel
Install R-devel if you are going to develop or compile R packages.

%package -n libRmath
Summary: Standalone math library from the R project
Group: Development/Libraries
%description -n libRmath
A standalone library of mathematical and statistical functions derived
from the R project.  This packages provides the shared libRmath library.

%package -n libRmath-devel
Summary: Standalone math library from the R project
Group: Development/Libraries
%description -n libRmath-devel
A standalone library of mathematical and statistical functions derived
from the R project.  This packages provides the static libRmath library
and header files.


%prep
%setup -q -n R-%{version}


%build 
./configure \
    --prefix=%{installroot} \
    --with-system-zlib --with-system-bzlib --with-system-pcre \
    --with-lapack \
    --enable-static \
    --enable-R-shlib
make
# make docs
make pdf
make info



%install

mkdir -p %{buildroot}%{installroot}
make DESTDIR=%{buildroot} install-strip install install-libR install-info install-pdf
#Install libRmath files
mkdir -p %{buildroot}%{installroot}/lib64/pkgconfig
(cd src/nmath/standalone; make; make DESTDIR=%{buildroot} install)


%files  R-core
%defattr(644, root, root, 755)
%{installroot}
%defattr(755, root, root, 755)
%{installroot}/bin/
%{installroot}/lib64/R/bin
%files -n R-devel
%defattr(755, root, root, 755)
%files -n libRmath
%{installroot}/include/Rmath.h
%{installroot}/lib64/libRmath.a
%{installroot}/lib64/libRmath.so
%{installroot}/lib64/pkgconfig/libRmath.pc
%defattr(755, root, root, 755)
%files -n libRmath-devel
%defattr(644, root, root, 755)


