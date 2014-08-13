# This is a sample spec file for wget

### define _topdir	 	/home/rpmbuild/rpms/%{name}
%define name			STAR
%define src_name		STAR
%define release		1
%define version 	2.3.0e
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	STAR aligns RNA-seq reads to a reference genome using uncompressed suffix arrays
License: 		GPL3
Name: 			%{name}
Version: 		%{version}
Packager:   Glen Newton <glen.newton@agr.gc.ca>
Release: 		%{release}
Source: 		%{src_name}-%{version}.tgz
Patch0:         %{name}_%{version}.patch
Prefix: 		/opt/bio
Group: 			Applications/BioInformatics/Alignment
URL:			https://code.google.com/p/rna-star/
AutoReq:		yes

%description
http://bioinformatics.oxfordjournals.org/content/29/1/15
Motivation: Accurate alignment of high-throughput RNA-seq data is a
challenging and yet unsolved problem because of the non-contiguous
transcript structure, relatively short read lengths and constantly
increasing throughput of the sequencing technologies. Currently
available RNA-seq aligners suffer from high mapping error rates, low
mapping speed, read length limitation and mapping biases.  

Results: To align our large (>80 billon reads) ENCODE Transcriptome
RNA-seq dataset, we developed the Spliced Transcripts Alignment to a
Reference (STAR) software based on a previously undescribed RNA-seq
alignment algorithm that uses sequential maximum mappable seed search
in uncompressed suffix arrays followed by seed clustering and
stitching procedure. STAR outperforms other aligners by a factor of
>50 in mapping speed, aligning to the human genome 550 million 2 × 76
bp paired-end reads per hour on a modest 12-core server, while at the
same time improving alignment sensitivity and precision. In addition
to unbiased de novo detection of canonical junctions, STAR can
discover non-canonical splices and chimeric (fusion) transcripts, and
is also capable of mapping full-length RNA sequences. Using Roche 454
sequencing of reverse transcription polymerase chain reaction
amplicons, we experimentally validated 1960 novel intergenic splice
junctions with an 80–90% success rate, corroborating the high
precision of the STAR mapping strategy.  

%prep
%setup -q -n STAR_2.3.0e
%patch -P 0 -p1

%build
make  -pipe --jobs=`nproc` prefix=%{installroot}

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp STAR $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root,755)
%{installroot}
