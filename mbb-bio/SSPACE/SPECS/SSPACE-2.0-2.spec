# This is a  spec file for SSPACE
%global debug_package %{nil}
### define _topdir	 	/home/rpmbuild/rpms/SSPACE
%define name		SSPACE
%define release		2
%define version 	2.0
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	SSPACE is a stand-alone program for scaffolding pre-assembled contigs using paired-read data.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-BASIC-%{version}_linux-x86_64.zip
Patch0:         %{name}-%{version}-%{release}.patch0
Patch1:         %{name}-%{version}-%{release}.bin.patch1
Patch2:         %{name}-%{version}-%{release}.tools.patch2
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
Prefix: 	/opt/bio
URL:		http://www.baseclear.com/landingpages/basetools-a-wide-range-of-bioinformatics-solutions/sspacev12/
Group: 		Development/Tools
License:        GNU GPL
AutoReq:	yes

%description
SSPACE is a stand-alone program for scaffolding pre-assembled contigs using
paired-read data. It is unique in offering the possibility to manually control
the scaffolding process. By using the distance information of paired-end and/or
matepair data, SSPACE is able to assess the order, distance and orientation of
your contigs and combine them into scaffolds. Currently we offer this as a
command-line tool in Perl. The input data is given by pre-assembled contig
sequences (FASTA) and NGS paired-read data (FASTA or FASTQ). The final scaffolds
are provided in FASTA format.
SSPACE has shown excellent performance on various datasets. The results have
been published in the high-impact journal Bioinformatics (2011, vol. 27(4), pag.
578-9), but the method is also frequently cited in other papers.

%prep
%setup -q -n SSPACE-BASIC-2.0_linux-x86_64
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

%build

%install
mkdir -p %{buildroot}%{installroot}
cp -r bin bowtie dotlib tools %{buildroot}%{installroot}
cp SSPACE_Basic_v2.0.pl README %{buildroot}%{installroot}

%files
%defattr(755,root,root)
%{installroot}
%defattr(644,root,root)
%{installroot}/README
%{installroot}/tools/TQS.readme
%{installroot}/tools/TRIMMING_PAIRED_READS.README
%{installroot}/bowtie/VERSION
