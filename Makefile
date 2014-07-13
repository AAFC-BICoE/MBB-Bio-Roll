
clean:
	cd mbb-bio-deps; make clean
	cd mbb-bio; make clean

all: 
	cd mbb-bio-deps; make
	cd mbb-bio; make



