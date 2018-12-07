FOLDERS=BUILD SRPMS
SPEC=ImageMagick.spec

.PHONY: clean

package: $(FOLDERS) RPMS

$(FOLDERS):
	mkdir $@

RPMS:
	mkdir $@
	rpmbuild --define '_topdir $(shell pwd)'  -bb --clean SPECS/${SPEC} 2>&1

clean:
	rm -rf RPMS SRPMS BUILD BUILDROOT
