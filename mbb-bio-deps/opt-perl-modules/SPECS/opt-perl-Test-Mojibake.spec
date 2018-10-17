#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Test-Mojibake
#    Version:           1.3
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Test\:\:Mojibake
#

Name:           opt-perl-Test-Mojibake
Version:        1.3
Release:        1%{?dist}
Summary:        check your source for encoding misbehavior.
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Mojibake/
BuildRoot:      /tmp/cpantorpm/Test-Mojibake-1.3-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/S/SY/SYP/Test-Mojibake-1.3.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Test::Mojibake) = 1.3
Requires:       opt-perl
Requires:       opt-perl(File::Spec::Functions)
Requires:       opt-perl(Pod::Usage)
Requires:       opt-perl(Test::Builder)
Requires:       opt-perl(bytes)
Requires:       opt-perl(integer)
Requires:       opt-perl(strict)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(File::Spec::Functions)
BuildRequires:  opt-perl(Pod::Usage)
BuildRequires:  opt-perl(Test::Builder)
BuildRequires:  opt-perl(bytes)
BuildRequires:  opt-perl(integer)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Many modern text editors automatically save files using UTF-8 codification,
however, L<perl> interpreter does not expects it by default. Whereas
this does not represent a big deal on (most) backend-oriented programs, Web
framework (L<Catalyst|http://www.catalystframework.org/>,
L<Mojolicious|http://mojolicio.us/>) based applications will suffer of
so-called L<Mojibake|http://en.wikipedia.org/wiki/Mojibake> (lit.
"unintelligible sequence of characters").

%prep

%setup  -n Test-Mojibake-1.3
chmod -R u+w %{_builddir}/Test-Mojibake-%{version}

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
/opt/perl/bin/*
/opt/perl/lib/site_perl/5.26.0/*
/opt/perl/man/man1/*
/opt/perl/man/man3/*

%changelog
* Thu Oct 04 2018 Rocks 1.3-1
- Generated using cpantorpm

