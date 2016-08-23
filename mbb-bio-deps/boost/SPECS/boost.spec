# This is a  spec file for boost
# Note: the following rpm packages are supposed to be installed before
# installing boost:
# bzip2-1.0.5-7.el6_0.x86_64.rpm 
# bzip2-devel-1.0.5-7.el6_0.x86_64.rpm
# bzip2-libs-1.0.5-7.el6_0.x86_64.rpm

### define _topdir	 	/home/rpmbuild/rpms/boost
%define name		opt-boost
%define release		3
%define version 	1.47.0
%define installroot 	/opt/bio/lib/boost
%define _libdir		%{installroot}/lib
%define _includedir	%{installroot}/include
%define sonamever	1.47.0
%define sourcedir	%(echo "boost_%{version}" | perl -pe 's/\\./_/g')

BuildRoot:	%{buildroot}
Summary: 	boost is C++ library
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{sourcedir}.tar.bz2
Prefix: 	%{installroot}
Group: 		Development/Tools
License:        Boost Software License - Version 1.0
AutoReq:	yes
Provides:	boost = %{version}-%{release}
URL:		www.boost.org/

%description
Boost provides free peer-reviewed portable C++ source libraries.


%package chrono 
Summary: Runtime component of boost date-time library
Group: System Environment/Libraries
Provides: boost-chrono = %{version}-%{release}

%description chrono

Boost dynamic library based on time 


%package random
Summary: Runtime component of boost date-time library
Group: System Environment/Libraries
Provides: boost-random = %{version}-%{release}


%description random

Boost dynamic library based on mathematical randomness and statistical analysis 


%package date-time
Summary: Runtime component of boost date-time library
Group: System Environment/Libraries
Provides: boost-date-time = %{version}-%{release}

%description date-time

Runtime support for Boost Date Time, set of date-time libraries based
on generic programming concepts.

%package filesystem
Summary: Runtime component of boost filesystem library
Group: System Environment/Libraries
Provides: boost-filesystem = %{version}-%{release}

%description filesystem

Runtime support for the Boost Filesystem Library, which provides
portable facilities to query and manipulate paths, files, and
directories.

%package graph
Summary: Runtime component of boost graph library
Group: System Environment/Libraries
Provides: boost-graph = %{version}-%{release}

%description graph

Runtime support for the BGL graph library.  BGL interface and graph
components are generic, in the same sense as the the Standard Template
Library (STL).

%package iostreams
Summary: Runtime component of boost iostreams library
Group: System Environment/Libraries
Provides: boost-iostreams = %{version}-%{release}

%description iostreams

Runtime support for Boost.IOStreams, a framework for defining streams,
stream buffers and i/o filters.

%package math
Summary: Stub that used to contain boost math library
Group: System Environment/Libraries
Provides: boost-math = %{version}-%{release}

%description math

This package is a stub that used to contain runtime component of boost
math library.  Now that boost math library is header-only, this
package is empty.  It's kept around only so that during yum-assisted
update, old libraries from boost-math package aren't left around.

%package program-options
Summary:  Runtime component of boost program_options library
Group: System Environment/Libraries
Provides: boost-program-options = %{version}-%{release}

%description program-options

Runtime support of boost program options library, which allows program
developers to obtain (name, value) pairs from the user, via
conventional methods such as command line and configuration file.

%package python
Summary: Runtime component of boost python library
Group: System Environment/Libraries
Provides: boost-python = %{version}-%{release}

%description python

The Boost Python Library is a framework for interfacing Python and
C++. It allows you to quickly and seamlessly expose C++ classes
functions and objects to Python, and vice versa, using no special
tools -- just your C++ compiler.  This package contains runtime
support for Boost Python Library.

%package regex
Summary: Runtime component of boost regular expression library
Group: System Environment/Libraries
Provides: boost-regex = %{version}-%{release}

%description regex

Runtime support for boost regular expression library.

%package serialization
Summary: Runtime component of boost serialization library
Group: System Environment/Libraries
Provides: boost-serialization = %{version}-%{release}

%description serialization

Runtime support for serialization for persistence and marshaling.

%package signals
Summary: Runtime component of boost signals and slots library
Group: System Environment/Libraries
Provides: boost-signals = %{version}-%{release}

%description signals

Runtime support for managed signals & slots callback implementation.

%package system
Summary: Runtime component of boost system support library
Group: System Environment/Libraries
Provides: boost-system = %{version}-%{release}

%description system

Runtime component of Boost operating system support library, including
the diagnostics support that will be part of the C++0x standard
library.

%package test
Summary: Runtime component of boost test library
Group: System Environment/Libraries
Provides: boost-test = %{version}-%{release}


%description test

Runtime support for simple program testing, full unit testing, and for
program execution monitoring.

%package thread
Summary: Runtime component of boost thread library
Group: System Environment/Libraries
Provides: boost-thread = %{version}-%{release}

%description thread

Runtime component Boost.Thread library, which provides classes and
functions for managing multiple threads of execution, and for
synchronizing data between the threads or providing separate copies of
data specific to individual threads.

%package wave
Summary: Runtime component of boost C99/C++ preprocessing library
Group: System Environment/Libraries
Provides: boost-wave = %{version}-%{release}

%description wave

Runtime support for the Boost.Wave library, a Standards conformant,
and highly configurable implementation of the mandated C99/C++
preprocessor functionality.

%package devel
Summary: The Boost C++ headers and shared development libraries
Group: Development/Libraries
Requires: boost = %{version}-%{release}
Provides: boost-devel = %{version}-%{release}
Provides: boost-python-devel = %{version}-%{release}

%description devel
Headers and shared object symlinks for the Boost C++ libraries.


%package static
Summary: The Boost C++ static development libraries
Group: Development/Libraries
Requires: boost-devel = %{version}-%{release}
Obsoletes: boost-devel-static < 1.34.1-14
Provides: boost-devel-static = %{version}-%{release}

%description static
Static Boost C++ libraries.

%package doc
Summary: HTML documentation for the Boost C++ libraries
Group: Documentation
Provides: boost-python-docs = %{version}-%{release}
Provides: boost-docs = %{version}-%{release}

%description doc
This package contains the documentation in the HTML format of the Boost C++
libraries. The documentation provides the same content as that on the Boost
web page (http://www.boost.org/doc/libs/1_40_0).

%prep
%setup -q -n %{sourcedir}

%build
mkdir -p %{buildroot}%{installroot}
./bootstrap.sh --prefix=%{buildroot}%{installroot}
./bjam -j $(nproc) --prefix=%{buildroot}%{installroot} 

%install
./bjam install --prefix=%{buildroot}%{installroot}

#%files
#%defattr(-,root,root)

#%{installroot}
%files

%dir %attr(0755, root, root) %{_libdir}
%dir %attr(0755, root, root) %{_includedir}
%dir %attr(0755, root, root) %{_includedir}/boost 

%files chrono
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_chrono*.so.%{sonamever}


%files random 
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_random*.so.%{sonamever}



%files date-time
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_date_time*.so.%{sonamever}

%files filesystem
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_filesystem*.so.%{sonamever}

%files graph
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_graph.so.%{sonamever}
#%{_libdir}/libboost_graph-mt.so.%{sonamever}

%files iostreams
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_iostreams*.so.%{sonamever}

%files math
%defattr(755, root, root, 755)
%{_libdir}/libboost_math*.so.%{sonamever}

%files test
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_prg_exec_monitor*.so.%{sonamever}
%{_libdir}/libboost_unit_test_framework*.so.%{sonamever}

%files program-options
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_program_options*.so.%{sonamever}

%files python
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_python*.so.%{sonamever}

%files regex
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_regex*.so.%{sonamever}

%files serialization
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_serialization*.so.%{sonamever}
%{_libdir}/libboost_wserialization*.so.%{sonamever}

%files signals
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_signals*.so.%{sonamever}

%files system
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_system*.so.%{sonamever}

%files thread
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_thread*.so.%{sonamever}

%files wave
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_wave*.so.%{sonamever}

%files doc
#%defattr(-, root, root, -)
#%doc %{boost_docdir}/*
#%doc %{installroot}/doc/* 

%files devel
%defattr(755, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/libboost_*.so
%{_includedir}/boost
#%{_datadir}/%{name}-%{version}
#%{_libdir}/boost/Boost*.cmake

%files static
%defattr(644, root, root, 755)
#%doc LICENSE_1_0.txt
%{_libdir}/*.a

