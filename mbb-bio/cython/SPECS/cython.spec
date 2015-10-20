### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/cython
%define name Cython
%define version 0.24.0a0
%define release 1
%define installroot       /opt/bio/lib/%{name}

Summary: The Cython compiler for writing C extensions for the Python language.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: Cython-0.24.0a0.zip
Group: Development/Libraries
Prefix: /opt/bio/lib
License:   Apache 2.0
Vendor: Robert Bradshaw, Stefan Behnel, Dag Seljebotn, Greg Ewing, et al. <cython-devel@python.org>
Packager:  Xie Qiu <xie.qiu@agr.gc.ca>
Url: http://cython.org/
AutoReq:   yes

%description
The Cython language makes writing C extensions for the Python language as
easy as Python itself.  Cython is a source code translator based on Pyrex_,
but supports more cutting edge functionality and optimizations.

The Cython language is a superset of the Python language (almost all Python
code is also valid Cython code), but Cython additionally supports optional
static typing to natively call C functions, operate with C++ classes and
declare fast C types on variables and class attributes.  This allows the
compiler to generate very efficient C code from Cython code.

This makes Cython the ideal language for writing glue code for external
C/C++ libraries, and for fast C modules that speed up the execution of
Python code.

.. _Pyrex: http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/


%prep
%setup -n cython-master

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --prefix=%{installroot} --root=$RPM_BUILD_ROOT 

%files 
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/lib

