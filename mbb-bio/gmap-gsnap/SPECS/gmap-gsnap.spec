%define name		gmap-gsnap
%define src_name	gmap
%define release		1
%define version 	2018_07_04
%define src_version 	2018-07-04
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	GMAP is a Genomic Mapping and Alignment Program for mRNA and EST Sequences, and GSNAP is a Genomic Short-read Nucleotide Alignment Program.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{src_version}.tar.gz
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>
URL:            http://research-pub.gene.com/gmap
Prefix: 	%{installroot}
Group: 		Bioinformatics/Alignment
License:        Free for non-commercial use. Copyright (c) 2005-2011 Genentech, Inc. Distribution of unmodified package allowed. See COPYING file.
AutoReq:	yes

Requires:	opt-perl
Requires:	opt-perl(File::Copy)
Requires:	opt-perl(Getopt::Long)
Requires:	opt-perl(Getopt::Std)
Requires:	opt-perl(IO::File)
Requires:	opt-perl(warnings)

%global __requires_exclude ^perl

%description
GMAP: A Genomic Mapping and Alignment Program for mRNA and EST Sequences, and
GSNAP: Genomic Short-read Nucleotide Alignment Program.

%prep
%setup -q -n %{src_name}-%{src_version}

%build
./configure --prefix=%{installroot} --with-gmapdb=%{installroot}/share/gmapdb MAX_READLENGTH=1000 PERL="/usr/bin/env perl"
make -j`nproc`

%install
make install DESTDIR=%{buildroot}

#cd src; cp atoiindex cmetindex fastlog.h get-genome gmap gmapindex gmapl gsnap gsnapl iit_dump iit_get iit_store sam_sort snpindex uniqscan uniqscanl %{buildroot}%{installroot}
#cd ../util; cp dbsnp_iit ensembl_genes fa_coords gff3_genes gff3_introns gff3_splicesites gmap_build gmap_compress gmap_process gmap_reassemble gmap_uncompress gtf_genes gtf_introns gtf_splicesites gvf_iit md_coords psl_genes psl_introns psl_splicesites vcf_iit %{buildroot}%{installroot}


%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc COPYING
%doc NOTICE
%doc AUTHORS
%doc ChangeLog
%doc VERSION
%defattr(755,root,root,755)
%{installroot}/bin
