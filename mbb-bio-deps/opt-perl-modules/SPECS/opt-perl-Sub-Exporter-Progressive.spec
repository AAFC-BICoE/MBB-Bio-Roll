#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Sub-Exporter-Progressive
#    Version:           0.001013
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Sub\:\:Exporter\:\:Progressive
#

Name:           opt-perl-Sub-Exporter-Progressive
Version:        0.001013
Release:        1%{?dist}
Summary:        Only use Sub::Exporter if you need it
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Sub-Exporter-Progressive/
BuildRoot:      /tmp/cpantorpm/Sub-Exporter-Progressive-0.001013-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/F/FR/FREW/Sub-Exporter-Progressive-0.001013.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Sub::Exporter::Progressive) = 0.001013
Requires:       opt-perl
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
L<Sub::Exporter> is an incredibly powerful module, but with that power
comes great responsibility, er- as well as some runtime penalties. This
module is a Sub::Exporter wrapper that will let your users just use
L<Exporter> if all they are doing is picking exports, but use
Sub::Exporter if your users try to use Sub::Exporter's more advanced
features, like renaming exports, if they try to use them.

%prep

%setup  -n Sub-Exporter-Progressive-0.001013
chmod -R u+w %{_builddir}/Sub-Exporter-Progressive-%{version}

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
* Thu Oct 04 2018 Rocks 0.001013-1
- Generated using cpantorpm

