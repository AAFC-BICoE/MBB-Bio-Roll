#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-DBD-SQLite
#    Version:           1.58
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only DBD\:\:SQLite
#

Name:           opt-perl-DBD-SQLite
Version:        1.58
Release:        1%{?dist}
Summary:        Self Contained SQLite RDBMS in a DBI Driver
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/DBD-SQLite/
BuildRoot:      /tmp/cpantorpm/DBD-SQLite-1.58-inst
BuildArch:      %{_arch}
Source0:        http://search.cpan.org/authors/id/authors/id/I/IS/ISHIGAKI/DBD-SQLite-1.58.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(DBD::SQLite) = 1.58
Provides:       opt-perl(DBD::SQLite::Constants) = 1.58
Provides:       opt-perl(DBD::SQLite::VirtualTable) = 1.58
Provides:       opt-perl(DBD::SQLite::VirtualTable::Cursor) = 1.58
Provides:       opt-perl(DBD::SQLite::VirtualTable::FileContent) = 1.58
Provides:       opt-perl(DBD::SQLite::VirtualTable::FileContent::Cursor) = 1.58
Provides:       opt-perl(DBD::SQLite::VirtualTable::PerlData) = 1.58
Provides:       opt-perl(DBD::SQLite::VirtualTable::PerlData::Cursor) = 1.58
Requires:       opt-perl
Requires:       opt-perl(Scalar::Util)
Requires:       opt-perl(Tie::Hash)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Scalar::Util)
BuildRequires:  opt-perl(Tie::Hash)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
SQLite is a public domain file-based relational database engine that you
can find at L<http://www.sqlite.org/>.

%prep

%setup  -n DBD-SQLite-1.58
chmod -R u+w %{_builddir}/DBD-SQLite-%{version}

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
/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi/*
/opt/perl/man/man3/*

%changelog
* Thu Oct 04 2018 Rocks 1.58-1
- Generated using cpantorpm

