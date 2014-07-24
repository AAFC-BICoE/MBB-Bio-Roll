

all: 
	cd mbb-bio-deps; make
	cd mbb-bio; make

clean:
	cd mbb-bio-deps; make clean
	cd mbb-bio; make clean

paths: all
	bin/rpmpaths */*/RPMS/x86_64/*.rpm

rpmlint:
	find . -name \*.spec -exec rpmlint {} \;

paths:
	find . -name \*.rpm -print | bin/rpmpaths -c






