
%global debug_package %{nil}
%define name		trinity2
%define release		1
%define version 	2.0.2
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	RNA-Seq De novo Assembly
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	trinityrnaseq-%{version}.tar.bz2
Packager:	Glen Newton <glen.newton@grc.gc.ca>
URL:            http://trinityrnaseq.github.io/
Prefix: 	/opt/bio
Group: 		Applications/BioInformatics/Assembler
License:        Open Source, MIT-like
#AutoReq:	yes
AutoReq:	no
Provides: /Users/min/projects/dao/dao
Provides: /software/bin/python
Provides: perl(CanvasXpress::Line)
Provides: perl(Bio::AlignIO
Provides: perl(Bio::Assembly::IO
Provides: perl(Bio::Coordinate::Pair
Provides: perl(Bio::DB::GFF::Util::Rearrange
Provides: perl(Bio::DB::SeqFeature::Store)
Provides: perl(Bio::Location::Simple)
Provides: perl(Bio::Root::Version)
Provides: perl(Bio::SearchIO)
Provides: perl(Bio::SeqFeature::Generic)
Provides: perl(Bio::SeqIO)
Provides: perl(Bio::Tools::CodonTable)
Provides: perl(Bio::Tools::GuessSeqFormat)
Provides: perl(Bio::TreeIO)

%description
Trinity, developed at the Broad Institute and the Hebrew University of Jerusalem, represents a novel method for the efficient and robust de novo reconstruction of transcriptomes from RNA-seq data. Trinity combines three independent software modules: Inchworm, Chrysalis, and Butterfly, applied sequentially to process large volumes of RNA-seq reads. Trinity partitions the sequence data into many individual de Bruijn graphs, each representing the transcriptional complexity at at a given gene or locus, and then processes each graph independently to extract full-length splicing isoforms and to tease apart transcripts derived from paralogous genes.

%prep
cat ../SOURCES/trinityrnaseq-2.0.2.tar.bz2.xa? > ../SOURCES/trinityrnaseq-2.0.2.tar.bz2

%setup -qn trinityrnaseq-2.0.2

%build
sed -i  's@#!/usr/local/bin/perl@#!/bin/env perl@' ./PerlLib/GFF_maker.pm
sed -i  's@#!/usr/local/bin/perl@#!/bin/env perl@' ./PerlLib/CDNA/Splice_graph_assembler.pm
sed -i  's@#!/usr/local/bin/perl@#!/bin/env perl@' ./PerlLib/CDNA/PASA_alignment_assembler.pm
sed -i  's@#!/usr/local/bin/perl@#!/bin/env perl@' ./PerlLib/CDNA/Alternative_splice_comparer.pm
sed -i  's@#!/usr/local/bin/perl@#!/bin/env perl@' ./PerlLib/CDNA/Genome_based_cDNA_assembler.pm
sed -i  's@#!/usr/local/bin/perl@#!/bin/env perl@' ./PerlLib/CDNA/CDNA_alignment.pm
sed -i  's@#!/usr/local/bin/perl@#!/bin/env perl@' ./PerlLib/CDNA/Genome_based_cDNA_graph_assembler.pm
sed -i  's@#!/usr/local/bin/perl@#!/bin/env perl@' ./PerlLib/Longest_orf.pm
sed -i  's@#!/usr/local/bin/perl@#!/bin/env perl@' ./PerlLib/TiedHash.pm
sed -i  's@#!/usr/local/bin/perl -w@#!/bin/env perl@' ./PerlLib/Fasta_reader.pm
sed -i  's@#!/usr/local/bin/perl@#!/bin/env perl@' ./PerlLib/Gene_obj_indexer.pm
sed -i  's@#!/usr/local/bin/perl@#!/bin/env perl@' ./PerlLib/GFF3_utils.pm
sed -i  's@#!/usr/local/bin/perl@#!/bin/env perl@' ./PerlLib/overlapping_nucs.ph
make -pipe --jobs=`nproc`
make -pipe --jobs=`nproc` plugins
#make -pipe --jobs=`nproc` testall
#make -pipe --jobs=`nproc` testclean
#rm trinity-plugins/rsem-1.2.19/sam/misc/._*.py

rm -rf trinity-plugins


%install
mkdir -p %{buildroot}%{installroot}
cp -r * %{buildroot}%{installroot}

%files 
%defattr(755,root,root)
%{installroot}

# make all files in the bin directory executable in post section
%post 
chmod +x %{installroot}/Trinity %{installroot}/util/support_scripts %{installroot}/util/misc
