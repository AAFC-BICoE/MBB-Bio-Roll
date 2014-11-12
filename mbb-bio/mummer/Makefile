FOLDERS=BUILD SRPMS
SPEC=mummer.3.23.spec

.PHONY: clean

package: $(FOLDERS) RPMS

$(FOLDERS):
	mkdir $@

RPMS:
	mkdir $@
	rpmbuild --define '_topdir $(shell pwd)' -bb --clean SPECS/${SPEC}
	rpm -qplv ./RPMS/x86_64/*.rpm 

clean:
	rm -rf RPMS SRPMS BUILD BUILDROOT
	rm build.log

