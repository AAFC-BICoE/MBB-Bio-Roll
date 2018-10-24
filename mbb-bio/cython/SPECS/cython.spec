%define name 		opt-cython
%define src_name	Cython
%define version		0.29
%define release		1
%define installroot     /opt/python
%define _prefix		%{installroot}

Summary: 		The Cython compiler for writing C extensions for the Python language.
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source0: 		%{src_name}-%{version}.tar.gz
Group: 			Development/Libraries
Prefix: 		%{installroot}
License:   		Apache 2.0
Vendor: 		Robert Bradshaw, Stefan Behnel, Dag Seljebotn, Greg Ewing, et al. <cython-devel@python.org>
Packager:  		Xie Qiu <xie.qiu@agr.gc.ca>
Url: 			http://cython.org/
AutoReq:   		yes

BuildRequires:		opt-python-27
BuildRequires:		opt-python-3
Requires:		opt-python-27
Requires:		opt-python-3

%global __requires_exclude ^libpython3.6m.so.1.0

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
%setup -n %{src_name}-%{version}

%build

%install
python2 setup.py install --prefix=%{installroot} --root=$RPM_BUILD_ROOT
make clean
mkdir python3
LD_LIBRARY_PATH=/opt/python/lib LD_RUN_PATH=/opt/python/lib python3.6m setup.py install --prefix=%{installroot} --root=$RPM_BUILD_ROOT --install-scripts=./python3
cd %{buildroot}/python3
for i in *; do
	mv $i %{buildroot}%{installroot}/bin/${i}3
done
rm -rf %{buildroot}/python3

%files 
%defattr(644,root,root,755)
%dir %{installroot}
%{installroot}/lib
%defattr(755,root,root,755)
%{installroot}/bin

