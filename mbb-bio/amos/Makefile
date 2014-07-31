FOLDERS=BUILD SRPMS
SPEC=amos-3.1.0.spec

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
