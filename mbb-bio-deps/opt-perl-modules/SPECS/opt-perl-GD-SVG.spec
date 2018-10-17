#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-GD-SVG
#    Version:           0.33
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only GD\:\:SVG
#

Name:           opt-perl-GD-SVG
Version:        0.33
Release:        1%{?dist}
Summary:        Seamlessly enable SVG output from scripts written using GD
License:        Unknown license: unknown
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/GD-SVG/
BuildRoot:      /tmp/cpantorpm/GD-SVG-0.33-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/T/TW/TWH/GD-SVG-0.33.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(GD::SVG) = 0.33
Provides:       opt-perl(GD::SVG::Font) = 0.33
Provides:       opt-perl(GD::SVG::Image) = 0.33
Provides:       opt-perl(GD::SVG::Polygon) = 0.33
Requires:       opt-perl
Requires:       opt-perl(GD)
Requires:       opt-perl(SVG)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(GD)
BuildRequires:  opt-perl(SVG)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
GD::SVG painlessly enables scripts that utilize GD to export scalable
vector graphics (SVG). It accomplishes this task by wrapping SVG.pm with
GD-styled method calls. To enable this functionality, one need only change
the "use GD" call to "use GD::SVG" (and initial "new" method calls).

%prep

%setup  -n GD-SVG-0.33
chmod -R u+w %{_builddir}/GD-SVG-%{version}

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
/opt/perl/lib/site_perl/5.26.0/*
/opt/perl/man/man3/*

%changelog
* Thu Oct 04 2018 Rocks 0.33-1
- Generated using cpantorpm

