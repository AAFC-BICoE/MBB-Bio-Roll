### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/cython
%define name              Cython
%define release           1
%define version           0.23
%define buildroot         %{_topdir}/%{name}-%{version}-root
%define installroot       /opt/bio/%{name}
%define python            /opt/python/bin/python2.7

Summary:   The Cython compiler for writing C extensions for the Python language.
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source0:   %{name}-%{version}.tar.gz
License:   Apache 2.0
Packager:  Alex MacLean <alex.maclean@agr.gc.ca>
Group:     Development/Librairies
BuildRoot: %{buildroot}
Prefix:    /opt/bio
Vendor:    Robert Bradshaw, Stefan Behnel, Dag Seljebotn, Greg Ewing, et al. <cython-devel@python.org>
Url:       http://cython.org/
AutoReq:   yes

%description
The Cython language makes writing C extensions for the Python language as
easy as Python itself.  Cython is a source code translator based on Pyrex_,
but supports more cutting edge functionality and optimizations.

The Cython language is very close to the Python language (and most Python
code is also valid Cython code), but Cython additionally supports calling C
functions and declaring C types on variables and class attributes. This
allows the compiler to generate very efficient C code from Cython code.

This makes Cython the ideal language for writing glue code for external C
libraries, and for fast C modules that speed up the execution of Python
code.

.. _Pyrex: http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/

%prep
%setup -n %{name}-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" %{python} setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
%{python} setup.py install --home=$RPM_BUILD_ROOT%{installroot}

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/lib
