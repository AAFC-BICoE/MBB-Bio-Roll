# This is a  spec file ifor artemis

### define _topdir	 	/home/rpmbuild/rpms/artemis
%define name		artemis
%define release		1
%define version 	15
%define installroot 	/opt/bio/%{name}

%define __jar_repack %{nil}

BuildRoot:	%{buildroot}
Summary: 	Artemis is a free genome browser and annotation tool. ACT is a free tool for displaying pairwise comparisons between two or more DNA sequences. DNAPlotter can be used to generate images of circular and linear DNA maps to display regions and features of interest.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}.tar.gz
Patch0:         %{name}-%{version}-%{release}.patch0
Patch1:         %{name}-%{version}-%{release}.patch1
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://www.sanger.ac.uk/resources/software/artemis/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPL|http://www.sanger.ac.uk/resources/software/artemis	
AutoReq:	yes

%description
Artemis is a free genome browser and annotation tool that allows visualisation
of sequence features, next generation data and the results of analyses within
the context of the sequence, and also its six-frame translation. Artemis is
writte in Java, and is available for UNIX, Macintosh and Windows systems. It can
read EMBL and GENBANK database entries or sequence in FASTA, indexed FASTA or
raw format. Other sequence features can be in EMBL, GENBANK or GFF format.  
ACT is a free tool for displaying pairwise comparisons between two or more DNA
sequences. It can be used to identify and analyse regions of similarity and
difference between genomes and to explore conservation of synteny, in the
context of the entire sequences and their annotation.
DNAPlotter can be used to generate images of circular and linear DNA maps to
display regions and features of interest. The images can be inserted into a
document or printed out directly. As this uses Artemis it can read in the common
file formats EMBL, GenBank and GFF3.

%prep
%setup -q -n artemis
%patch -P 0 -p1
%patch -P 1 -p1

%build


%install
mkdir -p %{buildroot}%{installroot}
cp -r * %{buildroot}%{installroot}

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/act
%{installroot}/art
%{installroot}/dnaplotter
%{installroot}/etc/gene_builder
%{installroot}/etc/go_associations.pl
%{installroot}/etc/results_to_netscape
%{installroot}/etc/run_blastn
%{installroot}/etc/run_blastn.sanger
%{installroot}/etc/run_blastp
%{installroot}/etc/run_blastp.sanger
%{installroot}/etc/run_blastp.sanger.linux
%{installroot}/etc/run_blastx
%{installroot}/etc/run_blastx.sanger
%{installroot}/etc/run_clustalx
%{installroot}/etc/run_clustalx.sanger
%{installroot}/etc/run_fasta
%{installroot}/etc/run_fasta.sanger
%{installroot}/etc/run_fasta.sanger.linux
%{installroot}/etc/run_hth
%{installroot}/etc/run_jalview
%{installroot}/etc/run_netblastp
%{installroot}/etc/run_pepstats
%{installroot}/etc/run_sigcleave
%{installroot}/etc/run_smart
%{installroot}/etc/run_tblastn
%{installroot}/etc/run_tblastx
%{installroot}/etc/run_tblastx.sanger
%{installroot}/etc/writedb_entry
