#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-DBI
#    Version:           1.641
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only DBI
#

Name:           opt-perl-DBI
Version:        1.641
Release:        1%{?dist}
Summary:        Database independent interface for Perl
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DBI/
BuildRoot:      /tmp/cpantorpm/DBI-1.641-inst
BuildArch:      %{_arch}
Source0:        http://search.cpan.org/authors/id/authors/id/T/TI/TIMB/DBI-1.641.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Bundle::DBI) = 12.008696
Provides:       opt-perl(DBD::DBM) = 0.08
Provides:       opt-perl(DBD::DBM::Statement) = 1.641
Provides:       opt-perl(DBD::DBM::Table) = 1.641
Provides:       opt-perl(DBD::DBM::db) = 1.641
Provides:       opt-perl(DBD::DBM::dr) = 1.641
Provides:       opt-perl(DBD::DBM::st) = 1.641
Provides:       opt-perl(DBD::ExampleP) = 12.014311
Provides:       opt-perl(DBD::File) = 0.44
Provides:       opt-perl(DBD::File::DataSource::File) = 1.641
Provides:       opt-perl(DBD::File::DataSource::Stream) = 1.641
Provides:       opt-perl(DBD::File::Statement) = 1.641
Provides:       opt-perl(DBD::File::Table) = 1.641
Provides:       opt-perl(DBD::File::TableSource::FileSystem) = 1.641
Provides:       opt-perl(DBD::File::db) = 1.641
Provides:       opt-perl(DBD::File::dr) = 1.641
Provides:       opt-perl(DBD::File::st) = 1.641
Provides:       opt-perl(DBD::Gofer) = 0.015327
Provides:       opt-perl(DBD::Gofer::Policy::Base) = 0.010088
Provides:       opt-perl(DBD::Gofer::Policy::classic) = 0.010088
Provides:       opt-perl(DBD::Gofer::Policy::pedantic) = 0.010088
Provides:       opt-perl(DBD::Gofer::Policy::rush) = 0.010088
Provides:       opt-perl(DBD::Gofer::Transport::Base) = 0.014121
Provides:       opt-perl(DBD::Gofer::Transport::corostream) = 1.641
Provides:       opt-perl(DBD::Gofer::Transport::null) = 0.010088
Provides:       opt-perl(DBD::Gofer::Transport::pipeone) = 0.010088
Provides:       opt-perl(DBD::Gofer::Transport::stream) = 0.014599
Provides:       opt-perl(DBD::Mem) = 0.001
Provides:       opt-perl(DBD::Mem::DataSource) = 1.641
Provides:       opt-perl(DBD::Mem::Statement) = 1.641
Provides:       opt-perl(DBD::Mem::Table) = 1.641
Provides:       opt-perl(DBD::Mem::db) = 1.641
Provides:       opt-perl(DBD::Mem::dr) = 1.641
Provides:       opt-perl(DBD::Mem::st) = 1.641
Provides:       opt-perl(DBD::NullP) = 12.014715
Provides:       opt-perl(DBD::Proxy) = 0.2004
Provides:       opt-perl(DBD::Proxy::db) = 1.641
Provides:       opt-perl(DBD::Proxy::dr) = 1.641
Provides:       opt-perl(DBD::Proxy::st) = 1.641
Provides:       opt-perl(DBD::Sponge) = 12.010003
Provides:       opt-perl(DBDI) = 1.641
Provides:       opt-perl(DBI) = 1.641
Provides:       opt-perl(DBI::Const::GetInfo::ANSI) = 2.008697
Provides:       opt-perl(DBI::Const::GetInfo::ODBC) = 2.011374
Provides:       opt-perl(DBI::Const::GetInfoReturn) = 2.008697
Provides:       opt-perl(DBI::Const::GetInfoType) = 2.008697
Provides:       opt-perl(DBI::DBD) = 12.015129
Provides:       opt-perl(DBI::DBD::Metadata) = 2.014214
Provides:       opt-perl(DBI::DBD::SqlEngine) = 0.06
Provides:       opt-perl(DBI::DBD::SqlEngine::DataSource) = 1.641
Provides:       opt-perl(DBI::DBD::SqlEngine::Statement) = 1.641
Provides:       opt-perl(DBI::DBD::SqlEngine::Table) = 1.641
Provides:       opt-perl(DBI::DBD::SqlEngine::TableSource) = 1.641
Provides:       opt-perl(DBI::DBD::SqlEngine::TieMeta) = 1.641
Provides:       opt-perl(DBI::DBD::SqlEngine::TieTables) = 1.641
Provides:       opt-perl(DBI::DBD::SqlEngine::db) = 1.641
Provides:       opt-perl(DBI::DBD::SqlEngine::dr) = 1.641
Provides:       opt-perl(DBI::DBD::SqlEngine::st) = 1.641
Provides:       opt-perl(DBI::Gofer::Execute) = 0.014283
Provides:       opt-perl(DBI::Gofer::Request) = 0.012537
Provides:       opt-perl(DBI::Gofer::Response) = 0.011566
Provides:       opt-perl(DBI::Gofer::Serializer::Base) = 0.009950
Provides:       opt-perl(DBI::Gofer::Serializer::DataDumper) = 0.009950
Provides:       opt-perl(DBI::Gofer::Serializer::Storable) = 0.015586
Provides:       opt-perl(DBI::Gofer::Transport::Base) = 0.012537
Provides:       opt-perl(DBI::Gofer::Transport::pipeone) = 0.012537
Provides:       opt-perl(DBI::Gofer::Transport::stream) = 0.012537
Provides:       opt-perl(DBI::Profile) = 2.015065
Provides:       opt-perl(DBI::ProfileData) = 2.010008
Provides:       opt-perl(DBI::ProfileDumper) = 2.015325
Provides:       opt-perl(DBI::ProfileDumper::Apache) = 2.014121
Provides:       opt-perl(DBI::ProfileSubs) = 0.009396
Provides:       opt-perl(DBI::ProxyServer) = 0.3005
Provides:       opt-perl(DBI::ProxyServer::db) = 1.641
Provides:       opt-perl(DBI::ProxyServer::dr) = 1.641
Provides:       opt-perl(DBI::ProxyServer::st) = 1.641
Provides:       opt-perl(DBI::SQL::Nano) = 1.015544
Provides:       opt-perl(DBI::SQL::Nano::Statement_) = 1.641
Provides:       opt-perl(DBI::SQL::Nano::Table_) = 1.641
Provides:       opt-perl(DBI::Util::CacheMemory) = 0.010315
Provides:       opt-perl(DBI::Util::_accessor) = 0.009479
Provides:       opt-perl(DBI::common) = 1.641
Requires:       opt-perl
BuildRequires:  opt-perl
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The DBI is a database access module for the Perl programming language. It
defines a set of methods, variables, and conventions that provide a
consistent database interface, independent of the actual database being
used.

%prep

%setup  -n DBI-1.641
chmod -R u+w %{_builddir}/DBI-%{version}

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
/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi/*
/opt/perl/man/man1/*
/opt/perl/man/man3/*

%changelog
* Thu Oct 04 2018 Rocks 1.641-1
- Generated using cpantorpm

