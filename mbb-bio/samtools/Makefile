FOLDERS=BUILD SRPMS
SPEC=samtools-0.1.19.spec
SPEC1=tabix-0.2.6-1.spec

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
