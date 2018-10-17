#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Eval-Closure
#    Version:           0.14
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Eval\:\:Closure
#

Name:           opt-perl-Eval-Closure
Version:        0.14
Release:        1%{?dist}
Summary:        safely and cleanly create closures via string eval
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Eval-Closure/
BuildRoot:      /tmp/cpantorpm/Eval-Closure-0.14-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/D/DO/DOY/Eval-Closure-0.14.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Eval::Closure) = 0.14
Requires:       opt-perl
Requires:       opt-perl(Carp)
Requires:       opt-perl(Exporter)
Requires:       opt-perl(Scalar::Util)
Requires:       opt-perl(constant)
Requires:       opt-perl(overload)
Requires:       opt-perl(strict)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(Exporter)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(Scalar::Util)
BuildRequires:  opt-perl(constant)
BuildRequires:  opt-perl(overload)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
String eval is often used for dynamic code generation. For instance,
Moose uses it heavily, to generate inlined versions of accessors and
constructors, which speeds code up at runtime by a significant amount.
String eval is not without its issues however - it's difficult to control
the scope it's used in (which determines which variables are in scope
inside the eval), and it's easy to miss compilation errors, since eval
catches them and sticks them in $@ instead.

%prep

%setup  -n Eval-Closure-0.14
chmod -R u+w %{_builddir}/Eval-Closure-%{version}

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
* Thu Oct 04 2018 Rocks 0.14-1
- Generated using cpantorpm

