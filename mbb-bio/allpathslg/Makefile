FOLDERS=BUILD SRPMS
SPEC=allpathslg.spec

.PHONY: clean

package: $(FOLDERS) RPMS

$(FOLDERS):
	mkdir $@

RPMS:
	mkdir $@
	rpmbuild --define '_topdir $(shell pwd)'  -bb --clean SPECS/${SPEC}
	-cd RPMS/x86_64; rpm2cpio  allpathslg-50960-1.x86_64.rpm | cpio -idmv

clean:
	rm -rf RPMS SRPMS BUILD BUILDROOT
