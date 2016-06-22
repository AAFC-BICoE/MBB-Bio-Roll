### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/HTSeq
%define name HTSeq
%define version 0.6.1
%define release 1
%define installroot       /opt/bio/%{name}

summary: HTSeq is a Python package that provides infrastructure to process data from high-throughput sequencing assays.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
Group: Development/Tools
License: GPL v3.0
Vendor: Free Software Foundation, Inc. <http://fsf.org/>
Packager: Alex MacLean <alex.maclean@agr.gc.ca>
Url: http://www-huber.embl.de/users/anders/HTSeq/doc/overview.html
AutoReq: yes
AutoProv: yes

%description
HTSeq is a Python package that provides infrastructure to process data from high-throughput sequencing assays.

%prep
%setup -q

%build
python setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
mkdir -p /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/HTSeq/BUILD/install/lib/python2.7/site-packages
export PYTHONPATH=$PYTHONPATH:/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/HTSeq/BUILD/install/lib/python2.7/site-packages
python setup.py install --prefix=/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/HTSeq/BUILD/install
cp -r ../install/bin ../install/lib $RPM_BUILD_ROOT%{installroot}

%files 
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/lib
