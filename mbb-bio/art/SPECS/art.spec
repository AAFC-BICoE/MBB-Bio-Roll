# This is a  spec file for art

### define _topdir	 	/home/rpmbuild/rpms/art
%define name		art
%define release		1
%define version 	2016.06.05
%define nameversion	mountrainier
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	ART is a set of simulation tools to generate synthetic next-generation sequencing reads.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}src%{nameversion}%{version}linux.tgz
Patch0: 	env-perl.patch
Packager:	Iyad Kandalaft <iyad.kandalaft@agr.gc.ca>
URL:            http://www.niehs.nih.gov/research/resources/software/biostatistics/art/
Prefix: 	%{installroot}
Group: 		Bioinformatics
License:        Public Domain
AutoReq:	yes
Requires:	opt-perl
Requires:	opt-perl(FileHandle)
Requires:	opt-perl(strict)

%global __requires_exclude ^perl


%description
ART is a set of simulation tools to generate synthetic next-generation
sequencing reads. ART simulates sequencing reads by mimicking real sequencing
process with empirical error models or quality profiles summarized from large
recalibrated sequencing data. ART can also simulate reads using user own read
error model or quality profiles. ART supports simulation of single-end,
paired-end/mate-pair reads of three major commercial next-generation sequencing
platforms: Illumina's Solexa, Roche's 454 and Applied Biosystems' SOLiD. ART can
be used to test or benchmark a variety of method or tools for next-generation
sequencing data analysis, including read alignment, de novo assembly, SNP and
structure variation discovery. ART was used as a primary tool for the simulation
study of the 1000 Genomes Project. ART is implemented in C++ with optimized
algorithms and is highly efficient in read simulation. ART outputs reads in the
FASTQ format, and alignments in the ALN format. ART can also generate alignments
in the SAM alignment or UCSC BED file format.

%prep
%setup -q -n art_src_MountRainier_Linux
%patch0 -p1
%build
./configure --prefix=%{installroot}
make -j 8

%install
make install DESTDIR=%{buildroot}

cp -r 454_profiles Illumina_profiles SOLiD_profiles %{buildroot}%{installroot}
cp -r examples %{buildroot}%{installroot}

%files
%defattr(755,root,root,755)
%{installroot}/bin
%defattr(644,root,root,755)
%dir %{installroot}
%{installroot}/*_profiles
%{installroot}/examples
