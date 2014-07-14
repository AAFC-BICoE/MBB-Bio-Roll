FOLDERS=BUILD SRPMS
SPEC=fastx-0.0.13-1.spec
SPEC1=libgtextutils-0.6.1-1.spec

.PHONY: clean

package: $(FOLDERS) RPMS

$(FOLDERS):
	mkdir $@

RPMS:
	mkdir $@
	rpmbuild --define '_topdir $(shell pwd)'  -bb --clean SPECS/${SPEC}
	rpmbuild --define '_topdir $(shell pwd)'  -bb --clean SPECS/${SPEC1}

clean:
	rm -rf RPMS SRPMS BUILD BUILDROOT
