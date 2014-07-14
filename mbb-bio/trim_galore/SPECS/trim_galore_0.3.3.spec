# This is a sample spec file for wget

### define _topdir	 	/home/rpmbuild/rpms/trim_galore
%define name		trim_galore	
%define version 	0.3.3
%define release 	1
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	A wrapper tool around Cutadapt and FastQC to consistently apply quality and adapter trimming to FastQ files, with some extra functionality for MspI-digested RRBS-type (Reduced Representation Bisufite-Seq) libraries.
License: 		GNU GPL v3
Packager:               Glen Newton glen.newton@gmail.com
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tgz
Patch0:		        %{name}.patch0
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
Trim Galore! is a wrapper script to automate quality and adapter trimming as well as quality control, with some added functionality to remove biased methylation positions for RRBS sequence files (for directional, non-directional (or paired-end) sequencing). It's main features are:
 - For adapter trimming, Trim Galore! uses the first 13 bp of Illumina standard adapters ('AGATCGGAAGAGC') by default (suitable for both ends of paired-end libraries), but accepts other adapter sequence, too
 - For MspI-digested RRBS libraries, Trim Galore! performs quality and adapter trimming in two subsequent steps. This allows it to remove 2 additional bases that contain a cytosine which was artificially introduced in the end-repair step during the library preparation
 - For any kind of FastQ file other than MspI-digested RRBS, Trim Galore! can perform single-pass adapter- and quality trimming
 - The Phred quality of basecalls and the stringency for adapter removal can be specified individually
 - Trim Galore! can remove sequences if they become too short during the trimming process. For paired-end files Trim Galore! removes entire sequence pairs if one (or both) of the two reads became shorter than the set length cutoff. Reads of a read-pair that are longer than a given threshold but for which the partner read has become too short can optionally be written out to single-end files. This ensures that the information of a read pair is not lost entirely if only one read is of good quality
 - Trim Galore! can trim paired-end files by 1 additional bp from the 3' end of all reads to avoid problems with invalid alignments with Bowtie 1
 - Trim Galore! accepts and produces standard or gzip compressed FastQ files
 - FastQC can be run on the resulting output files once trimming has completed (optional)


%prep
%setup -q -c -T
unzip ../../SOURCES/trim_galore_v0.3.3.zip
%patch -P 0 -p0


%build


%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp * $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
