%define name		opt-proj4
%define src_name	proj.4
%define release		1
%define version 	4.9.3
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{src_name}
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

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
./configure --prefix=%{_prefix}
make -j`nproc`

%install
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%doc NEWS
%{_includedir}
%{_datadir}/proj/
%{_mandir}
%defattr(755,root,root,) 
%{_libdir}
%{_bindir}
