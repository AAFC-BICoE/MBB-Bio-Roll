FOLDERS=BUILD SRPMS
SPEC=glibc.spec

.PHONY: clean

package: $(FOLDERS) RPMS

$(FOLDERS):
	mkdir $@

RPMS:
	mkdir $@
	rpmbuild --define '_topdir $(shell pwd)' -bb SPECS/${SPEC}

clean:
	rm -rf RPMS SRPMS BUILD BUILDROOT
