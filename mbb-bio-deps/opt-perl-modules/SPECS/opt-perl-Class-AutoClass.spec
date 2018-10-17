#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Class-AutoClass
#    Version:           1.56
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Class\:\:AutoClass
#

Name:           opt-perl-Class-AutoClass
Version:        1.56
Release:        1%{?dist}
Summary:        Create get and set methods and simplify object initialization
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Class-AutoClass/
BuildRoot:      /tmp/cpantorpm/Class-AutoClass-1.56-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/N/NA/NATG/Class-AutoClass-1.56.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Class::AutoClass) = 1.56
Provides:       opt-perl(Class::AutoClass::Root) = 1.56
Requires:       opt-perl
BuildRequires:  opt-perl
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This is yet another module that generates standard 'get' and 'set' methods
for Perl classes. It also handles initialization of object and class data
from parameter lists or defaults, and arranges for object creation and
initialization to occur in top-down, textbook order even in the presence of
multiple inheritance.

%prep

%setup  -n Class-AutoClass-1.56
chmod -R u+w %{_builddir}/Class-AutoClass-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Build.PL optimize="$RPM_OPT_FLAGS" --installdirs site --install_path arch=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi --install_path lib=/opt/perl/lib/site_perl/5.26.0 --install_path script=/opt/perl/bin --install_path bin=/opt/perl/bin --install_path libdoc=/opt/perl/man/man3 --install_path bindoc=/opt/perl/man/man1
./Build

#
# This is included here instead of in the 'check' section because
# older versions of rpmbuild (such as the one distributed with RHEL5)
# do not do 'check' by default.
#

if [ -z "$RPMBUILD_NOTESTS" ]; then
   ./Build test
fi

%install

rm -rf $RPM_BUILD_ROOT
./Build pure_install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%clean

rm -rf $RPM_BUILD_ROOT

%files

%defattr(-,root,root,-)
/opt/perl/lib/site_perl/5.26.0/*
/opt/perl/man/man3/*

%changelog
* Thu Oct 04 2018 Rocks 1.56-1
- Generated using cpantorpm

