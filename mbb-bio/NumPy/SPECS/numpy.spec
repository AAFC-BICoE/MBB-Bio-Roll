### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/NumPy
%define name NumPy
%define version 1.11.0
%define release 1
%define installroot       /opt/bio/lib/%{name}

summary: NumPy is the fundamental package for scientific computing with Python.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: numpy-1.11.0.tar.gz
Patch0: site.cfg.patch
Group: Development/Tools
License: BSD 3-Clause
Vendor: NumPy Developers
Packager: Alex MacLean <alex.maclean@agr.gc.ca>
Url: http://www.numpy.org/ 
AutoReq: yes
AutoProv: yes

%description
NumPy is the fundamental package for scientific computing with Python. It contains among other things:

- a powerful N-dimensional array object
- sophisticated (broadcasting) functions
- tools for integrating C/C++ and Fortran code
- useful linear algebra, Fourier transform, and random number capabilities

Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.

Numpy is licensed under the BSD license, enabling reuse with few restrictions.

%prep
%setup -q -n numpy-1.11.0
patch site.cfg.example -i /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/NumPy/SOURCES/site.cfg.patch -o site.cfg

%build
python setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
mkdir ../install
export PYTHONPATH=$PYTHONPATH:/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/NumPy/BUILD/install/lib/python2.7/site-packages
mkdir -p /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/NumPy/BUILD/install/lib/python2.7/site-packages
python setup.py install --prefix=/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/NumPy/BUILD/install
cp -r ../install/bin ../install/lib $RPM_BUILD_ROOT%{installroot}

%files 
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/lib
