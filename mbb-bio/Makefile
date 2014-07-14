SUBDIRS=$(shell find -maxdepth 1 -mindepth 1 -type d -not -name ".*" -exec basename {} \;)
PACKAGEDIRS=$(SUBDIRS:%=package-%)
CLEANDIRS=$(SUBDIRS:%=clean-%)

.PHONY: SUBDIRS
.PHONY: PACKAGEDIRS
.PHONY: CLEANDIRS

thisDir=$(shell pwd)
perl=/usr/bin/perl

package: $(PACKAGEDIRS)
$(PACKAGEDIRS):
	$(MAKE) -C $(@:package-%=%) package

clean: $(CLEANDIRS)
$(CLEANDIRS):
	$(MAKE) -C $(@:clean-%=%) clean

roll: 
	mkdir -p /export/src/roll
	cd /export/src/roll
	rocks create new roll name=mbb-bio

