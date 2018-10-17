#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-namespace-autoclean
#    Version:           0.28
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only namespace\:\:autoclean
#

Name:           opt-perl-namespace-autoclean
Version:        0.28
Release:        1%{?dist}
Summary:        Keep imports out of your namespace
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/namespace-autoclean/
BuildRoot:      /tmp/cpantorpm/namespace-autoclean-0.28-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/E/ET/ETHER/namespace-autoclean-0.28.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(namespace::autoclean) = 0.28
Requires:       opt-perl
Requires:       opt-perl(List::Util)
Requires:       opt-perl(Sub::Identify)
Requires:       opt-perl(strict)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(List::Util)
BuildRequires:  opt-perl(Sub::Identify)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
When you import a function into a Perl package, it will naturally also be
available as a method.

%prep

%setup  -n namespace-autoclean-0.28
chmod -R u+w %{_builddir}/namespace-autoclean-%{version}

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
* Thu Oct 04 2018 Rocks 0.28-1
- Generated using cpantorpm

