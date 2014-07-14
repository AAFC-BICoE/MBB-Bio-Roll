# This is a  spec file for art

### define _topdir	 	/home/rpmbuild/rpms/art
%define name		art
%define release		1
%define version 	1.5.0
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	ART is a set of simulation tools to generate synthetic next-generation sequencing reads.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}alllinux64bin_gwtargz.gz
Patch0:         %{name}-%{version}-%{release}.patch0
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://www.niehs.nih.gov/research/resources/software/biostatistics/art/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        Public Domain
AutoReq:	yes

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
%setup -q -n Linux64
%patch -P 0 -p1

%build


%install
mkdir -p %{buildroot}%{installroot}
cp 454_readprofile_art art_454 art_illumina art_SOLiD aln2bed.pl  %{buildroot}%{installroot}
cp -r examples GS_FLX_profile GS_FLX_Titanium_profile Illumina_GAII_profiles SOLiD_profile %{buildroot}%{installroot}


%files
%defattr(755,root,root)
%{installroot}
%defattr(644,root,root)
%{installroot}/examples/testSeq.fa
%{installroot}/GS_FLX_profile/indel_error_profile
%{installroot}/GS_FLX_profile/length_dist
%{installroot}/GS_FLX_profile/qual_1st_profile
%{installroot}/GS_FLX_profile/qual_mc_profile
%{installroot}/GS_FLX_Titanium_profile/indel_error_profile
%{installroot}/GS_FLX_Titanium_profile/length_dist
%{installroot}/GS_FLX_Titanium_profile/qual_1st_profile
%{installroot}/GS_FLX_Titanium_profile/qual_mc_profile
%{installroot}/SOLiD_profile/profile_default
%{installroot}/Illumina_GAII_profiles/Emp100R1.txt
%{installroot}/Illumina_GAII_profiles/Emp100R2.txt
%{installroot}/Illumina_GAII_profiles/Emp36R1.txt
%{installroot}/Illumina_GAII_profiles/Emp36R2.txt
%{installroot}/Illumina_GAII_profiles/Emp44R1.txt
%{installroot}/Illumina_GAII_profiles/Emp44R2.txt
%{installroot}/Illumina_GAII_profiles/Emp50R1.txt
%{installroot}/Illumina_GAII_profiles/Emp50R2.txt
%{installroot}/Illumina_GAII_profiles/Emp75R1.txt
%{installroot}/Illumina_GAII_profiles/Emp75R2.txt
%{installroot}/Illumina_GAII_profiles/EmpR36R1.txt
%{installroot}/Illumina_GAII_profiles/EmpR36R2.txt
%{installroot}/Illumina_GAII_profiles/EmpR44R1.txt
%{installroot}/Illumina_GAII_profiles/EmpR44R2.txt
%{installroot}/Illumina_GAII_profiles/EmpR50R1.txt
%{installroot}/Illumina_GAII_profiles/EmpR50R2.txt
%{installroot}/Illumina_GAII_profiles/EmpR75R1.txt
%{installroot}/Illumina_GAII_profiles/EmpR75R2.txt
