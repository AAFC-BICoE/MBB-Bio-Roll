%define name		opt-boost
%define release		1
%define version 	1.68.0
%define installroot 	/opt/bio/lib/boost
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib
%define sonamever	1.68.0
%define sourcedir	%(echo "boost_%{version}" | perl -pe 's/\\./_/g')

BuildRoot:	%{buildroot}
Summary:	boost is C++ library
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		%{sourcedir}.tar.bz2
Prefix:		%{installroot}
Group:		Development/Tools
License:	Boost Software License - Version 1.0
AutoReq:	yes
Requires:	 opt-boost-atomic = %{sonamever}
Requires:	 opt-boost-chrono  = %{sonamever}
Requires:	 opt-boost-container = %{sonamever}
Requires:	 opt-boost-context = %{sonamever}
Requires:	 opt-boost-contract = %{sonamever}
Requires:	 opt-boost-coroutine = %{sonamever}
Requires:	 opt-boost-date-time = %{sonamever}
Requires:	 opt-boost-filesystem = %{sonamever}
Requires:	 opt-boost-graph = %{sonamever}
Requires:	 opt-boost-iostreams = %{sonamever}
Requires:	 opt-boost-locale = %{sonamever}
Requires:	 opt-boost-log = %{sonamever}
Requires:	 opt-boost-math = %{sonamever}
Requires:	 opt-boost-numpy = %{sonamever}
Requires:	 opt-boost-program-options = %{sonamever}
Requires:	 opt-boost-python = %{sonamever}
Requires:	 opt-boost-random = %{sonamever}
Requires:	 opt-boost-regex = %{sonamever}
Requires:	 opt-boost-serialization = %{sonamever}
Requires:	 opt-boost-signals = %{sonamever}
Requires:	 opt-boost-system = %{sonamever}
Requires:	 opt-boost-stacktrace = %{sonamever}
Requires:	 opt-boost-test = %{sonamever}
Requires:	 opt-boost-thread = %{sonamever}
Requires:	 opt-boost-timer = %{sonamever}
Requires:	 opt-boost-type_erasure = %{sonamever}
Requires:	 opt-boost-wave = %{sonamever}
Requires:	 opt-boost-devel = %{sonamever}
Requires:	 opt-boost-static = %{sonamever}
Requires:	 opt-boost-doc = %{sonamever}
Provides:	boost = %{version}-%{release}
URL:		http://www.boost.org/

%description
Boost provides free peer-reviewed portable C++ source libraries.

%package atomic
Summary: Run-Time component of boost atomic library
Group: System Environment/Libraries
Provides: boost-atomic = %{version}-%{release}

%description atomic

Run-Time support for Boost.Atomic, a library that provides atomic data types
and operations on these data types, as well as memory ordering constraints
required for coordinating multiple threads through atomic variables.

%package chrono 
Summary: Runtime component of boost date-time library
Group: System Environment/Libraries
Provides: boost-chrono = %{version}-%{release}

%description chrono

Boost dynamic library based on time 

%package container
Summary: Runtime component of boost container library
Group: System Environment/Libraries
Provides: boost-container = %{version}-%{release}

%description container

Boost.Container library implements several well-known containers,
including STL containers. The aim of the library is to offer advanced
features not present in standard containers or to offer the latest
standard draft features for compilers that comply with C++03.

%package context
Summary: Run-time component of boost context switching library
Group: System Environment/Libraries
Provides: boost-context = %{version}-%{release}

%description context

Run-time support for Boost.Context, a foundational library that
provides a sort of cooperative multitasking on a single thread.

%package contract
Summary: Boost.Contract runtime library 
Group: System Environment/Libraries
Provides: boost-contract = %{version}-%{release}

%description contract

Runtime support for Boost.Contract, a library that implements
Design by Contract or DbC or contract programming.

%package coroutine
Summary: Boost.Coroutine runtime library 
Group: System Environment/Libraries
Provides: boost-coroutine = %{version}-%{release}

%description coroutine
This package contains the Boost Coroutine runtime library.



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

%package locale
Summary: Runtime component of boost locale library
Group: System Environment/Libraries
Provides: boost-locale = %{version}-%{release}

%description locale

Runtime support for Boost.Locale.

%package log
Summary: Runtime component of boost log library
Group: System Environment/Libraries
Provides: boost-log = %{version}-%{release}

%description log

Runtime support for Boost.Log.

%package math
Summary: Stub that used to contain boost math library
Group: System Environment/Libraries
Provides: boost-math = %{version}-%{release}

%description math

This package is a stub that used to contain runtime component of boost
math library.  Now that boost math library is header-only, this
package is empty.  It's kept around only so that during yum-assisted
update, old libraries from boost-math package aren't left around.

%package numpy
Summary: Stub that used to contain boost numpy library
Group: System Environment/Libraries
Provides: boost-numpy = %{version}-%{release}


%description numpy

Runtime support for Boost.numpy.

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

%package random
Summary: Runtime component of boost date-time library
Group: System Environment/Libraries
Provides: boost-random = %{version}-%{release}

%description random

Boost dynamic library based on mathematical randomness and statistical analysis 

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

%package stacktrace
Summary: Runtime component of boost stacktrace support library
Group: System Environment/Libraries
Provides: boost-stacktrace = %{version}-%{release}

%description stacktrace

This package contains development headers for Boost.Stacktrace library.
Boost.Stacktrace is a simple C++03 library that provide information
about call sequence in a human-readable form.

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

%package timer
Summary: Runtime component of boost timer library
Group: System Environment/Libraries
Provides: boost-timer = %{version}-%{release}

%description timer

This package contains Boost.Timer runtime library.

%package type_erasure
Summary: Runtime component of boost type_erasure library
Group: System Environment/Libraries
Provides: boost-type_erasure = %{version}-%{release}

%description type_erasure

This package contains Boost.TypeErasure runtime library.

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
Provides: opt-boost-devel = %{version}-%{release}
Provides: opt-boost-python-devel = %{version}-%{release}

%description devel
Headers and shared object symlinks for the Boost C++ libraries.


%package static
Summary: The Boost C++ static development libraries
Group: Development/Libraries
Requires: boost-devel = %{version}-%{release}
Obsoletes: boost-devel-static < 1.34.1-14
Provides: boost-devel-static = %{version}-%{release}
Provides: opt-boost-devel-static = %{version}-%{release}

%description static
Static Boost C++ libraries.

%package doc
Summary: HTML documentation for the Boost C++ libraries
Group: Documentation
Provides: boost-python-docs = %{version}-%{release}
Provides: boost-docs = %{version}-%{release}
Provides: opt-boost-python-docs = %{version}-%{release}
Provides: opt-boost-docs = %{version}-%{release}

%description doc
This package contains the documentation in the HTML format of the Boost C++
libraries. The documentation provides the same content as that on the Boost
web page (http://www.boost.org/doc/libs/1_40_0).

%prep
%setup -q -n %{sourcedir}

%build
mkdir -p %{buildroot}%{installroot}

export LD_RUN_PATH="%{_libdir}"

./bootstrap.sh --prefix=%{_prefix}
./b2 -j 24 --prefix=%{_prefix}

%install
./b2 -j 24 variant=release --prefix=%{buildroot}%{_prefix} install


%files

%dir %attr(0755, root, root) %{_libdir}
%dir %attr(0755, root, root) %{_includedir}
%dir %attr(0755, root, root) %{_includedir}/boost 

%files atomic
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_atomic.so.%{sonamever}

%files chrono
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_chrono*.so.%{sonamever}

%files container
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_container.so.%{sonamever}

%files context
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_context.so.%{sonamever}

%files contract
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_contract.so.%{sonamever}

%files coroutine
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_coroutine.so.%{sonamever}

%files date-time
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_date_time*.so.%{sonamever}

%files filesystem
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_filesystem*.so.%{sonamever}

%files graph
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_graph.so.%{sonamever}

%files iostreams
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_iostreams*.so.%{sonamever}

%files locale
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_locale*.so.%{sonamever}

%files log
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_log*.so.%{sonamever}

%files math
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_math*.so.%{sonamever}

%files numpy
%defattr(755, root, root, 755)
%{_libdir}/libboost_numpy*.so.%{sonamever}

%files test
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_prg_exec_monitor*.so.%{sonamever}
%{_libdir}/libboost_unit_test_framework*.so.%{sonamever}

%files program-options
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)

%{_libdir}/libboost_program_options*.so.%{sonamever}

%files python
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)

%{_libdir}/libboost_python*.so.%{sonamever}

%files random 
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)

%{_libdir}/libboost_random*.so.%{sonamever}

%files regex
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)

%{_libdir}/libboost_regex*.so.%{sonamever}

%files serialization
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_serialization*.so.%{sonamever}
%{_libdir}/libboost_wserialization*.so.%{sonamever}

%files signals
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)

%{_libdir}/libboost_signals*.so.%{sonamever}

%files system
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_system*.so.%{sonamever}

%files stacktrace
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_stacktrace*.so.%{sonamever}

%files thread
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_thread*.so.%{sonamever}

%files timer
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_timer*.so.%{sonamever}

%files type_erasure
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_type_erasure*.so.%{sonamever}

%files wave
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)

%{_libdir}/libboost_wave*.so.%{sonamever}

%files doc
%doc LICENSE_1_0.txt
#%defattr(-, root, root, -)
#%doc %{boost_docdir}/*
#%doc %{_prefix}/doc/* 

%files devel
%doc LICENSE_1_0.txt
%defattr(755, root, root, 755)
%{_libdir}/libboost_*.so
%{_includedir}/boost
#%{_datadir}/%{name}-%{version}
#%{_libdir}/boost/Boost*.cmake

%files static
%doc LICENSE_1_0.txt
%defattr(644, root, root, 755)
%{_libdir}/*.a

