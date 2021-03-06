#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Test2-Plugin-NoWarnings
#    Version:           0.06
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Test2\:\:Plugin\:\:NoWarnings
#

Name:           opt-perl-Test2-Plugin-NoWarnings
Version:        0.06
Release:        1%{?dist}
Summary:        Fail if tests warn
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test2-Plugin-NoWarnings/
BuildRoot:      /tmp/cpantorpm/Test2-Plugin-NoWarnings-0.06-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/D/DR/DROLSKY/Test2-Plugin-NoWarnings-0.06.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Test2::Event::Warning) = 0.06
Provides:       opt-perl(Test2::Plugin::NoWarnings) = 0.06
Requires:       opt-perl
Requires:       opt-perl(Carp)
Requires:       opt-perl(Test2::API)
Requires:       opt-perl(Test2::Event)
Requires:       opt-perl(Test2::Util::HashBase)
Requires:       opt-perl(parent)
Requires:       opt-perl(strict)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(Test2::API)
BuildRequires:  opt-perl(Test2::Event)
BuildRequires:  opt-perl(Test2::Util::HashBase)
BuildRequires:  opt-perl(parent)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Loading this plugin causes your tests to fail if there any warnings while
they run. Each warning generates a new failing test and the warning content
is outputted via diag.

%prep

%setup  -n Test2-Plugin-NoWarnings-0.06
chmod -R u+w %{_builddir}/Test2-Plugin-NoWarnings-%{version}

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
* Thu Oct 04 2018 Rocks 0.06-1
- Generated using cpantorpm

