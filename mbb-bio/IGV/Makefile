FOLDERS=BUILD SRPMS
SPEC=IGV.spec

.PHONY: clean

package: $(FOLDERS) RPMS

$(FOLDERS):
	mkdir $@

RPMS:
	mkdir $@
	spectool -C SOURCES -g SPECS/${SPEC}
	rpmbuild --define '_topdir $(shell pwd)'  -bb --clean SPECS/${SPEC}

clean:
	rm -rf RPMS SRPMS BUILD BUILDROOT
