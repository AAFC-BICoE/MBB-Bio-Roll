%define name		grass
%define src_name	grass
%define release		1
%define version 	7.4.2
%define shortver	74
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		Open source Geographic Information System (GIS) software suite
License: 		GPLv2
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz
Packager:   		Glen Newton <glen.newton@agr.gc.ca>
Prefix: 		%{installroot}
Group: 			GIS
URL:			http://grass.osgeo.org/
AutoReq:		yes

BuildRequires: 	opt-gdal 
BuildRequires:	opt-geos
BuildRequires:	opt-proj4
BuildRequires:	blas-devel
BuildRequires:	opt-python-27
Requires:	opt-python-27
Requires: 	opt-gdal
Requires:	opt-proj4

Provides:	libgrass_rli.so()(64bit)


%description
GRASS GIS, commonly referred to as GRASS (Geographic Resources Analysis Support System), is a free and open source Geographic Information System (GIS) software suite used for geospatial data management and analysis, image processing, graphics and maps production, spatial modeling, and visualization. GRASS GIS is currently used in academic and commercial settings around the world, as well as by many governmental agencies and environmental consulting companies. It is a founding member of the Open Source Geospatial Foundation (OSGeo).

GRASS GIS contains over 350 modules to render maps and images on monitor and paper; manipulate raster, and vector data including vector networks; process multispectral image data; and create, manage, and store spatial data. GRASS GIS offers both an intuitive graphical user interface as well as command line syntax for ease of operations. GRASS GIS can interface with printers, plotters, digitizers, and databases to develop new data as well as manage existing data.

Config: GISBASE must be set

%prep
%setup -q

%build
GEOS_CONFIG=$(rpm -ql opt-geos | grep 'geos-config$' | head -n1)
GEOS_LIB=$(dirname $(rpm -ql opt-geos | grep 'libgeos.so$' | head -n1))
GDAL_CONFIG=$(rpm -ql opt-gdal | grep 'gdal-config$' | head -n1)
GDAL_LIB=$(dirname $(rpm -ql opt-gdal  | grep 'libgdal.so$' | head -n 1))
PROJ_INCLUDE=$(dirname $(rpm -ql opt-proj4 | grep 'proj_api.h$' | head -n1))
PROJ_LIB=$(dirname $(rpm -ql opt-proj4 | grep 'libproj.so$' | head -n 1))
PROJ_DATA=$(dirname $(rpm -ql opt-proj4 | grep proj_def.dat | head -n 1))
PROJ_BIN=$(dirname $(rpm -ql opt-proj4 | grep nad2bin | head -n 1))
PYTHON=$(rpm -ql opt-python-27 | grep 'python2.7-config$' | head -n1)

export LD_LIBRARY_PATH=$PROJ_LIB:$GEOS_LIB:$GDAL_LIB 
export LD_RUN_PATH=$PROJ_LIB:$GEOS_LIB:$GDAL_LIB:%{_libdir}/%{name}-%{version}/lib
export PATH=$PROJ_BIN:$PATH 
export GRASS_PYTHON="/usr/bin/env python"

./configure --prefix=%{installroot}  --without-fftw --without-freetype -with-cxx --enable-largefile --with-cairo --with-pthread --with-blas --with-lapack --with-python=$PYTHON --enable-64bit --with-proj-includes=$PROJ_INCLUDE --with-proj-libs=$PROJ_LIB --with-geos=$GEOS_CONFIG --with-gdal=$GDAL_CONFIG --with-proj-share=$PROJ_DAT --with-libs=/usr/lib64

make -j`nproc`

%install
make install prefix=%{buildroot}%{_libdir} UNIX_BIN=%{buildroot}%{_bindir}

# Change GISBASE in startup script
sed -i -e 's|%{buildroot}%{_libdir}/%{name}-%{version}|%{_libdir}/%{name}-%{version}|g' \
        %{buildroot}%{_bindir}/%{name}%{shortver}
# fix GRASS_HOME and RUN_GISBASE in Platform.make
sed -i -e 's|%{buildroot}%{_libdir}/%{name}-%{version}|%{_libdir}/%{name}-%{version}|g' \
        %{buildroot}%{_libdir}/%{name}-%{version}/include/Make/Platform.make
# fix ARCH_DISTDIR in Grass.make
sed -i -e 's|%{buildroot}%{_libdir}/%{name}-%{version}|%{_libdir}/%{name}-%{version}|g' \
        %{buildroot}%{_libdir}/%{name}-%{version}/include/Make/Grass.make
# fix ARCH_BINDIR in Grass.make
sed -i -e 's|%{buildroot}%{_bindir}|%{_bindir}|g' \
        %{buildroot}%{_libdir}/%{name}-%{version}/include/Make/Grass.make
# fix GISDBASE in demolocation
sed -i -e 's|%{buildroot}%{_libdir}/%{name}-%{version}|%{_libdir}/%{name}-%{version}|g' \
        %{buildroot}%{_libdir}/%{name}-%{version}/demolocation/.grassrc%{shortver}
# Correct font path
sed -i -e 's|%{buildroot}%{_libdir}/%{name}-%{version}|%{_libdir}/%{name}-%{version}|' \
        %{buildroot}%{_libdir}/%{name}-%{version}/etc/fontcap
# fix paths in grass.pc
sed -i -e 's|%{_prefix}/%{name}-%{version}|%{_libdir}/%{name}-%{version}|g' \
        %{name}.pc


%files
%defattr(-,root,root,755)
%dir %{installroot}
%doc AUTHORS
%doc CHANGES
%doc CITING
%doc COPYING
%doc GPL.TXT
%_libdir
%defattr(755,root,root,755)
%_bindir
