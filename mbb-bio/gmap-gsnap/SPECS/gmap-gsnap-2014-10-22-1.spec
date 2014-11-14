# This is a  spec file for gmap-gsnap

%define name		gmap-gsnap
%define release		1
%define version 	2014.10.22
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	GMAP is a Genomic Mapping and Alignment Program for mRNA and EST Sequences, and GSNAP is a Genomic Short-read Nucleotide Alignment Program.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-2014-10-22.tar.gz
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://research-pub.gene.com/gmap
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        Free for non-commercial use. Copyright (c) 2005-2011 Genentech, Inc. Distribution of unmodified package allowed. See COPYING file.
AutoReq:	yes

%description
GMAP: A Genomic Mapping and Alignment Program for mRNA and EST Sequences, and
GSNAP: Genomic Short-read Nucleotide Alignment Program.

%prep
%setup -q -n gmap-2014-10-22

%build
./configure --prefix=%{installroot} --with-gmapdb=%{installroot}/share/gmapdb MAX_READLENGTH=500 PERL="/usr/bin/env perl"
make 

%install
mkdir -p %{buildroot}%{installroot}
cp COPYING NOTICE %{buildroot}%{installroot}
cd src; cp atoiindex cmetindex fastlog.h get-genome gmap gmapindex gmapl gsnap gsnapl iit_dump iit_get iit_store sam_sort snpindex uniqscan uniqscanl %{buildroot}%{installroot}
cd ../util; cp dbsnp_iit ensembl_genes fa_coords gff3_genes gff3_introns gff3_splicesites gmap_build gmap_compress gmap_process gmap_reassemble gmap_uncompress gtf_genes gtf_introns gtf_splicesites gvf_iit md_coords psl_genes psl_introns psl_splicesites vcf_iit %{buildroot}%{installroot}


%files
%defattr(755,root,root,755)
%{installroot}
%defattr(644,root,root,755)
%{installroot}/COPYING
%{installroot}/NOTICE
