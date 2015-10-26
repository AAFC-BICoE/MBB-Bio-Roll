### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/setuptools
%define name setuptools
%define version 18
%define release 4
%define installroot       /opt/bio/lib/%{name}

Summary: TSetuptools is a fully-featured, actively-maintained, and stable library designed to facilitate packaging Python projects.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: setuptools-18.4.zip
Group: Development/Libraries
Prefix: /opt/bio/lib
License:    PSF or ZPL
Vendor: Python Packaging Authority <distutils-sig@python.org>
Packager:  Xie Qiu <xie.qiu@agr.gc.ca>
Url: https://pypi.python.org/pypi/setuptools
AutoReq:   yes

%description
Setuptools is a package development process library designed to facilitate packaging Python projects by enhancing the Python standard library distutils (distribution utilities). It includes:

Python package and module definitions
Distribution package metadata
Test hooks
Project installation
Platform-specific details
Python 3 support

%prep
%setup -q -n %{name}-%{version}.%{release}

%build
#env CFLAGS="$RPM_OPT_FLAGS" python setup.py build
python setup.py build

%install
python setup.py install --prefix=%{installroot} --root=$RPM_BUILD_ROOT 

%files 
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/lib
