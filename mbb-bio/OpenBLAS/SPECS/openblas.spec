### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/OpenBLAS
%define name OpenBLAS
%define version 0.2.18
%define release 1
%define installroot       /opt/bio/%{name}

Summary: OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: v0.2.18.tar.gz
Group: Development/Libraries
Prefix: /opt/bio
License: BSD
Vendor: The OpenBLAS Project
Packager: Alex MacLean <alex.maclean@agr.gc.ca>
Url: http://www.openblas.net/
AutoReq: yes
AutoProv: yes

%description
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD version.

%prep
%setup -q

%build
make FC=gfortran

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
mkdir ../install
make PREFIX=/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/OpenBLAS/BUILD/install install
cd ../install
cp -r bin lib include $RPM_BUILD_ROOT%{installroot}

%files 
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/lib
%{installroot}/include
