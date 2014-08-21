EXTEND_COMPUTE=xml/extend_compute.xml
BASE=https://dl.fedoraproject.org/pub/epel/6/x86_64

all: \
	RPMS/docker-io-1.1.2-1.el6.x86_64.rpm \
	RPMS/libmspack-0.4-0.1.alpha.el6.x86_64.rpm \
	RPMS/lxc-0.9.0-2.el6.x86_64.rpm \
	RPMS/lxc-libs-0.9.0-2.el6.x86_64.rpm \
	RPMS/wxBase3-3.0.1-1.el6.x86_64.rpm \
	RPMS/wxGTK3-3.0.1-1.el6.x86_64.rpm \
	RPMS/wxGTK3-devel-3.0.1-1.el6.x86_64.rpm \
	RPMS/wxGTK3-gl-3.0.1-1.el6.x86_64.rpm \
	RPMS/wxGTK3-media-3.0.1-1.el6.x86_64.rpm \
	RPMS/wxPython-2.8.12.0-1.el6.x86_64.rpm \
	RPMS/wxPython-devel-2.8.12.0-1.el6.x86_64.rpm \
	RPMS/wxPython-docs-2.8.12.0-1.el6.x86_64.rpm \
	RPMS/wxBase-2.8.12-1.el6.x86_64.rpm \
	RPMS/wxGTK-2.8.12-1.el6.x86_64.rpm \
	RPMS/wxGTK-devel-2.8.12-1.el6.x86_64.rpm\
	RPMS/wxGTK-media-2.8.12-1.el6.x86_64.rpm \
	RPMS/wxGTK-gl-2.8.12-1.el6.x86_64.rpm\
	RPMS/bakefile-0.2.8-3.el6.x86_64.rpm\
	RPMS/python-empy-3.3-5.el6.noarch.rpm\
	RPMS/geos-3.3.2-1.el6.x86_64.rpm\
	RPMS/geos-devel-3.3.2-1.el6.x86_64.rpm \
	RPMS/geos-python-3.3.2-1.el6.x86_64.rpm \
	RPMS/gdal-1.7.3-15.el6.x86_64.rpm \
	RPMS/gdal-devel-1.7.3-15.el6.x86_64.rpm \
	RPMS/libdap-3.11.0-1.el6.x86_64.rpm \
	RPMS/libdap-devel-3.11.0-1.el6.x86_64.rpm \
	RPMS/librx-1.5-14.el6.x86_64.rpm\
	RPMS/librx-devel-1.5-14.el6.x86_64.rpm\
	RPMS/hdf5-1.8.5.patch1-7.el6.x86_64.rpm \
	RPMS/hdf5-devel-1.8.5.patch1-7.el6.x86_64.rpm \
	RPMS/hdf5-static-1.8.5.patch1-7.el6.x86_64.rpm \
	RPMS/libgeotiff-1.2.5-5.el6.x86_64.rpm \
	RPMS/libgeotiff-devel-1.2.5-5.el6.x86_64.rpm\
	RPMS/cfitsio-3.240-3.el6.x86_64.rpm \
	RPMS/cfitsio-devel-3.240-3.el6.x86_64.rpm \
	RPMS/cfitsio-static-3.240-3.el6.x86_64.rpm\
	RPMS/ogdi-3.2.0-0.14.beta2.el6.x86_64.rpm\
	RPMS/ogdi-devel-3.2.0-0.14.beta2.el6.x86_64.rpm\
	RPMS/ogdi-tcl-3.2.0-0.14.beta2.el6.x86_64.rpm \
	RPMS/netcdf-4.1.1-3.el6.5.x86_64.rpm \
	RPMS/netcdf-devel-4.1.1-3.el6.5.x86_64.rpm \
	RPMS/netcdf-static-4.1.1-3.el6.5.x86_64.rpm \
	RPMS/proj-4.7.0-1.el6.x86_64.rpm\
	RPMS/proj-devel-4.7.0-1.el6.x86_64.rpm \
	RPMS/proj-static-4.7.0-1.el6.x86_64.rpm \
	RPMS/proj-epsg-4.7.0-1.el6.x86_64.rpm \
	RPMS/proj-nad-4.7.0-1.el6.x86_64.rpm

clean-all: clean
	rm -rf RPMS/*.rpm

clean:
	-rm $(EXTEND_COMPUTE)

extend-compute:
	-rm $(EXTEND_COMPUTE)
	echo ""  >> $(EXTEND_COMPUTE)
	echo "<!-- START MBB-Bio-Roll pre-build RPM dependencies  -->"  >> $(EXTEND_COMPUTE)
	echo "<!-- Generated " `date` "-->"  >> $(EXTEND_COMPUTE)
	echo ""  >> $(EXTEND_COMPUTE)
	echo "<package>docker-io</package</a>" >> $(EXTEND_COMPUTE)
	echo "<package>lxc</package</a>" >> $(EXTEND_COMPUTE)
	echo "<package>lxc-libs</package</a>" >> $(EXTEND_COMPUTE)
	echo ""  >> $(EXTEND_COMPUTE)
	echo "<!-- END MBB-Bio-Roll pre-build RPM dependencies  -->"  >> $(EXTEND_COMPUTE)
	echo ""  >> $(EXTEND_COMPUTE)

RPMS/docker-io-1.1.2-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/docker-io-1.1.2-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/lxc-0.9.0-2.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/lxc-0.9.0-2.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/lxc-libs-0.9.0-2.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/lxc-libs-0.9.0-2.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/wxBase3-3.0.1-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/wxBase3-3.0.1-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/wxGTK3-3.0.1-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/wxGTK3-3.0.1-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/wxGTK3-devel-3.0.1-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/wxGTK3-devel-3.0.1-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/wxGTK3-gl-3.0.1-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/wxGTK3-gl-3.0.1-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/wxGTK3-media-3.0.1-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/wxGTK3-media-3.0.1-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/wxPython-2.8.12.0-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/wxPython-2.8.12.0-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/wxPython-devel-2.8.12.0-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/wxPython-devel-2.8.12.0-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/wxPython-docs-2.8.12.0-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/wxPython-docs-2.8.12.0-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/libmspack-0.4-0.1.alpha.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/libmspack-0.4-0.1.alpha.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/wxBase-2.8.12-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/wxBase-2.8.12-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/wxGTK-2.8.12-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/wxGTK-2.8.12-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/wxGTK-devel-2.8.12-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/wxGTK-devel-2.8.12-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/wxGTK-media-2.8.12-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/wxGTK3-docs-3.0.1-1.el6.noarch.rpm
	chmod 444 RPMS/*.rpm

RPMS/wxGTK-gl-2.8.12-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/wxGTK-gl-2.8.12-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm



RPMS/bakefile-0.2.8-3.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/bakefile-0.2.8-3.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm



RPMS/python-empy-3.3-5.el6.noarch.rpm:
	cd RPMS;wget $(BASE)/python-empy-3.3-5.el6.noarch.rpm
	chmod 444 RPMS/*.rpm

RPMS/geos-3.3.2-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/geos-3.3.2-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/geos-devel-3.3.2-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/geos-devel-3.3.2-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/geos-python-3.3.2-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/geos-python-3.3.2-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/gdal-1.7.3-15.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/gdal-1.7.3-15.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/gdal-devel-1.7.3-15.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/gdal-devel-1.7.3-15.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm



RPMS/libdap-3.11.0-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/libdap-3.11.0-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/libdap-devel-3.11.0-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/libdap-devel-3.11.0-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm


RPMS/librx-1.5-14.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/librx-1.5-14.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/librx-devel-1.5-14.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/librx-devel-1.5-14.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/hdf5-1.8.5.patch1-7.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/hdf5-1.8.5.patch1-7.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/hdf5-devel-1.8.5.patch1-7.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/hdf5-devel-1.8.5.patch1-7.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/hdf5-static-1.8.5.patch1-7.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/hdf5-static-1.8.5.patch1-7.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/libgeotiff-1.2.5-5.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/libgeotiff-1.2.5-5.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/libgeotiff-devel-1.2.5-5.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/libgeotiff-devel-1.2.5-5.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/cfitsio-3.240-3.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/cfitsio-3.240-3.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/cfitsio-devel-3.240-3.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/cfitsio-devel-3.240-3.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/cfitsio-static-3.240-3.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/cfitsio-static-3.240-3.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/ogdi-3.2.0-0.14.beta2.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/ogdi-3.2.0-0.14.beta2.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/ogdi-devel-3.2.0-0.14.beta2.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/ogdi-devel-3.2.0-0.14.beta2.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/ogdi-tcl-3.2.0-0.14.beta2.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/ogdi-tcl-3.2.0-0.14.beta2.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/netcdf-4.1.1-3.el6.5.x86_64.rpm:
	cd RPMS;wget $(BASE)/netcdf-4.1.1-3.el6.5.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/netcdf-devel-4.1.1-3.el6.5.x86_64.rpm:
	cd RPMS;wget $(BASE)/netcdf-devel-4.1.1-3.el6.5.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/netcdf-static-4.1.1-3.el6.5.x86_64.rpm:
	cd RPMS;wget $(BASE)/netcdf-static-4.1.1-3.el6.5.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/proj-4.7.0-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/proj-4.7.0-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/proj-devel-4.7.0-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/proj-devel-4.7.0-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm

RPMS/proj-static-4.7.0-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/proj-static-4.7.0-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm



RPMS/proj-epsg-4.7.0-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/proj-epsg-4.7.0-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm



RPMS/proj-nad-4.7.0-1.el6.x86_64.rpm:
	cd RPMS;wget $(BASE)/proj-nad-4.7.0-1.el6.x86_64.rpm
	chmod 444 RPMS/*.rpm


# RPMS/:
# 	cd RPMS;wget $(BASE)/
# 	chmod 444 RPMS/*.rpm







