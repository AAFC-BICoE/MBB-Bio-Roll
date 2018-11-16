# This is a  spec file for SSPACE
%global debug_package %{nil}
### define _topdir	 	/home/rpmbuild/rpms/SSPACE
%define name		SSPACE
%define src_name	%{name}-BASIC
%define release		2
%define version 	2.1.1
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}
%define buildroot	%{_topdir}/%{name}-%{version}-root

BuildRoot:	%{buildroot}
Summary: 	SSPACE is a stand-alone program for scaffolding pre-assembled contigs using paired-read data.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-BASIC-%{version}.tar.gz
Patch0: 	%{name}-%{version}-%{release}.patch0
Patch1: 	%{name}-%{version}-%{release}.bin.patch1
Patch2: 	 %{name}-%{version}-%{release}.tools.patch2
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
Prefix: 	%{_prefix}
URL:		https://github.com/nsoranzo/sspace_basic
Group: 		Development/Tools
License:	GNU GPL-2.0
AutoReq:	yes

Provides:	perl(DotLib)

Requires:	perl(DotLib)
Requires:	opt-perl(Exporter)
Requires:	opt-perl(File::Basename)
Requires:	opt-perl(File::Path)
Requires:	opt-perl(FindBin)
Requires:	opt-perl(Getopt::Std)
Requires:	opt-perl(Storable)
Requires:	opt-perl(lib)
Requires:	opt-perl(strict)
Requires:	opt-perl(threads)
Requires:	opt-perl(vars)
Requires:	opt-perl(warnings)

%global __requires_exclude ^perl

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
%setup -q -n sspace_basic-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

%build

%install
mkdir -p %{buildroot}%{installroot}
cp -r bin dotlib tools %{buildroot}%{installroot}
cp SSPACE_Basic_v2.0.pl README %{buildroot}%{installroot}

%files
%defattr(755,root,root)
%{_prefix}
%defattr(644,root,root)
%{_prefix}/README
%{_prefix}/tools/TQS.readme
%{_prefix}/tools/TRIMMING_PAIRED_READS.README

