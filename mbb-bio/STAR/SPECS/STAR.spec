### define _topdir	 	/home/rpmbuild/rpms/%{name}
%define name		STAR
%define release		1
%define version 	2.5.0b
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		STAR aligns RNA-seq reads to a reference genome using uncompressed suffix arrays
License: 		GPL3
Name: 			%{name}
Version: 		%{version}
Packager: 		Iyad Kandalaft <Iyad.Kandalaft@agr.gc.ca>
Release: 		%{release}
Source0: 		%{name}-%{version}.tar.gz
Source1: 		STAR-Fusion-0.1.1.tar.gz
Prefix: 		%{_prefix}
Group: 			Applications/BioInformatics/Alignment
URL:			https://github.com/alexdobin/STAR
AutoReq:		yes

Requires:	perl(SAM_entry)
Requires:	perl(SAM_reader)
Requires:	opt-perl(Carp)
Requires:	opt-perl(Cwd)
Requires:	opt-perl(Data::Dumper)
Requires:	opt-perl(File::Basename)
Requires:	opt-perl(FindBin)
Requires:	opt-perl(Getopt::Long)
Requires:	opt-perl(Set::IntervalTree)
Requires:	opt-perl(lib)
Requires:	opt-perl(strict)
Requires:	opt-perl(warnings)

%global __requires_exclude ^perl

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
%setup -q
%setup -T -D -a 1

%build
cd source
make -pie --jobs=`nproc` prefix=%{_prefix} STARlong
make -pie --jobs=`nproc` prefix=%{_prefix} STAR

%install
mkdir -p $RPM_BUILD_ROOT%{_prefix}/bin
cp source/STAR source/STARlong $RPM_BUILD_ROOT%{_prefix}/bin
cp -r doc $RPM_BUILD_ROOT%{_prefix}/
cp -r STAR-Fusion-0.1.1/STAR-Fusion STAR-Fusion-0.1.1/lib  $RPM_BUILD_ROOT%{_prefix}/bin
cp -r STAR-Fusion-0.1.1/{resources,test}  $RPM_BUILD_ROOT%{_prefix}/


%files
%defattr(755,root,root,755)
%{_bindir}

%defattr(644,root,root,755)
%{_bindir}/lib
%{_prefix}/doc
%{_prefix}/resources


