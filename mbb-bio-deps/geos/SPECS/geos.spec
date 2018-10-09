%define debug_package %{nil}
### define _topdir	 	/home/rpmbuild/rpms/%{name}
%define name			geos
%define src_name		geos
%define release		1
%define version 	3.4.2
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	GEOS (Geometry Engine - Open Source)
License: 		LGPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.bz2
Prefix: 		/opt/bio
Group: 			Development/Libraries/GIS
URL:			http://trac.osgeo.org/geos/
AutoReq:		yes
Packager:   Glen Newton <glen.newton@agr.gc.ca>

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
%setup -q

%build
./configure --prefix=/opt/bio/gdal
make  --jobs=`nproc` prefix=%{installroot}

%install
make install prefix=$RPM_BUILD_ROOT%{installroot}

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
