%define name		opt-R
%define srcname		R
%define version		3.5.1
%define release		2
%define installroot     /opt/R/
%define _prefix		%{installroot}


Name:			%{name}
Version:		%{version} 
Release:		%{release} 
Summary:		A language for data analysis and graphics
URL:			http://www.r-project.org
Source0:		%{srcname}-%{version}.tar.gz 
License:		GPLv2+
Packager:		Iyad Kandalaft <Iyad.Kandalaft@agr.gc.ca>
Group:			Applications/Engineering
BuildRoot:		%{_topdir}/%{name}-%{version}-root

# Necessary to support HTTPS and FTPS URLs
Requires: libcurl >= 7.28.0
BuildRequires: libcurl-devel >= 7.28.0

Requires: zlib >= 1.2.5, bzip2 >= 1.0.6, xz >= 5.0.3

BuildRequires: gcc-gfortran
BuildRequires: gcc-c++, texinfo-tex 
BuildRequires: gcc-objc, pango-devel
BuildRequires: libpng-devel, libjpeg-devel, readline-devel
BuildRequires: tcl-devel, tk-devel, ncurses-devel
BuildRequires: blas >= 3.0, pcre-devel, 
BuildRequires: lapack-devel
BuildRequires: libSM-devel, libX11-devel, libICE-devel, libXt-devel
BuildRequires: zlib-devel, bzip2-devel, xz-devel
BuildRequires: libXmu-devel, cairo-devel, libtiff-devel

%ifarch x86_64
%define java_arch amd64
%else
%define java_arch %{_arch}
%endif

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

%package -n opt-R-core
Summary: The minimal R components necessary for a functional runtime
Group: Applications/Engineering
Requires: xdg-utils, cups
Requires: perl, sed, gawk, tetex-latex, less, vim-minimal

%description -n opt-R-core
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

%package -n opt-R-devel
Summary: Files for development of R packages
Group: Applications/Engineering
Requires: opt-R-core = %{version}-%{release}
%description -n opt-R-devel
Install R-devel if you are going to develop or compile R packages.

%package -n opt-libRmath
Summary: Standalone math library from the R project
Group: Development/Libraries
%description -n opt-libRmath
A standalone library of mathematical and statistical functions derived
from the R project.  This packages provides the shared libRmath library.

%package -n opt-libRmath-devel
Summary: Standalone math library from the R project
Group: Development/Libraries
Requires: opt-libRmath = %{version}-%{release}
%description -n opt-libRmath-devel
A standalone library of mathematical and statistical functions derived
from the R project.  This packages provides the static libRmath library
and header files.


%prep
%setup -q -n %{srcname}-%{version}

%build 
# Ensures libcurl-devel components are on the path and part of RUNPATHT
#export PATH=$(dirname $(rpm -ql opt-libcurl-devel | grep bin/curl-config)):$PATH 
#export C_INCLUDE_PATH=$(dirname $(dirname $(rpm -ql opt-libcurl-devel | grep curlbuild.h))):$C_INCLUDE_PATH
#export LD_RUN_PATH=$(dirname $(rpm -ql opt-libcurl | grep "libcurl.so.4.3.0")):$LD_RUN_PATH

#export C_INCLUDE_PATH=$(dirname $(rpm -ql opt-zlib-devel | grep 'zlib.h')):$C_INCLUDE_PATH
#export LD_RUN_PATH=$(dirname $(rpm -ql opt-zlib | grep "libz.so.1.2.11")):$LD_RUN_PATH

#export C_INCLUDE_PATH=$(dirname $(rpm -ql opt-bzip2-devel | grep 'bzlib.h')):$C_INCLUDE_PATH
#export LD_RUN_PATH=$(dirname $(rpm -ql opt-bzip2-libs | grep "libbz2.so.1.0.6")):$LD_RUN_PATH

#export C_INCLUDE_PATH=$(dirname $(rpm -ql opt-xz-devel | grep 'lzma.h')):$C_INCLUDE_PATH
#export C_INCLUDE_PATH=$(dirname $(rpm -ql opt-xz-devel | grep 'lzma/' | head -1)):$C_INCLUDE_PATH
#export LD_RUN_PATH=$(dirname $(rpm -ql opt-xz-libs | grep "liblzma.so.5.2.4")):$LD_RUN_PATH

./configure \
    --prefix=%{_prefix} -q \
    --with-lapack \
    --enable-static \
    --enable-R-shlib \
    --disable-nls

make -j`nproc`
# make docs
make -j`nproc` pdf
make -j`nproc` info

%install

mkdir -p %{buildroot}%{_prefix}
make DESTDIR=%{buildroot} install-strip install install-libR install-info install-pdf
#Install libRmath files
mkdir -p %{buildroot}%{_prefix}/lib64/pkgconfig
(cd src/nmath/standalone; make; make DESTDIR=%{buildroot} install)

%files -n opt-R-core
%defattr(755, root, root, 755)
%dir %{_prefix}
%{_bindir}
%{_libdir}/R/bin
%defattr(-, root, root, -)
%{_libdir}/libR.so
%{_libdir}/R/COPYING
%{_libdir}/R/doc
%{_libdir}/R/etc
%{_libdir}/R/lib
%{_libdir}/R/library
%{_libdir}/R/modules
%{_libdir}/R/share
%{installroot}/share
%files -n opt-R-devel
%{_libdir}/R/include
%{_libdir}/pkgconfig/libR.pc
%files -n opt-libRmath
%{_libdir}/libRmath.so
%{_libdir}/pkgconfig/libRmath.pc
%files -n opt-libRmath-devel
%{_includedir}/Rmath.h
%{_libdir}/libRmath.a
