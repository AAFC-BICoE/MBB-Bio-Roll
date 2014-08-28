FOLDERS=BUILD SRPMS
SPEC=abyss-1.5.2-1.spec

.PHONY: clean

package: $(FOLDERS) RPMS

$(FOLDERS):
	mkdir $@

RPMS:

	mkdir $@
	export CPLUS_INCLUDE_PATH=/opt/bio/boost/include; rpmbuild --define '_topdir $(shell pwd)'  -bb --clean SPECS/${SPEC}

clean:
	rm -rf RPMS SRPMS BUILD BUILDROOT
