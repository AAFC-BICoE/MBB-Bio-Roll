FOLDERS=BUILD SRPMS
SPEC=gmap-gsnap-2014-10-22-1.spec

.PHONY: clean

package: $(FOLDERS) RPMS

$(FOLDERS):
	mkdir $@

RPMS:
	mkdir $@
	rpmbuild --define '_topdir $(shell pwd)'  -bb --clean SPECS/${SPEC}
	rpm -qplv ./RPMS/x86_64/*.rpm 

clean:
	rm -rf RPMS SRPMS BUILD BUILDROOT
