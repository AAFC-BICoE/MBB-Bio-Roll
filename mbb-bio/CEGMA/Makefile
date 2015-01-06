FOLDERS=BUILD SRPMS
SPEC=CEGMA_v2.5.spec

.PHONY: clean

package: $(FOLDERS) RPMS

$(FOLDERS):
	mkdir $@

RPMS:
	mkdir $@
	rpmbuild --define '_topdir $(shell pwd)'  -bb --clean SPECS/${SPEC}
	-cd RPMS/x86_64; rpm2cpio *.rpm | cpio -idmv

clean:
	rm -rf RPMS SRPMS BUILD BUILDROOT
