#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-BioPerl
#    Version:           1.007002
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Bio\:\:Perl
#

Name:           opt-perl-BioPerl
Version:        1.007002
Release:        1%{?dist}
Summary:        Bioinformatics Toolkit
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/BioPerl/
BuildRoot:      /tmp/cpantorpm/BioPerl-1.007002-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/C/CJ/CJFIELDS/BioPerl-1.007002.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Bio::Align::AlignI) = 1.007002
Provides:       opt-perl(Bio::Align::DNAStatistics) = 1.007002
Provides:       opt-perl(Bio::Align::Graphics) = 1.007002
Provides:       opt-perl(Bio::Align::PairwiseStatistics) = 1.007002
Provides:       opt-perl(Bio::Align::ProteinStatistics) = 1.007002
Provides:       opt-perl(Bio::Align::StatisticsI) = 1.007002
Provides:       opt-perl(Bio::Align::Utilities) = 1.007002
Provides:       opt-perl(Bio::AlignIO) = 1.007002
Provides:       opt-perl(Bio::AlignIO::Handler::GenericAlignHandler) = 1.007002
Provides:       opt-perl(Bio::AlignIO::arp) = 1.007002
Provides:       opt-perl(Bio::AlignIO::bl2seq) = 1.007002
Provides:       opt-perl(Bio::AlignIO::clustalw) = 1.007002
Provides:       opt-perl(Bio::AlignIO::emboss) = 1.007002
Provides:       opt-perl(Bio::AlignIO::fasta) = 1.007002
Provides:       opt-perl(Bio::AlignIO::largemultifasta) = 1.007002
Provides:       opt-perl(Bio::AlignIO::maf) = 1.007002
Provides:       opt-perl(Bio::AlignIO::mase) = 1.007002
Provides:       opt-perl(Bio::AlignIO::mega) = 1.007002
Provides:       opt-perl(Bio::AlignIO::meme) = 1.007002
Provides:       opt-perl(Bio::AlignIO::metafasta) = 1.007002
Provides:       opt-perl(Bio::AlignIO::msf) = 1.007002
Provides:       opt-perl(Bio::AlignIO::nexml) = 1.007002
Provides:       opt-perl(Bio::AlignIO::nexus) = 1.007002
Provides:       opt-perl(Bio::AlignIO::pfam) = 1.007002
Provides:       opt-perl(Bio::AlignIO::phylip) = 1.007002
Provides:       opt-perl(Bio::AlignIO::po) = 1.007002
Provides:       opt-perl(Bio::AlignIO::proda) = 1.007002
Provides:       opt-perl(Bio::AlignIO::prodom) = 1.007002
Provides:       opt-perl(Bio::AlignIO::psi) = 1.007002
Provides:       opt-perl(Bio::AlignIO::selex) = 1.007002
Provides:       opt-perl(Bio::AlignIO::stockholm) = 1.007002
Provides:       opt-perl(Bio::AlignIO::xmfa) = 1.007002
Provides:       opt-perl(Bio::AnalysisI) = 1.007002
Provides:       opt-perl(Bio::AnalysisI::JobI) = 1.007002
Provides:       opt-perl(Bio::AnalysisParserI) = 1.007002
Provides:       opt-perl(Bio::AnalysisResultI) = 1.007002
Provides:       opt-perl(Bio::AnnotatableI) = 1.007002
Provides:       opt-perl(Bio::Annotation::AnnotationFactory) = 1.007002
Provides:       opt-perl(Bio::Annotation::Collection) = 1.007002
Provides:       opt-perl(Bio::Annotation::Comment) = 1.007002
Provides:       opt-perl(Bio::Annotation::DBLink) = 1.007002
Provides:       opt-perl(Bio::Annotation::OntologyTerm) = 1.007002
Provides:       opt-perl(Bio::Annotation::Reference) = 1.007002
Provides:       opt-perl(Bio::Annotation::Relation) = 1.007002
Provides:       opt-perl(Bio::Annotation::SimpleValue) = 1.007002
Provides:       opt-perl(Bio::Annotation::StructuredValue) = 1.007002
Provides:       opt-perl(Bio::Annotation::TagTree) = 1.007002
Provides:       opt-perl(Bio::Annotation::Target) = 1.007002
Provides:       opt-perl(Bio::Annotation::Tree) = 1.007002
Provides:       opt-perl(Bio::Annotation::TypeManager) = 1.007002
Provides:       opt-perl(Bio::AnnotationCollectionI) = 1.007002
Provides:       opt-perl(Bio::AnnotationI) = 1.007002
Provides:       opt-perl(Bio::Assembly::Contig) = 1.007002
Provides:       opt-perl(Bio::Assembly::ContigAnalysis) = 1.007002
Provides:       opt-perl(Bio::Assembly::IO) = 1.007002
Provides:       opt-perl(Bio::Assembly::IO::ace) = 1.007002
Provides:       opt-perl(Bio::Assembly::IO::bowtie) = 1.007002
Provides:       opt-perl(Bio::Assembly::IO::maq) = 1.007002
Provides:       opt-perl(Bio::Assembly::IO::phrap) = 1.007002
Provides:       opt-perl(Bio::Assembly::IO::sam) = 1.007002
Provides:       opt-perl(Bio::Assembly::IO::tigr) = 1.007002
Provides:       opt-perl(Bio::Assembly::Scaffold) = 1.007002
Provides:       opt-perl(Bio::Assembly::ScaffoldI) = 1.007002
Provides:       opt-perl(Bio::Assembly::Singlet) = 1.007002
Provides:       opt-perl(Bio::Assembly::Tools::ContigSpectrum) = 1.007002
Provides:       opt-perl(Bio::Cluster::ClusterFactory) = 1.007002
Provides:       opt-perl(Bio::Cluster::FamilyI) = 1.007002
Provides:       opt-perl(Bio::Cluster::SequenceFamily) = 1.007002
Provides:       opt-perl(Bio::Cluster::UniGene) = 1.007002
Provides:       opt-perl(Bio::Cluster::UniGeneI) = 1.007002
Provides:       opt-perl(Bio::ClusterI) = 1.007002
Provides:       opt-perl(Bio::ClusterIO) = 1.007002
Provides:       opt-perl(Bio::ClusterIO::dbsnp) = 1.007002
Provides:       opt-perl(Bio::ClusterIO::unigene) = 1.007002
Provides:       opt-perl(Bio::CodonUsage::IO) = 1.007002
Provides:       opt-perl(Bio::CodonUsage::Table) = 1.007002
Provides:       opt-perl(Bio::DB::Ace) = 1.007002
Provides:       opt-perl(Bio::DB::BioFetch) = 1.007002
Provides:       opt-perl(Bio::DB::CUTG) = 1.007002
Provides:       opt-perl(Bio::DB::DBFetch) = 1.007002
Provides:       opt-perl(Bio::DB::EMBL) = 1.007002
Provides:       opt-perl(Bio::DB::EntrezGene) = 1.007002
Provides:       opt-perl(Bio::DB::Expression) = 1.007002
Provides:       opt-perl(Bio::DB::Expression::geo) = 1.007002
Provides:       opt-perl(Bio::DB::Failover) = 1.007002
Provides:       opt-perl(Bio::DB::Fasta) = 1.007002
Provides:       opt-perl(Bio::DB::Fasta::Subdir) = 1.007002
Provides:       opt-perl(Bio::DB::FileCache) = 1.007002
Provides:       opt-perl(Bio::DB::Flat) = 1.007002
Provides:       opt-perl(Bio::DB::Flat::BDB) = 1.007002
Provides:       opt-perl(Bio::DB::Flat::BDB::embl) = 1.007002
Provides:       opt-perl(Bio::DB::Flat::BDB::fasta) = 1.007002
Provides:       opt-perl(Bio::DB::Flat::BDB::genbank) = 1.007002
Provides:       opt-perl(Bio::DB::Flat::BDB::swiss) = 1.007002
Provides:       opt-perl(Bio::DB::Flat::BinarySearch) = 1.007002
Provides:       opt-perl(Bio::DB::GFF) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::ace) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::berkeleydb) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::berkeleydb::iterator) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::biofetch) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::biofetch_oracle) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::dbi) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::dbi::caching_handle) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::dbi::faux_dbh) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::dbi::iterator) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::dbi::mysql) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::dbi::mysqlace) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::dbi::mysqlcmap) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::dbi::mysqlopt) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::dbi::oracle) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::dbi::oracleace) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::dbi::pg) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::dbi::pg_fts) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::memory) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::memory::feature_serializer) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Adaptor::memory::iterator) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::alignment) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::clone) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::coding) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::gene) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::match) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::none) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::orf) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::processed_transcript) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::so_transcript) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::transcript) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::ucsc_acembly) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::ucsc_ensgene) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::ucsc_genscan) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::ucsc_refgene) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::ucsc_sanger22) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::ucsc_sanger22pseudo) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::ucsc_softberry) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::ucsc_twinscan) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Aggregator::ucsc_unigene) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Featname) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Feature) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::FeatureIterator) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Homol) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::ID_Iterator) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::RelSegment) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Segment) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Typename) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Util::Binning) = 1.007002
Provides:       opt-perl(Bio::DB::GFF::Util::Rearrange) = 1.007002
Provides:       opt-perl(Bio::DB::GenBank) = 1.007002
Provides:       opt-perl(Bio::DB::GenPept) = 1.007002
Provides:       opt-perl(Bio::DB::GenericWebAgent) = 1.007002
Provides:       opt-perl(Bio::DB::HIV) = 1.007002
Provides:       opt-perl(Bio::DB::HIV::HIVAnnotProcessor) = 1.007002
Provides:       opt-perl(Bio::DB::HIV::HIVQueryHelper) = 1.007002
Provides:       opt-perl(Bio::DB::InMemoryCache) = 1.007002
Provides:       opt-perl(Bio::DB::Indexed::Stream) = 1.007002
Provides:       opt-perl(Bio::DB::IndexedBase) = 1.007002
Provides:       opt-perl(Bio::DB::LocationI) = 1.007002
Provides:       opt-perl(Bio::DB::MeSH) = 1.007002
Provides:       opt-perl(Bio::DB::NCBIHelper) = 1.007002
Provides:       opt-perl(Bio::DB::Qual) = 1.007002
Provides:       opt-perl(Bio::DB::Query::GenBank) = 1.007002
Provides:       opt-perl(Bio::DB::Query::HIVQuery) = 1.007002
Provides:       opt-perl(Bio::DB::Query::WebQuery) = 1.007002
Provides:       opt-perl(Bio::DB::QueryI) = 1.007002
Provides:       opt-perl(Bio::DB::RandomAccessI) = 1.007002
Provides:       opt-perl(Bio::DB::RefSeq) = 1.007002
Provides:       opt-perl(Bio::DB::ReferenceI) = 1.007002
Provides:       opt-perl(Bio::DB::Registry) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::NormalizedFeature) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::NormalizedFeatureI) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::NormalizedTableFeatureI) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Segment) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::DBI::Iterator) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::DBI::Pg) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::DBI::SQLite) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::DBI::mysql) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::FeatureFileLoader) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::FeatureIterator) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::GFF2Loader) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::GFF3Loader) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::LoadHelper) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::Loader) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::bdb) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::berkeleydb) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::berkeleydb3) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::berkeleydb::Iterator) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::memory) = 1.007002
Provides:       opt-perl(Bio::DB::SeqFeature::Store::memory::Iterator) = 1.007002
Provides:       opt-perl(Bio::DB::SeqI) = 1.007002
Provides:       opt-perl(Bio::DB::SeqVersion) = 1.007002
Provides:       opt-perl(Bio::DB::SeqVersion::gi) = 1.007002
Provides:       opt-perl(Bio::DB::SwissProt) = 1.007002
Provides:       opt-perl(Bio::DB::TFBS) = 1.007002
Provides:       opt-perl(Bio::DB::TFBS::transfac_pro) = 1.007002
Provides:       opt-perl(Bio::DB::Taxonomy) = 1.007002
Provides:       opt-perl(Bio::DB::Taxonomy::entrez) = 1.007002
Provides:       opt-perl(Bio::DB::Taxonomy::flatfile) = 1.007002
Provides:       opt-perl(Bio::DB::Taxonomy::greengenes) = 1.007002
Provides:       opt-perl(Bio::DB::Taxonomy::list) = 1.007002
Provides:       opt-perl(Bio::DB::Taxonomy::silva) = 1.007002
Provides:       opt-perl(Bio::DB::Taxonomy::sqlite) = 1.007002
Provides:       opt-perl(Bio::DB::Universal) = 1.007002
Provides:       opt-perl(Bio::DB::UpdateableSeqI) = 1.007002
Provides:       opt-perl(Bio::DB::WebDBSeqI) = 1.007002
Provides:       opt-perl(Bio::DBLinkContainerI) = 1.007002
Provides:       opt-perl(Bio::Das::FeatureTypeI) = 1.007002
Provides:       opt-perl(Bio::Das::SegmentI) = 1.007002
Provides:       opt-perl(Bio::DasI) = 1.007002
Provides:       opt-perl(Bio::DescribableI) = 1.007002
Provides:       opt-perl(Bio::Draw::Pictogram) = 1.007002
Provides:       opt-perl(Bio::Event::EventGeneratorI) = 1.007002
Provides:       opt-perl(Bio::Event::EventHandlerI) = 1.007002
Provides:       opt-perl(Bio::Factory::AnalysisI) = 1.007002
Provides:       opt-perl(Bio::Factory::ApplicationFactoryI) = 1.007002
Provides:       opt-perl(Bio::Factory::DriverFactory) = 1.007002
Provides:       opt-perl(Bio::Factory::FTLocationFactory) = 1.007002
Provides:       opt-perl(Bio::Factory::LocationFactoryI) = 1.007002
Provides:       opt-perl(Bio::Factory::MapFactoryI) = 1.007002
Provides:       opt-perl(Bio::Factory::ObjectBuilderI) = 1.007002
Provides:       opt-perl(Bio::Factory::ObjectFactory) = 1.007002
Provides:       opt-perl(Bio::Factory::ObjectFactoryI) = 1.007002
Provides:       opt-perl(Bio::Factory::SeqAnalysisParserFactory) = 1.007002
Provides:       opt-perl(Bio::Factory::SeqAnalysisParserFactoryI) = 1.007002
Provides:       opt-perl(Bio::Factory::SequenceFactoryI) = 1.007002
Provides:       opt-perl(Bio::Factory::SequenceProcessorI) = 1.007002
Provides:       opt-perl(Bio::Factory::SequenceStreamI) = 1.007002
Provides:       opt-perl(Bio::Factory::TreeFactoryI) = 1.007002
Provides:       opt-perl(Bio::FeatureHolderI) = 1.007002
Provides:       opt-perl(Bio::HandlerBaseI) = 1.007002
Provides:       opt-perl(Bio::IdCollectionI) = 1.007002
Provides:       opt-perl(Bio::IdentifiableI) = 1.007002
Provides:       opt-perl(Bio::Index::Abstract) = 1.007002
Provides:       opt-perl(Bio::Index::AbstractSeq) = 1.007002
Provides:       opt-perl(Bio::Index::Blast) = 1.007002
Provides:       opt-perl(Bio::Index::BlastTable) = 1.007002
Provides:       opt-perl(Bio::Index::EMBL) = 1.007002
Provides:       opt-perl(Bio::Index::Fasta) = 1.007002
Provides:       opt-perl(Bio::Index::Fastq) = 1.007002
Provides:       opt-perl(Bio::Index::GenBank) = 1.007002
Provides:       opt-perl(Bio::Index::Hmmer) = 1.007002
Provides:       opt-perl(Bio::Index::Qual) = 1.007002
Provides:       opt-perl(Bio::Index::Stockholm) = 1.007002
Provides:       opt-perl(Bio::Index::SwissPfam) = 1.007002
Provides:       opt-perl(Bio::Index::Swissprot) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::AARange) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::Chain) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::ChainI) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::DNA) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::Exon) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::Gene) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::IO::BioPerl) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::IO::Loader) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::Intron) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::Mutation) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::Mutator) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::Prim_Transcript) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::Range) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::Repeat_Region) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::Repeat_Unit) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::SeqI) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::Transcript) = 1.007002
Provides:       opt-perl(Bio::LiveSeq::Translation) = 1.007002
Provides:       opt-perl(Bio::LocatableSeq) = 1.007002
Provides:       opt-perl(Bio::Location::Atomic) = 1.007002
Provides:       opt-perl(Bio::Location::AvWithinCoordPolicy) = 1.007002
Provides:       opt-perl(Bio::Location::CoordinatePolicyI) = 1.007002
Provides:       opt-perl(Bio::Location::Fuzzy) = 1.007002
Provides:       opt-perl(Bio::Location::FuzzyLocationI) = 1.007002
Provides:       opt-perl(Bio::Location::NarrowestCoordPolicy) = 1.007002
Provides:       opt-perl(Bio::Location::Simple) = 1.007002
Provides:       opt-perl(Bio::Location::Split) = 1.007002
Provides:       opt-perl(Bio::Location::SplitLocationI) = 1.007002
Provides:       opt-perl(Bio::Location::WidestCoordPolicy) = 1.007002
Provides:       opt-perl(Bio::LocationI) = 1.007002
Provides:       opt-perl(Bio::Map::Clone) = 1.007002
Provides:       opt-perl(Bio::Map::Contig) = 1.007002
Provides:       opt-perl(Bio::Map::CytoMap) = 1.007002
Provides:       opt-perl(Bio::Map::CytoMarker) = 1.007002
Provides:       opt-perl(Bio::Map::CytoPosition) = 1.007002
Provides:       opt-perl(Bio::Map::EntityI) = 1.007002
Provides:       opt-perl(Bio::Map::FPCMarker) = 1.007002
Provides:       opt-perl(Bio::Map::Gene) = 1.007002
Provides:       opt-perl(Bio::Map::GeneMap) = 1.007002
Provides:       opt-perl(Bio::Map::GenePosition) = 1.007002
Provides:       opt-perl(Bio::Map::GeneRelative) = 1.007002
Provides:       opt-perl(Bio::Map::LinkageMap) = 1.007002
Provides:       opt-perl(Bio::Map::LinkagePosition) = 1.007002
Provides:       opt-perl(Bio::Map::MapI) = 1.007002
Provides:       opt-perl(Bio::Map::Mappable) = 1.007002
Provides:       opt-perl(Bio::Map::MappableI) = 1.007002
Provides:       opt-perl(Bio::Map::Marker) = 1.007002
Provides:       opt-perl(Bio::Map::MarkerI) = 1.007002
Provides:       opt-perl(Bio::Map::Microsatellite) = 1.007002
Provides:       opt-perl(Bio::Map::OrderedPosition) = 1.007002
Provides:       opt-perl(Bio::Map::OrderedPositionWithDistance) = 1.007002
Provides:       opt-perl(Bio::Map::Physical) = 1.007002
Provides:       opt-perl(Bio::Map::Position) = 1.007002
Provides:       opt-perl(Bio::Map::PositionHandler) = 1.007002
Provides:       opt-perl(Bio::Map::PositionHandlerI) = 1.007002
Provides:       opt-perl(Bio::Map::PositionI) = 1.007002
Provides:       opt-perl(Bio::Map::PositionWithSequence) = 1.007002
Provides:       opt-perl(Bio::Map::Prediction) = 1.007002
Provides:       opt-perl(Bio::Map::Relative) = 1.007002
Provides:       opt-perl(Bio::Map::RelativeI) = 1.007002
Provides:       opt-perl(Bio::Map::SimpleMap) = 1.007002
Provides:       opt-perl(Bio::Map::TranscriptionFactor) = 1.007002
Provides:       opt-perl(Bio::MapIO) = 1.007002
Provides:       opt-perl(Bio::MapIO::fpc) = 1.007002
Provides:       opt-perl(Bio::MapIO::mapmaker) = 1.007002
Provides:       opt-perl(Bio::Matrix::Generic) = 1.007002
Provides:       opt-perl(Bio::Matrix::IO) = 1.007002
Provides:       opt-perl(Bio::Matrix::IO::mlagan) = 1.007002
Provides:       opt-perl(Bio::Matrix::IO::phylip) = 1.007002
Provides:       opt-perl(Bio::Matrix::IO::scoring) = 1.007002
Provides:       opt-perl(Bio::Matrix::MatrixI) = 1.007002
Provides:       opt-perl(Bio::Matrix::Mlagan) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::IO) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::IO::mast) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::IO::masta) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::IO::meme) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::IO::psiblast) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::IO::transfac) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::InstanceSite) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::InstanceSiteI) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::ProtMatrix) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::ProtPsm) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::Psm) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::PsmHeader) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::PsmHeaderI) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::PsmI) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::SiteMatrix) = 1.007002
Provides:       opt-perl(Bio::Matrix::PSM::SiteMatrixI) = 1.007002
Provides:       opt-perl(Bio::Matrix::PhylipDist) = 1.007002
Provides:       opt-perl(Bio::Matrix::Scoring) = 1.007002
Provides:       opt-perl(Bio::MolEvol::CodonModel) = 1.007002
Provides:       opt-perl(Bio::Nexml::Factory) = 1.007002
Provides:       opt-perl(Bio::NexmlIO) = 1.007002
Provides:       opt-perl(Bio::Ontology::DocumentRegistry) = 1.007002
Provides:       opt-perl(Bio::Ontology::GOterm) = 1.007002
Provides:       opt-perl(Bio::Ontology::InterProTerm) = 1.007002
Provides:       opt-perl(Bio::Ontology::OBOEngine) = 1.007002
Provides:       opt-perl(Bio::Ontology::OBOterm) = 1.007002
Provides:       opt-perl(Bio::Ontology::Ontology) = 1.007002
Provides:       opt-perl(Bio::Ontology::OntologyEngineI) = 1.007002
Provides:       opt-perl(Bio::Ontology::OntologyI) = 1.007002
Provides:       opt-perl(Bio::Ontology::OntologyStore) = 1.007002
Provides:       opt-perl(Bio::Ontology::Path) = 1.007002
Provides:       opt-perl(Bio::Ontology::PathI) = 1.007002
Provides:       opt-perl(Bio::Ontology::Relationship) = 1.007002
Provides:       opt-perl(Bio::Ontology::RelationshipFactory) = 1.007002
Provides:       opt-perl(Bio::Ontology::RelationshipI) = 1.007002
Provides:       opt-perl(Bio::Ontology::RelationshipType) = 1.007002
Provides:       opt-perl(Bio::Ontology::SimpleGOEngine::GraphAdaptor) = 1.007002
Provides:       opt-perl(Bio::Ontology::SimpleOntologyEngine) = 1.007002
Provides:       opt-perl(Bio::Ontology::Term) = 1.007002
Provides:       opt-perl(Bio::Ontology::TermFactory) = 1.007002
Provides:       opt-perl(Bio::Ontology::TermI) = 1.007002
Provides:       opt-perl(Bio::OntologyIO) = 1.007002
Provides:       opt-perl(Bio::OntologyIO::Handlers::BaseSAXHandler) = 1.007002
Provides:       opt-perl(Bio::OntologyIO::Handlers::InterProHandler) = 1.007002
Provides:       opt-perl(Bio::OntologyIO::Handlers::InterPro_BioSQL_Handler) = 1.007002
Provides:       opt-perl(Bio::OntologyIO::InterProParser) = 1.007002
Provides:       opt-perl(Bio::OntologyIO::dagflat) = 1.007002
Provides:       opt-perl(Bio::OntologyIO::goflat) = 1.007002
Provides:       opt-perl(Bio::OntologyIO::obo) = 1.007002
Provides:       opt-perl(Bio::OntologyIO::simplehierarchy) = 1.007002
Provides:       opt-perl(Bio::OntologyIO::soflat) = 1.007002
Provides:       opt-perl(Bio::ParameterBaseI) = 1.007002
Provides:       opt-perl(Bio::Perl) = 1.007002
Provides:       opt-perl(Bio::Phenotype::Correlate) = 1.007002
Provides:       opt-perl(Bio::Phenotype::MeSH::Term) = 1.007002
Provides:       opt-perl(Bio::Phenotype::MeSH::Twig) = 1.007002
Provides:       opt-perl(Bio::Phenotype::Measure) = 1.007002
Provides:       opt-perl(Bio::Phenotype::OMIM::MiniMIMentry) = 1.007002
Provides:       opt-perl(Bio::Phenotype::OMIM::OMIMentry) = 1.007002
Provides:       opt-perl(Bio::Phenotype::OMIM::OMIMentryAllelicVariant) = 1.007002
Provides:       opt-perl(Bio::Phenotype::OMIM::OMIMparser) = 1.007002
Provides:       opt-perl(Bio::Phenotype::Phenotype) = 1.007002
Provides:       opt-perl(Bio::Phenotype::PhenotypeI) = 1.007002
Provides:       opt-perl(Bio::PhyloNetwork) = 1.007002
Provides:       opt-perl(Bio::PhyloNetwork::Factory) = 1.007002
Provides:       opt-perl(Bio::PhyloNetwork::FactoryX) = 1.007002
Provides:       opt-perl(Bio::PhyloNetwork::GraphViz) = 1.007002
Provides:       opt-perl(Bio::PhyloNetwork::RandomFactory) = 1.007002
Provides:       opt-perl(Bio::PhyloNetwork::TreeFactory) = 1.007002
Provides:       opt-perl(Bio::PhyloNetwork::TreeFactoryMulti) = 1.007002
Provides:       opt-perl(Bio::PhyloNetwork::TreeFactoryX) = 1.007002
Provides:       opt-perl(Bio::PhyloNetwork::muVector) = 1.007002
Provides:       opt-perl(Bio::PopGen::Genotype) = 1.007002
Provides:       opt-perl(Bio::PopGen::GenotypeI) = 1.007002
Provides:       opt-perl(Bio::PopGen::HtSNP) = 1.007002
Provides:       opt-perl(Bio::PopGen::IO) = 1.007002
Provides:       opt-perl(Bio::PopGen::IO::csv) = 1.007002
Provides:       opt-perl(Bio::PopGen::IO::hapmap) = 1.007002
Provides:       opt-perl(Bio::PopGen::IO::phase) = 1.007002
Provides:       opt-perl(Bio::PopGen::IO::prettybase) = 1.007002
Provides:       opt-perl(Bio::PopGen::Individual) = 1.007002
Provides:       opt-perl(Bio::PopGen::IndividualI) = 1.007002
Provides:       opt-perl(Bio::PopGen::Marker) = 1.007002
Provides:       opt-perl(Bio::PopGen::MarkerI) = 1.007002
Provides:       opt-perl(Bio::PopGen::PopStats) = 1.007002
Provides:       opt-perl(Bio::PopGen::Population) = 1.007002
Provides:       opt-perl(Bio::PopGen::PopulationI) = 1.007002
Provides:       opt-perl(Bio::PopGen::Simulation::Coalescent) = 1.007002
Provides:       opt-perl(Bio::PopGen::Simulation::GeneticDrift) = 1.007002
Provides:       opt-perl(Bio::PopGen::Statistics) = 1.007002
Provides:       opt-perl(Bio::PopGen::TagHaplotype) = 1.007002
Provides:       opt-perl(Bio::PopGen::Utilities) = 1.007002
Provides:       opt-perl(Bio::PrimarySeq) = 1.007002
Provides:       opt-perl(Bio::PrimarySeq::Fasta) = 1.007002
Provides:       opt-perl(Bio::PrimarySeqI) = 1.007002
Provides:       opt-perl(Bio::PullParserI) = 1.007002
Provides:       opt-perl(Bio::Range) = 1.007002
Provides:       opt-perl(Bio::RangeI) = 1.007002
Provides:       opt-perl(Bio::Restriction::Analysis) = 1.007002
Provides:       opt-perl(Bio::Restriction::Enzyme) = 1.007002
Provides:       opt-perl(Bio::Restriction::Enzyme::MultiCut) = 1.007002
Provides:       opt-perl(Bio::Restriction::Enzyme::MultiSite) = 1.007002
Provides:       opt-perl(Bio::Restriction::EnzymeCollection) = 1.007002
Provides:       opt-perl(Bio::Restriction::EnzymeI) = 1.007002
Provides:       opt-perl(Bio::Restriction::IO) = 1.007002
Provides:       opt-perl(Bio::Restriction::IO::bairoch) = 1.007002
Provides:       opt-perl(Bio::Restriction::IO::base) = 1.007002
Provides:       opt-perl(Bio::Restriction::IO::itype2) = 1.007002
Provides:       opt-perl(Bio::Restriction::IO::prototype) = 1.007002
Provides:       opt-perl(Bio::Restriction::IO::withrefm) = 1.007002
Provides:       opt-perl(Bio::Root::Build) = 1.007002
Provides:       opt-perl(Bio::Root::Exception) = 1.007002
Provides:       opt-perl(Bio::Root::HTTPget) = 1.007002
Provides:       opt-perl(Bio::Root::IO) = 1.007002
Provides:       opt-perl(Bio::Root::Root) = 1.007002
Provides:       opt-perl(Bio::Root::RootI) = 1.007002
Provides:       opt-perl(Bio::Root::Storable) = 1.007002
Provides:       opt-perl(Bio::Root::Test) = 1.007002
Provides:       opt-perl(Bio::Root::TestObject) = 1.007002
Provides:       opt-perl(Bio::Root::Utilities) = 1.007002
Provides:       opt-perl(Bio::Root::Version) = 1.007002
Provides:       opt-perl(Bio::Search::BlastStatistics) = 1.007002
Provides:       opt-perl(Bio::Search::BlastUtils) = 1.007002
Provides:       opt-perl(Bio::Search::DatabaseI) = 1.007002
Provides:       opt-perl(Bio::Search::GenericDatabase) = 1.007002
Provides:       opt-perl(Bio::Search::GenericStatistics) = 1.007002
Provides:       opt-perl(Bio::Search::HSP::BlastHSP) = 1.007002
Provides:       opt-perl(Bio::Search::HSP::BlastPullHSP) = 1.007002
Provides:       opt-perl(Bio::Search::HSP::FastaHSP) = 1.007002
Provides:       opt-perl(Bio::Search::HSP::GenericHSP) = 1.007002
Provides:       opt-perl(Bio::Search::HSP::HMMERHSP) = 1.007002
Provides:       opt-perl(Bio::Search::HSP::HSPFactory) = 1.007002
Provides:       opt-perl(Bio::Search::HSP::HSPI) = 1.007002
Provides:       opt-perl(Bio::Search::HSP::HmmpfamHSP) = 1.007002
Provides:       opt-perl(Bio::Search::HSP::ModelHSP) = 1.007002
Provides:       opt-perl(Bio::Search::HSP::PSLHSP) = 1.007002
Provides:       opt-perl(Bio::Search::HSP::PsiBlastHSP) = 1.007002
Provides:       opt-perl(Bio::Search::HSP::PullHSPI) = 1.007002
Provides:       opt-perl(Bio::Search::HSP::WABAHSP) = 1.007002
Provides:       opt-perl(Bio::Search::Hit::BlastHit) = 1.007002
Provides:       opt-perl(Bio::Search::Hit::BlastPullHit) = 1.007002
Provides:       opt-perl(Bio::Search::Hit::Fasta) = 1.007002
Provides:       opt-perl(Bio::Search::Hit::GenericHit) = 1.007002
Provides:       opt-perl(Bio::Search::Hit::HMMERHit) = 1.007002
Provides:       opt-perl(Bio::Search::Hit::HitFactory) = 1.007002
Provides:       opt-perl(Bio::Search::Hit::HitI) = 1.007002
Provides:       opt-perl(Bio::Search::Hit::HmmpfamHit) = 1.007002
Provides:       opt-perl(Bio::Search::Hit::ModelHit) = 1.007002
Provides:       opt-perl(Bio::Search::Hit::PsiBlastHit) = 1.007002
Provides:       opt-perl(Bio::Search::Hit::PullHitI) = 1.007002
Provides:       opt-perl(Bio::Search::Hit::hmmer3Hit) = 1.007002
Provides:       opt-perl(Bio::Search::Iteration::GenericIteration) = 1.007002
Provides:       opt-perl(Bio::Search::Iteration::IterationI) = 1.007002
Provides:       opt-perl(Bio::Search::Processor) = 1.007002
Provides:       opt-perl(Bio::Search::Result::BlastPullResult) = 1.007002
Provides:       opt-perl(Bio::Search::Result::BlastResult) = 1.007002
Provides:       opt-perl(Bio::Search::Result::CrossMatchResult) = 1.007002
Provides:       opt-perl(Bio::Search::Result::GenericResult) = 1.007002
Provides:       opt-perl(Bio::Search::Result::HMMERResult) = 1.007002
Provides:       opt-perl(Bio::Search::Result::HmmpfamResult) = 1.007002
Provides:       opt-perl(Bio::Search::Result::INFERNALResult) = 1.007002
Provides:       opt-perl(Bio::Search::Result::PullResultI) = 1.007002
Provides:       opt-perl(Bio::Search::Result::ResultFactory) = 1.007002
Provides:       opt-perl(Bio::Search::Result::ResultI) = 1.007002
Provides:       opt-perl(Bio::Search::Result::WABAResult) = 1.007002
Provides:       opt-perl(Bio::Search::Result::hmmer3Result) = 1.007002
Provides:       opt-perl(Bio::Search::SearchUtils) = 1.007002
Provides:       opt-perl(Bio::Search::StatisticsI) = 1.007002
Provides:       opt-perl(Bio::Search::Tiling::MapTileUtils) = 1.007002
Provides:       opt-perl(Bio::Search::Tiling::MapTiling) = 1.007002
Provides:       opt-perl(Bio::Search::Tiling::TilingI) = 1.007002
Provides:       opt-perl(Bio::SearchDist) = 1.007002
Provides:       opt-perl(Bio::SearchIO) = 1.007002
Provides:       opt-perl(Bio::SearchIO::EventHandlerI) = 1.007002
Provides:       opt-perl(Bio::SearchIO::FastHitEventBuilder) = 1.007002
Provides:       opt-perl(Bio::SearchIO::IteratedSearchResultEventBuilder) = 1.007002
Provides:       opt-perl(Bio::SearchIO::SearchResultEventBuilder) = 1.007002
Provides:       opt-perl(Bio::SearchIO::SearchWriterI) = 1.007002
Provides:       opt-perl(Bio::SearchIO::Writer::GbrowseGFF) = 1.007002
Provides:       opt-perl(Bio::SearchIO::Writer::HSPTableWriter) = 1.007002
Provides:       opt-perl(Bio::SearchIO::Writer::HTMLResultWriter) = 1.007002
Provides:       opt-perl(Bio::SearchIO::Writer::HitTableWriter) = 1.007002
Provides:       opt-perl(Bio::SearchIO::Writer::ResultTableWriter) = 1.007002
Provides:       opt-perl(Bio::SearchIO::Writer::TextResultWriter) = 1.007002
Provides:       opt-perl(Bio::SearchIO::axt) = 1.007002
Provides:       opt-perl(Bio::SearchIO::blast) = 1.007002
Provides:       opt-perl(Bio::SearchIO::blast_pull) = 1.007002
Provides:       opt-perl(Bio::SearchIO::blasttable) = 1.007002
Provides:       opt-perl(Bio::SearchIO::cross_match) = 1.007002
Provides:       opt-perl(Bio::SearchIO::erpin) = 1.007002
Provides:       opt-perl(Bio::SearchIO::exonerate) = 1.007002
Provides:       opt-perl(Bio::SearchIO::fasta) = 1.007002
Provides:       opt-perl(Bio::SearchIO::gmap_f9) = 1.007002
Provides:       opt-perl(Bio::SearchIO::hmmer) = 1.007002
Provides:       opt-perl(Bio::SearchIO::hmmer2) = 1.007002
Provides:       opt-perl(Bio::SearchIO::hmmer3) = 1.007002
Provides:       opt-perl(Bio::SearchIO::hmmer_pull) = 1.007002
Provides:       opt-perl(Bio::SearchIO::infernal) = 1.007002
Provides:       opt-perl(Bio::SearchIO::megablast) = 1.007002
Provides:       opt-perl(Bio::SearchIO::psl) = 1.007002
Provides:       opt-perl(Bio::SearchIO::rnamotif) = 1.007002
Provides:       opt-perl(Bio::SearchIO::sim4) = 1.007002
Provides:       opt-perl(Bio::SearchIO::waba) = 1.007002
Provides:       opt-perl(Bio::SearchIO::wise) = 1.007002
Provides:       opt-perl(Bio::Seq) = 1.007002
Provides:       opt-perl(Bio::Seq::BaseSeqProcessor) = 1.007002
Provides:       opt-perl(Bio::Seq::EncodedSeq) = 1.007002
Provides:       opt-perl(Bio::Seq::LargeLocatableSeq) = 1.007002
Provides:       opt-perl(Bio::Seq::LargePrimarySeq) = 1.007002
Provides:       opt-perl(Bio::Seq::LargeSeq) = 1.007002
Provides:       opt-perl(Bio::Seq::LargeSeqI) = 1.007002
Provides:       opt-perl(Bio::Seq::Meta) = 1.007002
Provides:       opt-perl(Bio::Seq::Meta::Array) = 1.007002
Provides:       opt-perl(Bio::Seq::MetaI) = 1.007002
Provides:       opt-perl(Bio::Seq::PrimaryQual) = 1.007002
Provides:       opt-perl(Bio::Seq::PrimaryQual::Qual) = 1.007002
Provides:       opt-perl(Bio::Seq::PrimedSeq) = 1.007002
Provides:       opt-perl(Bio::Seq::QualI) = 1.007002
Provides:       opt-perl(Bio::Seq::Quality) = 1.007002
Provides:       opt-perl(Bio::Seq::RichSeq) = 1.007002
Provides:       opt-perl(Bio::Seq::RichSeqI) = 1.007002
Provides:       opt-perl(Bio::Seq::SeqBuilder) = 1.007002
Provides:       opt-perl(Bio::Seq::SeqFactory) = 1.007002
Provides:       opt-perl(Bio::Seq::SeqFastaSpeedFactory) = 1.007002
Provides:       opt-perl(Bio::Seq::SeqWithQuality) = 1.007002
Provides:       opt-perl(Bio::Seq::SequenceTrace) = 1.007002
Provides:       opt-perl(Bio::Seq::SimulatedRead) = 1.007002
Provides:       opt-perl(Bio::Seq::TraceI) = 1.007002
Provides:       opt-perl(Bio::SeqAnalysisParserI) = 1.007002
Provides:       opt-perl(Bio::SeqEvolution::DNAPoint) = 1.007002
Provides:       opt-perl(Bio::SeqEvolution::EvolutionI) = 1.007002
Provides:       opt-perl(Bio::SeqEvolution::Factory) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Amplicon) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::AnnotationAdaptor) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Collection) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::CollectionI) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Computation) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::FeaturePair) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Gene::Exon) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Gene::ExonI) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Gene::GeneStructure) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Gene::GeneStructureI) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Gene::Intron) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Gene::NC_Feature) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Gene::Poly_A_site) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Gene::Promoter) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Gene::Transcript) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Gene::TranscriptI) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Gene::UTR) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Generic) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Lite) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::PositionProxy) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Primer) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::SiRNA::Oligo) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::SiRNA::Pair) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Similarity) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::SimilarityPair) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::SubSeq) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Tools::FeatureNamer) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Tools::IDHandler) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Tools::TypeMapper) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::Tools::Unflattener) = 1.007002
Provides:       opt-perl(Bio::SeqFeature::TypedSeqFeatureI) = 1.007002
Provides:       opt-perl(Bio::SeqFeatureI) = 1.007002
Provides:       opt-perl(Bio::SeqI) = 1.007002
Provides:       opt-perl(Bio::SeqIO) = 1.007002
Provides:       opt-perl(Bio::SeqIO::FTHelper) = 1.007002
Provides:       opt-perl(Bio::SeqIO::Handler::GenericRichSeqHandler) = 1.007002
Provides:       opt-perl(Bio::SeqIO::MultiFile) = 1.007002
Provides:       opt-perl(Bio::SeqIO::abi) = 1.007002
Provides:       opt-perl(Bio::SeqIO::ace) = 1.007002
Provides:       opt-perl(Bio::SeqIO::agave) = 1.007002
Provides:       opt-perl(Bio::SeqIO::alf) = 1.007002
Provides:       opt-perl(Bio::SeqIO::asciitree) = 1.007002
Provides:       opt-perl(Bio::SeqIO::bsml) = 1.007002
Provides:       opt-perl(Bio::SeqIO::bsml_sax) = 1.007002
Provides:       opt-perl(Bio::SeqIO::chadoxml) = 1.007002
Provides:       opt-perl(Bio::SeqIO::chaos) = 1.007002
Provides:       opt-perl(Bio::SeqIO::chaosxml) = 1.007002
Provides:       opt-perl(Bio::SeqIO::ctf) = 1.007002
Provides:       opt-perl(Bio::SeqIO::embl) = 1.007002
Provides:       opt-perl(Bio::SeqIO::embldriver) = 1.007002
Provides:       opt-perl(Bio::SeqIO::entrezgene) = 1.007002
Provides:       opt-perl(Bio::SeqIO::excel) = 1.007002
Provides:       opt-perl(Bio::SeqIO::exp) = 1.007002
Provides:       opt-perl(Bio::SeqIO::fasta) = 1.007002
Provides:       opt-perl(Bio::SeqIO::fastq) = 1.007002
Provides:       opt-perl(Bio::SeqIO::flybase_chadoxml) = 1.007002
Provides:       opt-perl(Bio::SeqIO::game) = 1.007002
Provides:       opt-perl(Bio::SeqIO::game::featHandler) = 1.007002
Provides:       opt-perl(Bio::SeqIO::game::gameHandler) = 1.007002
Provides:       opt-perl(Bio::SeqIO::game::gameSubs) = 1.007002
Provides:       opt-perl(Bio::SeqIO::game::gameWriter) = 1.007002
Provides:       opt-perl(Bio::SeqIO::game::seqHandler) = 1.007002
Provides:       opt-perl(Bio::SeqIO::gbdriver) = 1.007002
Provides:       opt-perl(Bio::SeqIO::gbxml) = 1.007002
Provides:       opt-perl(Bio::SeqIO::gcg) = 1.007002
Provides:       opt-perl(Bio::SeqIO::genbank) = 1.007002
Provides:       opt-perl(Bio::SeqIO::interpro) = 1.007002
Provides:       opt-perl(Bio::SeqIO::kegg) = 1.007002
Provides:       opt-perl(Bio::SeqIO::largefasta) = 1.007002
Provides:       opt-perl(Bio::SeqIO::lasergene) = 1.007002
Provides:       opt-perl(Bio::SeqIO::locuslink) = 1.007002
Provides:       opt-perl(Bio::SeqIO::mbsout) = 1.007002
Provides:       opt-perl(Bio::SeqIO::metafasta) = 1.007002
Provides:       opt-perl(Bio::SeqIO::msout) = 1.007002
Provides:       opt-perl(Bio::SeqIO::nexml) = 1.007002
Provides:       opt-perl(Bio::SeqIO::phd) = 1.007002
Provides:       opt-perl(Bio::SeqIO::pir) = 1.007002
Provides:       opt-perl(Bio::SeqIO::pln) = 1.007002
Provides:       opt-perl(Bio::SeqIO::qual) = 1.007002
Provides:       opt-perl(Bio::SeqIO::raw) = 1.007002
Provides:       opt-perl(Bio::SeqIO::scf) = 1.007002
Provides:       opt-perl(Bio::SeqIO::seqxml) = 1.007002
Provides:       opt-perl(Bio::SeqIO::strider) = 1.007002
Provides:       opt-perl(Bio::SeqIO::swiss) = 1.007002
Provides:       opt-perl(Bio::SeqIO::swissdriver) = 1.007002
Provides:       opt-perl(Bio::SeqIO::tab) = 1.007002
Provides:       opt-perl(Bio::SeqIO::table) = 1.007002
Provides:       opt-perl(Bio::SeqIO::tigr) = 1.007002
Provides:       opt-perl(Bio::SeqIO::tigrxml) = 1.007002
Provides:       opt-perl(Bio::SeqIO::tinyseq) = 1.007002
Provides:       opt-perl(Bio::SeqIO::tinyseq::tinyseqHandler) = 1.007002
Provides:       opt-perl(Bio::SeqIO::ztr) = 1.007002
Provides:       opt-perl(Bio::SeqUtils) = 1.007002
Provides:       opt-perl(Bio::SimpleAlign) = 1.007002
Provides:       opt-perl(Bio::SimpleAnalysisI) = 1.007002
Provides:       opt-perl(Bio::Species) = 1.007002
Provides:       opt-perl(Bio::Structure::Atom) = 1.007002
Provides:       opt-perl(Bio::Structure::Chain) = 1.007002
Provides:       opt-perl(Bio::Structure::Entry) = 1.007002
Provides:       opt-perl(Bio::Structure::IO) = 1.007002
Provides:       opt-perl(Bio::Structure::IO::pdb) = 1.007002
Provides:       opt-perl(Bio::Structure::Model) = 1.007002
Provides:       opt-perl(Bio::Structure::Residue) = 1.007002
Provides:       opt-perl(Bio::Structure::SecStr::DSSP::Res) = 1.007002
Provides:       opt-perl(Bio::Structure::SecStr::STRIDE::Res) = 1.007002
Provides:       opt-perl(Bio::Structure::StructureI) = 1.007002
Provides:       opt-perl(Bio::Symbol::Alphabet) = 1.007002
Provides:       opt-perl(Bio::Symbol::AlphabetI) = 1.007002
Provides:       opt-perl(Bio::Symbol::DNAAlphabet) = 1.007002
Provides:       opt-perl(Bio::Symbol::ProteinAlphabet) = 1.007002
Provides:       opt-perl(Bio::Symbol::Symbol) = 1.007002
Provides:       opt-perl(Bio::Symbol::SymbolI) = 1.007002
Provides:       opt-perl(Bio::Taxon) = 1.007002
Provides:       opt-perl(Bio::Taxonomy) = 1.007002
Provides:       opt-perl(Bio::Taxonomy::FactoryI) = 1.007002
Provides:       opt-perl(Bio::Taxonomy::Node) = 1.007002
Provides:       opt-perl(Bio::Taxonomy::Taxon) = 1.007002
Provides:       opt-perl(Bio::Taxonomy::Tree) = 1.007002
Provides:       opt-perl(Bio::Tools::AlignFactory) = 1.007002
Provides:       opt-perl(Bio::Tools::Alignment::Consed) = 1.007002
Provides:       opt-perl(Bio::Tools::Alignment::Trim) = 1.007002
Provides:       opt-perl(Bio::Tools::AmpliconSearch) = 1.007002
Provides:       opt-perl(Bio::Tools::Analysis::DNA::ESEfinder) = 1.007002
Provides:       opt-perl(Bio::Tools::Analysis::Protein::Domcut) = 1.007002
Provides:       opt-perl(Bio::Tools::Analysis::Protein::ELM) = 1.007002
Provides:       opt-perl(Bio::Tools::Analysis::Protein::GOR4) = 1.007002
Provides:       opt-perl(Bio::Tools::Analysis::Protein::HNN) = 1.007002
Provides:       opt-perl(Bio::Tools::Analysis::Protein::NetPhos) = 1.007002
Provides:       opt-perl(Bio::Tools::Analysis::Protein::Scansite) = 1.007002
Provides:       opt-perl(Bio::Tools::Analysis::Protein::Sopma) = 1.007002
Provides:       opt-perl(Bio::Tools::Analysis::SimpleAnalysisBase) = 1.007002
Provides:       opt-perl(Bio::Tools::AnalysisResult) = 1.007002
Provides:       opt-perl(Bio::Tools::Blat) = 1.007002
Provides:       opt-perl(Bio::Tools::CodonTable) = 1.007002
Provides:       opt-perl(Bio::Tools::Coil) = 1.007002
Provides:       opt-perl(Bio::Tools::ECnumber) = 1.007002
Provides:       opt-perl(Bio::Tools::EMBOSS::Palindrome) = 1.007002
Provides:       opt-perl(Bio::Tools::EPCR) = 1.007002
Provides:       opt-perl(Bio::Tools::ESTScan) = 1.007002
Provides:       opt-perl(Bio::Tools::Eponine) = 1.007002
Provides:       opt-perl(Bio::Tools::Est2Genome) = 1.007002
Provides:       opt-perl(Bio::Tools::Fgenesh) = 1.007002
Provides:       opt-perl(Bio::Tools::FootPrinter) = 1.007002
Provides:       opt-perl(Bio::Tools::GFF) = 1.007002
Provides:       opt-perl(Bio::Tools::Gel) = 1.007002
Provides:       opt-perl(Bio::Tools::Geneid) = 1.007002
Provides:       opt-perl(Bio::Tools::Genemark) = 1.007002
Provides:       opt-perl(Bio::Tools::Genewise) = 1.007002
Provides:       opt-perl(Bio::Tools::Genomewise) = 1.007002
Provides:       opt-perl(Bio::Tools::Genscan) = 1.007002
Provides:       opt-perl(Bio::Tools::Glimmer) = 1.007002
Provides:       opt-perl(Bio::Tools::Grail) = 1.007002
Provides:       opt-perl(Bio::Tools::GuessSeqFormat) = 1.007002
Provides:       opt-perl(Bio::Tools::HMMER::Domain) = 1.007002
Provides:       opt-perl(Bio::Tools::HMMER::Results) = 1.007002
Provides:       opt-perl(Bio::Tools::HMMER::Set) = 1.007002
Provides:       opt-perl(Bio::Tools::Hmmpfam) = 1.007002
Provides:       opt-perl(Bio::Tools::IUPAC) = 1.007002
Provides:       opt-perl(Bio::Tools::Lucy) = 1.007002
Provides:       opt-perl(Bio::Tools::MZEF) = 1.007002
Provides:       opt-perl(Bio::Tools::Match) = 1.007002
Provides:       opt-perl(Bio::Tools::OddCodes) = 1.007002
Provides:       opt-perl(Bio::Tools::Phylo::Gerp) = 1.007002
Provides:       opt-perl(Bio::Tools::Phylo::Gumby) = 1.007002
Provides:       opt-perl(Bio::Tools::Phylo::Molphy) = 1.007002
Provides:       opt-perl(Bio::Tools::Phylo::Molphy::Result) = 1.007002
Provides:       opt-perl(Bio::Tools::Phylo::Phylip::ProtDist) = 1.007002
Provides:       opt-perl(Bio::Tools::Prediction::Exon) = 1.007002
Provides:       opt-perl(Bio::Tools::Prediction::Gene) = 1.007002
Provides:       opt-perl(Bio::Tools::Primer3) = 1.007002
Provides:       opt-perl(Bio::Tools::Primer::Assessor::Base) = 1.007002
Provides:       opt-perl(Bio::Tools::Primer::AssessorI) = 1.007002
Provides:       opt-perl(Bio::Tools::Primer::Feature) = 1.007002
Provides:       opt-perl(Bio::Tools::Primer::Pair) = 1.007002
Provides:       opt-perl(Bio::Tools::Prints) = 1.007002
Provides:       opt-perl(Bio::Tools::Profile) = 1.007002
Provides:       opt-perl(Bio::Tools::Promoterwise) = 1.007002
Provides:       opt-perl(Bio::Tools::PrositeScan) = 1.007002
Provides:       opt-perl(Bio::Tools::Protparam) = 1.007002
Provides:       opt-perl(Bio::Tools::Pseudowise) = 1.007002
Provides:       opt-perl(Bio::Tools::QRNA) = 1.007002
Provides:       opt-perl(Bio::Tools::RandomDistFunctions) = 1.007002
Provides:       opt-perl(Bio::Tools::RepeatMasker) = 1.007002
Provides:       opt-perl(Bio::Tools::Run::GenericParameters) = 1.007002
Provides:       opt-perl(Bio::Tools::Run::ParametersI) = 1.007002
Provides:       opt-perl(Bio::Tools::Run::RemoteBlast) = 1.007002
Provides:       opt-perl(Bio::Tools::Seg) = 1.007002
Provides:       opt-perl(Bio::Tools::SeqPattern) = 1.007002
Provides:       opt-perl(Bio::Tools::SeqPattern::Backtranslate) = 1.007002
Provides:       opt-perl(Bio::Tools::SeqStats) = 1.007002
Provides:       opt-perl(Bio::Tools::SeqWords) = 1.007002
Provides:       opt-perl(Bio::Tools::SiRNA) = 1.007002
Provides:       opt-perl(Bio::Tools::SiRNA::Ruleset::saigo) = 1.007002
Provides:       opt-perl(Bio::Tools::SiRNA::Ruleset::tuschl) = 1.007002
Provides:       opt-perl(Bio::Tools::Sigcleave) = 1.007002
Provides:       opt-perl(Bio::Tools::Signalp) = 1.007002
Provides:       opt-perl(Bio::Tools::Signalp::ExtendedSignalp) = 1.007002
Provides:       opt-perl(Bio::Tools::Sim4::Exon) = 1.007002
Provides:       opt-perl(Bio::Tools::Sim4::Results) = 1.007002
Provides:       opt-perl(Bio::Tools::Spidey::Exon) = 1.007002
Provides:       opt-perl(Bio::Tools::Spidey::Results) = 1.007002
Provides:       opt-perl(Bio::Tools::TandemRepeatsFinder) = 1.007002
Provides:       opt-perl(Bio::Tools::TargetP) = 1.007002
Provides:       opt-perl(Bio::Tools::Tmhmm) = 1.007002
Provides:       opt-perl(Bio::Tools::dpAlign) = 1.007002
Provides:       opt-perl(Bio::Tools::ipcress) = 1.007002
Provides:       opt-perl(Bio::Tools::isPcr) = 1.007002
Provides:       opt-perl(Bio::Tools::pICalculator) = 1.007002
Provides:       opt-perl(Bio::Tools::pSW) = 1.007002
Provides:       opt-perl(Bio::Tools::tRNAscanSE) = 1.007002
Provides:       opt-perl(Bio::Tree::AlleleNode) = 1.007002
Provides:       opt-perl(Bio::Tree::AnnotatableNode) = 1.007002
Provides:       opt-perl(Bio::Tree::Compatible) = 1.007002
Provides:       opt-perl(Bio::Tree::DistanceFactory) = 1.007002
Provides:       opt-perl(Bio::Tree::Draw::Cladogram) = 1.007002
Provides:       opt-perl(Bio::Tree::Node) = 1.007002
Provides:       opt-perl(Bio::Tree::NodeI) = 1.007002
Provides:       opt-perl(Bio::Tree::NodeNHX) = 1.007002
Provides:       opt-perl(Bio::Tree::RandomFactory) = 1.007002
Provides:       opt-perl(Bio::Tree::Statistics) = 1.007002
Provides:       opt-perl(Bio::Tree::Tree) = 1.007002
Provides:       opt-perl(Bio::Tree::TreeFunctionsI) = 1.007002
Provides:       opt-perl(Bio::Tree::TreeI) = 1.007002
Provides:       opt-perl(Bio::TreeIO) = 1.007002
Provides:       opt-perl(Bio::TreeIO::NewickParser) = 1.007002
Provides:       opt-perl(Bio::TreeIO::TreeEventBuilder) = 1.007002
Provides:       opt-perl(Bio::TreeIO::cluster) = 1.007002
Provides:       opt-perl(Bio::TreeIO::lintree) = 1.007002
Provides:       opt-perl(Bio::TreeIO::newick) = 1.007002
Provides:       opt-perl(Bio::TreeIO::nexml) = 1.007002
Provides:       opt-perl(Bio::TreeIO::nexus) = 1.007002
Provides:       opt-perl(Bio::TreeIO::nhx) = 1.007002
Provides:       opt-perl(Bio::TreeIO::pag) = 1.007002
Provides:       opt-perl(Bio::TreeIO::phyloxml) = 1.007002
Provides:       opt-perl(Bio::TreeIO::svggraph) = 1.007002
Provides:       opt-perl(Bio::TreeIO::tabtree) = 1.007002
Provides:       opt-perl(Bio::UpdateableSeqI) = 1.007002
Provides:       opt-perl(Bio::Variation::AAChange) = 1.007002
Provides:       opt-perl(Bio::Variation::AAReverseMutate) = 1.007002
Provides:       opt-perl(Bio::Variation::Allele) = 1.007002
Provides:       opt-perl(Bio::Variation::DNAMutation) = 1.007002
Provides:       opt-perl(Bio::Variation::IO) = 1.007002
Provides:       opt-perl(Bio::Variation::IO::flat) = 1.007002
Provides:       opt-perl(Bio::Variation::IO::xml) = 1.007002
Provides:       opt-perl(Bio::Variation::RNAChange) = 1.007002
Provides:       opt-perl(Bio::Variation::SNP) = 1.007002
Provides:       opt-perl(Bio::Variation::SeqDiff) = 1.007002
Provides:       opt-perl(Bio::Variation::VariantI) = 1.007002
Provides:       opt-perl(Bio::WebAgent) = 1.007002
Provides:       opt-perl(FeatureStore) = 1.007002
Requires:       opt-perl
Requires:       opt-perl(IO::String)
Requires:       opt-perl(Scalar::Util)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(IO::String)
BuildRequires:  opt-perl(Scalar::Util)
BuildRequires:  opt-perl(Test::Most)
BuildRequires:  opt-perl(URI::Escape)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A perl module

%prep

%setup  -n BioPerl-1.007002
chmod -R u+w %{_builddir}/BioPerl-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Build.PL optimize="$RPM_OPT_FLAGS" --installdirs site --install_path arch=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi --install_path lib=/opt/perl/lib/site_perl/5.26.0 --install_path script=/opt/perl/bin --install_path bin=/opt/perl/bin --install_path libdoc=/opt/perl/man/man3 --install_path bindoc=/opt/perl/man/man1
./Build

#
# This is included here instead of in the 'check' section because
# older versions of rpmbuild (such as the one distributed with RHEL5)
# do not do 'check' by default.
#

if [ -z "$RPMBUILD_NOTESTS" ]; then
   ./Build test
fi

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
/opt/perl/bin/*
/opt/perl/lib/site_perl/5.26.0/*
/opt/perl/man/man1/*
/opt/perl/man/man3/*

%changelog
* Thu Oct 04 2018 Rocks 1.007002-1
- Generated using cpantorpm

