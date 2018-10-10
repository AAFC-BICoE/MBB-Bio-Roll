# This is a sample spec file for wget
%define debug_package %{nil}

%define name		opt-gdal
%define src_name	gdal
%define release		1
%define version 	1.11.5
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define installroot	/opt/bio/lib/%{src_name}

BuildRoot:		%{buildroot}
Summary: 		GDAL - Geospatial Data Abstraction Library 
License: 		MIT
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz
Packager:		Glen Newton <glen.newton@agr.gc.ca>
Prefix: 		%{installroot}
Group: 			Development/Libraries/GIS
URL:			http://www.gdal.org/
AutoReq:		yes

%description
GDAL is a translator library for raster and vector geospatial data
formats that is released under an X/MIT style Open Source license by
the Open Source Geospatial Foundation. As a library, it presents a
single raster abstract data model and vector abstract data model to
the calling application for all supported formats. It also comes with
a variety of useful commandline utilities for data translation and
processing. The NEWS page describes the April 2014 GDAL/OGR 1.11.0
release.  

%prep
%setup -q -n %{src_name}-%{version}

%build
./configure --prefix=%{installroot}
make -pipe --jobs=`nproc` prefix=%{installroot}

%install
make install prefix=$RPM_BUILD_ROOT%{installroot}

%files
%defattr(644,root,root,755)
%dir %{installroot}
%{installroot}/include
%{installroot}/lib
%{installroot}/share
%defattr(755,root,root,755)
%{installroot}/bin
