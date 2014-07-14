FOLDERS=BUILD SRPMS
SPEC=cd-hit-otu-454.0.0.2-patched-1.spec
SPEC1=cd-hit-v4.6.1-2012-08-27-2.spec

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
