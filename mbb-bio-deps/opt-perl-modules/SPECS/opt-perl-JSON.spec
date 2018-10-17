#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-JSON
#    Version:           2.97001
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only JSON
#

Name:           opt-perl-JSON
Version:        2.97001
Release:        1%{?dist}
Summary:        JSON (JavaScript Object Notation) encoder/decoder
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/JSON/
BuildRoot:      /tmp/cpantorpm/JSON-2.97001-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/I/IS/ISHIGAKI/JSON-2.97001.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(JSON) = 2.97001
Provides:       opt-perl(JSON::Backend::PP) = 2.97001
Requires:       opt-perl
Requires:       opt-perl(Test::More)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(Test::More)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module is a thin wrapper for L<JSON::XS>-compatible modules with a few
additional features. All the backend modules convert a Perl data structure
to a JSON text as of RFC4627 (which we know is obsolete but we still stick
to; see below for an option to support part of RFC7159) and vice versa.
This module uses L<JSON::XS> by default, and when JSON::XS is not
available, this module falls back on L<JSON::PP>, which is in the Perl core
since 5.14. If JSON::PP is not available either, this module then falls
back on JSON::backportPP (which is actually JSON::PP in a different .pm
file) bundled in the same distribution as this module. You can also
explicitly specify to use L<Cpanel::JSON::XS>, a fork of JSON::XS by Reini
Urban.

%prep

%setup  -n JSON-2.97001
chmod -R u+w %{_builddir}/JSON-%{version}

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
* Thu Oct 04 2018 Rocks 2.97001-1
- Generated using cpantorpm

