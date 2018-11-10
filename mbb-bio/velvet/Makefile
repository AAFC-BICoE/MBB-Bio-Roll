FOLDERS=BUILD SRPMS
SPEC=velvet.spec

.PHONY: clean

package: $(FOLDERS) RPMS

$(FOLDERS):
	mkdir $@

RPMS:
	mkdir $@
	rpmbuild --define '_topdir $(shell pwd)' -bb --clean SPECS/${SPEC}

clean:
	rm -rf RPMS SRPMS BUILD BUILDROOT

test: RPMS
	-cd RPMS/x86_64; rpm2cpio velvet-1.2.08-3.x86_64.rpm | cpio -idmv
	-RPMS/x86_64/opt/bio/velvet/velvetg_127
	-RPMS/x86_64/opt/bio/velvet/velvetg_145
	-RPMS/x86_64/opt/bio/velvet/velvetg_195
	-RPMS/x86_64/opt/bio/velvet/velvetg_245
	-RPMS/x86_64/opt/bio/velvet/velvetg_31
	-RPMS/x86_64/opt/bio/velvet/velvetg_63
	RPMS/x86_64/opt/bio/velvet/velveth_127
	RPMS/x86_64/opt/bio/velvet/velveth_145
	RPMS/x86_64/opt/bio/velvet/velveth_195
	RPMS/x86_64/opt/bio/velvet/velveth_245
	RPMS/x86_64/opt/bio/velvet/velveth_31
	rm -rf RPMS/x86_64/opt
