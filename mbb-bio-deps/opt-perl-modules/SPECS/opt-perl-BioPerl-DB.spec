#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-BioPerl-DB
#    Version:           1.006900
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --NO-TESTS --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Bio\:\:DB\:\:BioDB
#

Name:           opt-perl-BioPerl-DB
Version:        1.006900
Release:        1%{?dist}
Summary:        BioPerl-DB - package for biological databases
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/BioPerl-DB/
BuildRoot:      /tmp/cpantorpm/BioPerl-DB-1.006900-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/C/CJ/CJFIELDS/BioPerl-DB-1.006900.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Bio::BioEntry) = 1.006900
Provides:       opt-perl(Bio::DB::BioDB) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::AnnotationCollectionAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::BaseDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::BasePersistenceAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::BioNamespaceAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::BiosequenceAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::ClusterAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::CommentAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::DBAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::DBLinkAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::LocationAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::MultiDB) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::OBDA) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::OntologyAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::Oracle::AnnotationCollectionAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::Oracle::BasePersistenceAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::Oracle::BiosequenceAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::Oracle::PathAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::Oracle::SpeciesAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::Oracle::TermAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::PathAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::Pg::AnnotationCollectionAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::Pg::BasePersistenceAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::Pg::BiosequenceAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::Pg::PathAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::Pg::SpeciesAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::Pg::TermAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::PrimarySeqAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::ReferenceAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::RelationshipAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::SeqAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::SeqFeatureAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::SimpleValueAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::SpeciesAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::TermAdaptor) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::mysql::AnnotationCollectionAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::mysql::BasePersistenceAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::mysql::BiosequenceAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::mysql::PathAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::mysql::SpeciesAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::BioSQL::mysql::TermAdaptorDriver) = 1.006900
Provides:       opt-perl(Bio::DB::CacheServer::SeqDB) = 1.006900
Provides:       opt-perl(Bio::DB::DBAdaptorI) = 1.006900
Provides:       opt-perl(Bio::DB::DBContextI) = 1.006900
Provides:       opt-perl(Bio::DB::DBD) = 1.006900
Provides:       opt-perl(Bio::DB::DBI) = 1.006900
Provides:       opt-perl(Bio::DB::DBI::Oracle) = 1.006900
Provides:       opt-perl(Bio::DB::DBI::Pg) = 1.006900
Provides:       opt-perl(Bio::DB::DBI::Transaction) = 1.006900
Provides:       opt-perl(Bio::DB::DBI::TransactionListener) = 1.006900
Provides:       opt-perl(Bio::DB::DBI::base) = 1.006900
Provides:       opt-perl(Bio::DB::DBI::mysql) = 1.006900
Provides:       opt-perl(Bio::DB::EasyArgv) = 1.006900
Provides:       opt-perl(Bio::DB::PersistenceAdaptorI) = 1.006900
Provides:       opt-perl(Bio::DB::Persistent::BioNamespace) = 1.006900
Provides:       opt-perl(Bio::DB::Persistent::ObjectRellMapperI) = 1.006900
Provides:       opt-perl(Bio::DB::Persistent::PersistentObject) = 1.006900
Provides:       opt-perl(Bio::DB::Persistent::PersistentObjectFactory) = 1.006900
Provides:       opt-perl(Bio::DB::Persistent::PrimarySeq) = 1.006900
Provides:       opt-perl(Bio::DB::Persistent::Seq) = 1.006900
Provides:       opt-perl(Bio::DB::Persistent::SeqFeature) = 1.006900
Provides:       opt-perl(Bio::DB::PersistentObjectI) = 1.006900
Provides:       opt-perl(Bio::DB::Query::AbstractQuery) = 1.006900
Provides:       opt-perl(Bio::DB::Query::BioQuery) = 1.006900
Provides:       opt-perl(Bio::DB::Query::DBQueryResult) = 1.006900
Provides:       opt-perl(Bio::DB::Query::PrebuiltResult) = 1.006900
Provides:       opt-perl(Bio::DB::Query::QueryConstraint) = 1.006900
Provides:       opt-perl(Bio::DB::Query::QueryResultI) = 1.006900
Provides:       opt-perl(Bio::DB::Query::SqlGenerator) = 1.006900
Provides:       opt-perl(Bio::DB::Query::SqlQuery) = 1.006900
Provides:       opt-perl(Bio::DB::SimpleDBContext) = 1.006900
Requires:       opt-perl
Requires:       opt-perl(DBI)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(DBI)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A perl module

%prep

%setup  -n BioPerl-DB-1.006900
chmod -R u+w %{_builddir}/BioPerl-DB-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Build.PL optimize="$RPM_OPT_FLAGS" --installdirs site --install_path arch=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi --install_path lib=/opt/perl/lib/site_perl/5.26.0 --install_path script=/opt/perl/bin --install_path bin=/opt/perl/bin --install_path libdoc=/opt/perl/man/man3 --install_path bindoc=/opt/perl/man/man1
./Build


%install

rm -rf $RPM_BUILD_ROOT
./Build pure_install destdir=$RPM_BUILD_ROOT create_packlist=0
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
* Thu Oct 04 2018 Rocks 1.006900-1
- Generated using cpantorpm

