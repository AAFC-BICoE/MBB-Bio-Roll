### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/pysam
%define name pysam
%define version 0.8.3
%define release 3
%define installroot       /opt/bio/lib/%{name}

Summary: Pysam is a python module for reading and manipulating files in the SAM/BAM format.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: master.zip
Group: Development/Libraries
Prefix: /opt/bio/lib
License:   MIT License
Vendor: Andreas Heger and contributors
Packager:  Xie Qiu <xie.qiu@agr.gc.ca>
Url: https://github.com/pysam-developers/pysam
AutoReq:   yes
Requires: Cython >= 0.22
%description
Pysam is a python module for reading and manipulating Samfiles. It's a lightweight wrapper of the samtools C-API. Pysam also includes an interface for tabix.

%prep
%setup -q -n pysam-master

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --prefix=%{installroot} --root=$RPM_BUILD_ROOT 

%files 
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/lib
