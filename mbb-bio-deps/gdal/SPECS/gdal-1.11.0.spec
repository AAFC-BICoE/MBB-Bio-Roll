# This is a sample spec file for wget

### define _topdir	 	/home/rpmbuild/rpms/%{name}
%define name			gdal
%define src_name		gdal
%define release		1
%define version 	1.11.0
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	GDAL - Geospatial Data Abstraction Library 
License: 		{"licenses": [{"name": "MIT", "url": "https://svn.osgeo.org/gdal/tags/1.11.0/gdal/LICENSE.TXT"},{"name": "Others", "url": "https://svn.osgeo.org/gdal/tags/1.11.0/gdal/LICENSE.TXT"}]}
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz
Packager:   Glen Newton <glen.newton@agr.gc.ca>
Prefix: 		/opt/bio
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
%setup -q

%build
./configure --prefix=/opt/bio/gdal
make prefix=%{installroot}

%install
make install prefix=$RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root,755)
%{installroot}
