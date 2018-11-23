%define name		opt-geos
%define src_name	geos
%define release		1
%define version 	3.4.3
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define installroot	/opt/bio/lib/%{src_name}
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

BuildRoot:		%{buildroot}
Summary: 		GEOS (Geometry Engine - Open Source)
License: 		LGPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.bz2
Prefix: 		%{_prefix}
Group: 			Development/Libraries/GIS
URL:			http://trac.osgeo.org/geos/
AutoReq:		yes
Packager:		Glen Newton <glen.newton@agr.gc.ca>

%description
GEOS (Geometry Engine - Open Source) is a C++ port of the  Java Topology Suite (JTS). As such, it aims to contain the complete functionality of JTS in C++. This includes all the  OpenGIS Simple Features for SQL spatial predicate functions and spatial operators, as well as specific JTS enhanced topology functions.
GEOS is available under the terms of  GNU Lesser General Public License (LGPL), and is a project of  OSGeo.
Capabilities Include:
    Geometries: Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, GeometryCollection;
    Predicates: Intersects, Touches, Disjoint, Crosses, Within, Contains, Overlaps, Equals, Covers;
    Operations: Union, Distance, Intersection, Symmetric Difference, Convex Hull, Envelope, Buffer, Simplify, Polygon Assembly, Valid, Area, Length,;
    Prepared geometries (pre-spatially indexed);
    STR spatial index;
    OGC Well Known Text (WKT) and Well Known Binary (WKB) encoders and decoders.;
    C and C++ API (C API gives long term ABI stability);
    Thread safe (using the reentrant API). 

%prep
%setup -q -n %{src_name}-%{version}

%build
./configure --prefix=%{_prefix}
make  --jobs=`nproc`

%install
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc COPYING
%doc AUTHORS
%{_includedir}
%defattr(755,root,root,755)
%{_libdir}
%{_bindir}
