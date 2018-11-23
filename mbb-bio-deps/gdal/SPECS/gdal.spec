%define name		opt-gdal
%define src_name	gdal
%define release		1
%define version 	1.11.5
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define installroot	/opt/bio/lib/%{src_name}
%define	_prefix		%{installroot}
%define _libdir		%{_prefix}/lib

BuildRoot:		%{buildroot}
Summary: 		GDAL - Geospatial Data Abstraction Library 
License: 		MIT
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz
Packager:		Glen Newton <glen.newton@agr.gc.ca>
Prefix: 		%{_prefix}
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
./configure --prefix=%{_prefix}
make -pipe --jobs=`nproc`

%install
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc LICENSE.TXT
%{_includedir}
%{_datadir}
%defattr(755,root,root,755)
%{_libdir}
%{_bindir}
