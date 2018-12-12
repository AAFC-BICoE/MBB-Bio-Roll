#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-go-perl
#    Version:           0.15
#    cpantorpm version: 1.08
#    Date:              Wed Dec 12 2018
#    Command:
# /opt/perl/bin/cpantorpm --NO-TESTS --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only GO\:\:Utils
#

Name:           opt-perl-go-perl
Version:        0.15
Release:        1%{?dist}
Summary:        GO Perl
License:        Unknown license: unknown
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/go-perl/
BuildRoot:      /tmp/cpantorpm/go-perl-0.15-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/C/CM/CMUNGALL/go-perl-0.15.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(GO::Basic) = 0.15
Provides:       opt-perl(GO::Handlers::abstract_prolog_writer) = 0.15
Provides:       opt-perl(GO::Handlers::abstract_sql_writer) = 0.15
Provides:       opt-perl(GO::Handlers::base) = 0.15
Provides:       opt-perl(GO::Handlers::go_def) = 0.15
Provides:       opt-perl(GO::Handlers::go_ont) = 0.15
Provides:       opt-perl(GO::Handlers::go_xref) = 0.15
Provides:       opt-perl(GO::Handlers::godb_prestore) = 0.15
Provides:       opt-perl(GO::Handlers::lexanalysis) = 0.15
Provides:       opt-perl(GO::Handlers::lexanalysis2sql) = 0.15
Provides:       opt-perl(GO::Handlers::obj) = 0.15
Provides:       opt-perl(GO::Handlers::obj_storable) = 0.15
Provides:       opt-perl(GO::Handlers::obj_yaml) = 0.15
Provides:       opt-perl(GO::Handlers::obo) = 0.15
Provides:       opt-perl(GO::Handlers::obo_godb_flat) = 0.15
Provides:       opt-perl(GO::Handlers::obo_html) = 0.15
Provides:       opt-perl(GO::Handlers::obo_sxpr) = 0.15
Provides:       opt-perl(GO::Handlers::obo_text) = 0.15
Provides:       opt-perl(GO::Handlers::obo_xml) = 0.15
Provides:       opt-perl(GO::Handlers::owl) = 0.15
Provides:       opt-perl(GO::Handlers::owl_to_obo_text) = 0.15
Provides:       opt-perl(GO::Handlers::pathlist) = 0.15
Provides:       opt-perl(GO::Handlers::prolog) = 0.15
Provides:       opt-perl(GO::Handlers::rdf) = 0.15
Provides:       opt-perl(GO::Handlers::summary) = 0.15
Provides:       opt-perl(GO::Handlers::sxpr) = 0.15
Provides:       opt-perl(GO::Handlers::tbl) = 0.15
Provides:       opt-perl(GO::Handlers::text_html) = 0.15
Provides:       opt-perl(GO::Handlers::xml) = 0.15
Provides:       opt-perl(GO::Handlers::xsl_base) = 0.15
Provides:       opt-perl(GO::IO::Analysis) = 0.15
Provides:       opt-perl(GO::IO::Blast) = 0.15
Provides:       opt-perl(GO::IO::Dotty) = 0.15
Provides:       opt-perl(GO::IO::OBDXML) = 0.15
Provides:       opt-perl(GO::IO::ObanOwl) = 0.15
Provides:       opt-perl(GO::IO::RDFXML) = 0.15
Provides:       opt-perl(GO::IO::XML) = 0.15
Provides:       opt-perl(GO::IO::go_assoc) = 0.15
Provides:       opt-perl(GO::Metadata::Panther) = 0.15
Provides:       opt-perl(GO::Model::Association) = 0.15
Provides:       opt-perl(GO::Model::CrossProduct) = 0.15
Provides:       opt-perl(GO::Model::DB) = 0.15
Provides:       opt-perl(GO::Model::Evidence) = 0.15
Provides:       opt-perl(GO::Model::GeneProduct) = 0.15
Provides:       opt-perl(GO::Model::Graph) = 0.15
Provides:       opt-perl(GO::Model::GraphIterator) = 0.15
Provides:       opt-perl(GO::Model::GraphNodeInstance) = 0.15
Provides:       opt-perl(GO::Model::LogicalDefinition) = 0.15
Provides:       opt-perl(GO::Model::Modification) = 0.15
Provides:       opt-perl(GO::Model::Ontology) = 0.15
Provides:       opt-perl(GO::Model::Path) = 0.15
Provides:       opt-perl(GO::Model::Property) = 0.15
Provides:       opt-perl(GO::Model::Relationship) = 0.15
Provides:       opt-perl(GO::Model::Restriction) = 0.15
Provides:       opt-perl(GO::Model::Root) = 0.15
Provides:       opt-perl(GO::Model::Seq) = 0.15
Provides:       opt-perl(GO::Model::Species) = 0.15
Provides:       opt-perl(GO::Model::Term) = 0.15
Provides:       opt-perl(GO::Model::TreeIterator) = 0.15
Provides:       opt-perl(GO::Model::Xref) = 0.15
Provides:       opt-perl(GO::ObjCache) = 0.15
Provides:       opt-perl(GO::ObjFactory) = 0.15
Provides:       opt-perl(GO::Parser) = 0.15
Provides:       opt-perl(GO::Parsers::ParserEventNames) = 0.15
Provides:       opt-perl(GO::Parsers::base_parser) = 0.15
Provides:       opt-perl(GO::Parsers::generic_tagval_parser) = 0.15
Provides:       opt-perl(GO::Parsers::go_assoc_parser) = 0.15
Provides:       opt-perl(GO::Parsers::go_def_parser) = 0.15
Provides:       opt-perl(GO::Parsers::go_ids_parser) = 0.15
Provides:       opt-perl(GO::Parsers::go_ont_parser) = 0.15
Provides:       opt-perl(GO::Parsers::go_xref_parser) = 0.15
Provides:       opt-perl(GO::Parsers::locuslink_parser) = 0.15
Provides:       opt-perl(GO::Parsers::mesh_parser) = 0.15
Provides:       opt-perl(GO::Parsers::mgi_assoc_parser) = 0.15
Provides:       opt-perl(GO::Parsers::ncbi_taxon_names_parser) = 0.15
Provides:       opt-perl(GO::Parsers::ncbi_taxonomy_parser) = 0.15
Provides:       opt-perl(GO::Parsers::obj_emitter) = 0.15
Provides:       opt-perl(GO::Parsers::obj_storable_parser) = 0.15
Provides:       opt-perl(GO::Parsers::obj_yaml_parser) = 0.15
Provides:       opt-perl(GO::Parsers::obo_parser) = 0.15
Provides:       opt-perl(GO::Parsers::obo_text_parser) = 0.15
Provides:       opt-perl(GO::Parsers::obo_xml_parser) = 0.15
Provides:       opt-perl(GO::Parsers::owl_parser) = 0.15
Provides:       opt-perl(GO::Parsers::references_parser) = 0.15
Provides:       opt-perl(GO::Parsers::refgenomes_parser) = 0.15
Provides:       opt-perl(GO::Parsers::unknown_format_parser) = 0.15
Provides:       opt-perl(GO::Parsers::xrf_abbs_parser) = 0.15
Provides:       opt-perl(GO::Utils) = 0.15
Requires:       opt-perl
Requires:       opt-perl(Data::Dumper)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Data::Dumper)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A perl module

%prep

%setup  -n go-perl-0.15
chmod -R u+w %{_builddir}/go-perl-%{version}

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
* Wed Dec 12 2018 Rocks 0.15-1
- Generated using cpantorpm

