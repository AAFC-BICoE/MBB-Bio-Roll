SUBDIRS=$(shell find -maxdepth 1 -mindepth 1 -type d -not -name ".*" -exec basename {} \;)
PACKAGEDIRS=$(SUBDIRS:%=package-%)
CLEANDIRS=$(SUBDIRS:%=clean-%)

.PHONY: SUBDIRS
.PHONY: PACKAGEDIRS
.PHONY: CLEANDIRS

thisDir=$(shell pwd)

package: $(PACKAGEDIRS)
$(PACKAGEDIRS):
	$(MAKE) -C $(@:package-%=%) package

clean: $(CLEANDIRS)
$(CLEANDIRS):
	$(MAKE) -C $(@:clean-%=%) clean

install-rpms: 
	rpm -fi */RPMS/x86_64/*.rpm

remove-rpms: 
	rpm -fe */RPMS/x86_64/*.rpm

roll: 
	mkdir -p /export/src/roll
	cd /export/src/roll
	rocks create new roll name=mbb-bio

