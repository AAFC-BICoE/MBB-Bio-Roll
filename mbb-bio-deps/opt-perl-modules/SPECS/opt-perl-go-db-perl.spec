#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-go-db-perl
#    Version:           0.04
#    cpantorpm version: 1.08
#    Date:              Wed Dec 12 2018
#    Command:
# /opt/perl/bin/cpantorpm --vers 0.04 --NO-TESTS --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only GO\:\:AppHandle
#

Name:           opt-perl-go-db-perl
Version:        0.04
Release:        1%{?dist}
Summary:        GO-DB Perl
License:        Unknown license: unknown
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/go-db-perl/
BuildRoot:      /tmp/cpantorpm/go-db-perl-0.04-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/S/SJ/SJCARBON/go-db-perl-0.04.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(GO) = 0.04
Provides:       opt-perl(GO::Admin) = 0.04
Provides:       opt-perl(GO::AppHandle) = 0.04
Provides:       opt-perl(GO::AppHandles::AppHandleAbstractSqlImpl) = 0.04
Provides:       opt-perl(GO::AppHandles::AppHandleCWrapper) = 0.04
Provides:       opt-perl(GO::AppHandles::AppHandleCachingImpl) = 0.04
Provides:       opt-perl(GO::AppHandles::AppHandleChadoSqlImpl) = 0.04
Provides:       opt-perl(GO::AppHandles::AppHandlePgImpl) = 0.04
Provides:       opt-perl(GO::AppHandles::AppHandleSqlImpl) = 0.04
Provides:       opt-perl(GO::DebugUtils) = 0.04
Provides:       opt-perl(GO::Handlers::db) = 0.04
Provides:       opt-perl(GO::Handlers::genericdb) = 0.04
Provides:       opt-perl(GO::Handlers::godb) = 0.04
Provides:       opt-perl(GO::Reasoner) = 0.04
Provides:       opt-perl(GO::SqlWrapper) = 0.04
Provides:       opt-perl(GO::Tango) = 0.04
Provides:       opt-perl(GO::TestHarness) = 0.04
Provides:       opt-perl(TermC) = 0.04
Provides:       opt-perl(Wrapper) = 0.04
Requires:       opt-perl
Requires:       opt-perl(Bio::Seq)
Requires:       opt-perl(Carp)
Requires:       opt-perl(DBI)
Requires:       opt-perl(Data::Stag)
Requires:       opt-perl(Digest::MD5)
Requires:       opt-perl(Set::Scalar)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Bio::Seq)
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(DBI)
BuildRequires:  opt-perl(Data::Stag)
BuildRequires:  opt-perl(Digest::MD5)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(Set::Scalar)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A perl module

%prep

%setup  -n go-db-perl-0.04
chmod -R u+w %{_builddir}/go-db-perl-%{version}

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
/opt/perl/lib/site_perl/5.26.0/*
/opt/perl/man/man3/*

%changelog
* Wed Dec 12 2018 Rocks 0.04-1
- Generated using cpantorpm

