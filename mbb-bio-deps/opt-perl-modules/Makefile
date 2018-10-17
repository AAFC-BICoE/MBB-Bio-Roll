FOLDERS=BUILD SRPMS

.PHONY: clean
.PHONY: RPMS

package: $(FOLDERS)

$(FOLDERS):
	mkdir $@

RPMS:
	WORKDIR=$(shell pwd) sh buildmodules.sh opt-perl-modules-list

clean:
	rm -rf SRPMS BUILD BUILDROOT
