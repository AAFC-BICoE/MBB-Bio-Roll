FOLDERS=BUILD SRPMS
SPEC=EMBOSS.spec

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
