FOLDERS=BUILD SRPMS
SPEC=trinity.spec

.PHONY: clean

package: $(FOLDERS) RPMS

$(FOLDERS):
	mkdir $@

RPMS:
	mkdir $@
	# Trick RPM into thinking there is a valid SOURCES file; must be >13bytes
	test -s SOURCES/trinityrnaseq-2.0.2.tar.bz2|| echo "12345678901234" > SOURCES/trinityrnaseq-2.0.2.tar.bz2	
	rpmbuild --define '_topdir $(shell pwd)'  -bb --clean SPECS/${SPEC}
	rpm -qlpv RPMS/x86_64/*.rpm
	echo "12345678901234" > SOURCES/trinityrnaseq-2.0.2.tar.bz2		

clean:
	rm -rf RPMS SRPMS BUILD BUILDROOT
	echo "12345678901234" > SOURCES/trinityrnaseq-2.0.2.tar.bz2		
