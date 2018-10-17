#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Curses
#    Version:           1.36
#    cpantorpm version: 1.08
#    Date:              Wed Oct 17 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Curses
#

Name:           opt-perl-Curses
Version:        1.36
Release:        1%{?dist}
Summary:        unknown
License:        Unknown license: unknown
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Curses/
BuildRoot:      /tmp/cpantorpm/Curses-1.36-inst
BuildArch:      %{_arch}
Source0:        http://search.cpan.org/authors/id/authors/id/G/GI/GIRAFFED/Curses-1.36.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Curses) = 1.36
Provides:       opt-perl(Curses::Field) = 1.36
Provides:       opt-perl(Curses::Form) = 1.36
Provides:       opt-perl(Curses::Item) = 1.36
Provides:       opt-perl(Curses::Menu) = 1.36
Provides:       opt-perl(Curses::Panel) = 1.36
Provides:       opt-perl(Curses::Screen) = 1.36
Provides:       opt-perl(Curses::Window) = 1.36
Requires:       opt-perl
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Curses is the interface between Perl and your system's curses(3)
library. For descriptions on the usage of a given function, variable, or
constant, consult your system's documentation, as such information
invariably varies (:-) between different curses(3) libraries and operating
systems. This document describes the interface itself, and assumes that you
already know how your system's curses(3) library works.

%prep

%setup  -n Curses-1.36
chmod -R u+w %{_builddir}/Curses-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS" INSTALLDIRS=site SITEPREFIX=/opt/perl INSTALLSITEARCH=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi INSTALLSITELIB=/opt/perl/lib/site_perl/5.26.0 INSTALLSITEBIN=/opt/perl/bin INSTALLSITESCRIPT=/opt/perl/bin INSTALLSITEMAN1DIR=/opt/perl/man/man1 INSTALLSITEMAN3DIR=/opt/perl/man/man3 INSTALLSCRIPT=/opt/perl/bin
make %{?_smp_mflags}

#
# This is included here instead of in the 'check' section because
# older versions of rpmbuild (such as the one distributed with RHEL5)
# do not do 'check' by default.
#

if [ -z "$RPMBUILD_NOTESTS" ]; then
   make test
fi

%install

rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%clean

rm -rf $RPM_BUILD_ROOT

%files

%defattr(-,root,root,-)
/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi/*
/opt/perl/man/man3/*

%changelog
* Wed Oct 17 2018 Rocks 1.36-1
- Generated using cpantorpm

