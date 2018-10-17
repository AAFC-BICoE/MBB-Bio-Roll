#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Regexp-Common
#    Version:           2017060201
#    cpantorpm version: 1.08
#    Date:              Wed Oct 17 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Regexp\:\:Common
#

Name:           opt-perl-Regexp-Common
Version:        2017060201
Release:        1%{?dist}
Summary:        Provide commonly requested regular expressions
License:        MIT, MIT, BSD, Unknown license: artistic_1, Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Regexp-Common/
BuildRoot:      /tmp/cpantorpm/Regexp-Common-2017060201-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/A/AB/ABIGAIL/Regexp-Common-2017060201.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Regexp::Common) = 2017060201
Provides:       opt-perl(Regexp::Common::CC) = 2017060201
Provides:       opt-perl(Regexp::Common::Entry) = 2017060201
Provides:       opt-perl(Regexp::Common::SEN) = 2017060201
Provides:       opt-perl(Regexp::Common::URI) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::RFC1035) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::RFC1738) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::RFC1808) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::RFC2384) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::RFC2396) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::RFC2806) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::fax) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::file) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::ftp) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::gopher) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::http) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::news) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::pop) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::prospero) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::tel) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::telnet) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::tv) = 2017060201
Provides:       opt-perl(Regexp::Common::URI::wais) = 2017060201
Provides:       opt-perl(Regexp::Common::_support) = 2017060201
Provides:       opt-perl(Regexp::Common::balanced) = 2017060201
Provides:       opt-perl(Regexp::Common::comment) = 2017060201
Provides:       opt-perl(Regexp::Common::delimited) = 2017060201
Provides:       opt-perl(Regexp::Common::lingua) = 2017060201
Provides:       opt-perl(Regexp::Common::list) = 2017060201
Provides:       opt-perl(Regexp::Common::net) = 2017060201
Provides:       opt-perl(Regexp::Common::number) = 2017060201
Provides:       opt-perl(Regexp::Common::profanity) = 2017060201
Provides:       opt-perl(Regexp::Common::whitespace) = 2017060201
Provides:       opt-perl(Regexp::Common::zip) = 2017060201
Requires:       opt-perl
Requires:       opt-perl(Config)
Requires:       opt-perl(strict)
Requires:       opt-perl(vars)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Config)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(vars)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
By default, this module exports a single hash (%RE) that stores or
generates commonly needed regular expressions (see L<"List of available
patterns">).

%prep

%setup  -n Regexp-Common-2017060201
chmod -R u+w %{_builddir}/Regexp-Common-%{version}

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
* Wed Oct 17 2018 Rocks 2017060201-1
- Generated using cpantorpm

