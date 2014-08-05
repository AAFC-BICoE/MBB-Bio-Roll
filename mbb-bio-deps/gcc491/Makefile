FOLDERS=BUILD SRPMS
SPEC=gcc-4.9.1.spec

.PHONY: clean

package: $(FOLDERS) RPMS

$(FOLDERS):
	mkdir $@

RPMS:
	mkdir $@
	rpmbuild --define '_topdir $(shell pwd)'  -bb --clean SPECS/${SPEC}
	rpm -qlpv RPMS/x86_64/*.rpm

clean:
	rm -rf RPMS SRPMS BUILD BUILDROOT
