FOLDERS=BUILD SRPMS
SPEC=FastOrtho.spec

.PHONY: clean

package: $(FOLDERS) RPMS

$(FOLDERS):
	mkdir $@

RPMS:
	mkdir $@
	rpmbuild --define '_topdir $(shell pwd)' -bb --clean SPECS/${SPEC}

clean:
	rm -rf RPMS SRPMS BUILD BUILDROOT

