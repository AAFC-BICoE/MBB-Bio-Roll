# This is a sample spec file for wget
%define debug_package %{nil}

### define _topdir	 	/home/rpmbuild/rpms/%{name}
%define name			opt-proj4
%define src_name		proj.4
%define release			1
%define version 		4.9.3
%define buildroot 		%{_topdir}/%{name}-%{version}-root
%define installroot 		/opt/bio/%{src_name}

BuildRoot:		%{buildroot}
Summary: 		PROJ.4 Cartographic Projections library
License: 	  	MIT
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		proj-%{version}.tar.gz
Packager:   		Glen Newton <glen.newton@agr.gc.ca>
Prefix: 		/opt/bio
Group: 			Development/Libraries/GIS
URL:			http://trac.osgeo.org/proj/
AutoReq:		yes

%description
PROJ.4 is a library for performing conversions between cartographic projections. The library is based on the work of Gerald Evenden at the USGS,[2] but is now an OSGeo project maintained by Frank Warmerdam. The library also ships with executables for performing these transformations from the command line (Fromwikipedia: https://en.wikipedia.org/wiki/PROJ.4 )

%prep
%setup -q -n %{src_name}-%{version}

%build
./autogen.sh
./configure --prefix=%{installroot}
make prefix=%{installroot}

%install
make install prefix=$RPM_BUILD_ROOT%{installroot}

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,) 
%{installroot}/bin/*
