#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Bio-ASN1-EntrezGene
#    Version:           1.73
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Bio\:\:ASN1\:\:EntrezGene
#

Name:           opt-perl-Bio-ASN1-EntrezGene
Version:        1.73
Release:        1%{?dist}
Summary:        Regular expression-based Perl Parser for NCBI Entrez Gene.
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Bio-ASN1-EntrezGene/
BuildRoot:      /tmp/cpantorpm/Bio-ASN1-EntrezGene-1.73-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/C/CJ/CJFIELDS/Bio-ASN1-EntrezGene-1.73.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Bio::ASN1::EntrezGene) = 1.73
Provides:       opt-perl(Bio::ASN1::EntrezGene::Indexer) = 1.73
Provides:       opt-perl(Bio::ASN1::Sequence) = 1.73
Provides:       opt-perl(Bio::ASN1::Sequence::Indexer) = 1.73
Provides:       opt-perl(Bio::SeqIO::entrezgene) = 1.73
Requires:       opt-perl
Requires:       opt-perl(Bio::Annotation::Comment)
Requires:       opt-perl(Bio::Annotation::DBLink)
Requires:       opt-perl(Bio::Annotation::OntologyTerm)
Requires:       opt-perl(Bio::Annotation::Reference)
Requires:       opt-perl(Bio::Annotation::SimpleValue)
Requires:       opt-perl(Bio::Cluster::SequenceFamily)
Requires:       opt-perl(Bio::Index::AbstractSeq)
Requires:       opt-perl(Bio::Ontology::Term)
Requires:       opt-perl(Bio::Seq)
Requires:       opt-perl(Bio::SeqFeature::Gene::Exon)
Requires:       opt-perl(Bio::SeqFeature::Gene::GeneStructure)
Requires:       opt-perl(Bio::SeqFeature::Gene::Transcript)
Requires:       opt-perl(Bio::SeqFeature::Generic)
Requires:       opt-perl(Bio::SeqIO)
Requires:       opt-perl(Bio::Species)
Requires:       opt-perl(Carp)
Requires:       opt-perl(Data::Dumper)
Requires:       opt-perl(base)
Requires:       opt-perl(parent)
Requires:       opt-perl(strict)
Requires:       opt-perl(utf8)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Bio::Annotation::Comment)
BuildRequires:  opt-perl(Bio::Annotation::DBLink)
BuildRequires:  opt-perl(Bio::Annotation::OntologyTerm)
BuildRequires:  opt-perl(Bio::Annotation::Reference)
BuildRequires:  opt-perl(Bio::Annotation::SimpleValue)
BuildRequires:  opt-perl(Bio::Cluster::SequenceFamily)
BuildRequires:  opt-perl(Bio::Index::AbstractSeq)
BuildRequires:  opt-perl(Bio::Ontology::Term)
BuildRequires:  opt-perl(Bio::Seq)
BuildRequires:  opt-perl(Bio::SeqFeature::Gene::Exon)
BuildRequires:  opt-perl(Bio::SeqFeature::Gene::GeneStructure)
BuildRequires:  opt-perl(Bio::SeqFeature::Gene::Transcript)
BuildRequires:  opt-perl(Bio::SeqFeature::Generic)
BuildRequires:  opt-perl(Bio::SeqIO)
BuildRequires:  opt-perl(Bio::Species)
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(Data::Dumper)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(base)
BuildRequires:  opt-perl(parent)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(utf8)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Bio::ASN1::EntrezGene is a regular expression-based Perl Parser for NCBI
Entrez Gene genome databases
(L<http://www.ncbi.nih.gov/entrez/query.fcgi?db=gene>). It parses an
ASN.1-formatted Entrez Gene record and returns a data structure that
contains all data items from the gene record.

%prep

%setup  -n Bio-ASN1-EntrezGene-1.73
chmod -R u+w %{_builddir}/Bio-ASN1-EntrezGene-%{version}

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
%perl_sitelib/Bio/ASN1
/opt/perl/man/man3/Bio::ASN1*

%changelog
* Thu Oct 04 2018 Rocks 1.73-1
- Generated using cpantorpm

