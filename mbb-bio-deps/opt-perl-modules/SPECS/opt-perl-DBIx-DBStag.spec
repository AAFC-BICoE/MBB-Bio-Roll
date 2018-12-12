#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-DBIx-DBStag
#    Version:           0.12
#    cpantorpm version: 1.08
#    Date:              Wed Dec 12 2018
#    Command:
# /opt/perl/bin/cpantorpm --NO-TESTS --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only DBIx\:\:DBStag
#

Name:           opt-perl-DBIx-DBStag
Version:        0.12
Release:        1%{?dist}
Summary:        DBStag
License:        Unknown license: unknown
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DBIx-DBStag/
BuildRoot:      /tmp/cpantorpm/DBIx-DBStag-0.12-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/S/SC/SCAIN/DBIx-DBStag-0.12.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(DBIx::DBStag) = 0.12
Provides:       opt-perl(DBIx::DBStag::Constraint) = 0.12
Provides:       opt-perl(DBIx::DBStag::SQLTemplate) = 0.12
Requires:       opt-perl
Requires:       opt-perl(DBI)
Requires:       opt-perl(Parse::RecDescent)
Requires:       opt-perl(Text::Balanced)
Requires:       opt-perl(XML::Parser::PerlSAX)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(DBI)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(Parse::RecDescent)
BuildRequires:  opt-perl(Text::Balanced)
BuildRequires:  opt-perl(XML::Parser::PerlSAX)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A perl module

%prep

%setup  -n DBIx-DBStag-0.12
chmod -R u+w %{_builddir}/DBIx-DBStag-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS" INSTALLDIRS=site SITEPREFIX=/opt/perl INSTALLSITEARCH=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi INSTALLSITELIB=/opt/perl/lib/site_perl/5.26.0 INSTALLSITEBIN=/opt/perl/bin INSTALLSITESCRIPT=/opt/perl/bin INSTALLSITEMAN1DIR=/opt/perl/man/man1 INSTALLSITEMAN3DIR=/opt/perl/man/man3 INSTALLSCRIPT=/opt/perl/bin
make %{?_smp_mflags}


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
* Wed Dec 12 2018 Rocks 0.12-1
- Generated using cpantorpm

