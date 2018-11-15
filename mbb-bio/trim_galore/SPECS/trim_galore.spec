%define name		trim_galore
%define version 	0.5.0
%define release 	1
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		A wrapper tool around Cutadapt and FastQC to consistently apply quality and adapter trimming to FastQ files, with some extra functionality for MspI-digested RRBS-type (Reduced Representation Bisufite-Seq) libraries.
License: 		GNU GPL v3
Packager:               Glen Newton glen.newton@gmail.com
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{version}.tar.gz
Prefix: 		%{_prefix}
Group: 			BioInformatics/Tools
URL:			https://github.com/FelixKrueger/TrimGalore
AutoReq:		yes

Patch0:		        env-perl.patch

%global		        __requires_exclude ^perl
%global         	__provides_exclude ^perl


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
%setup -qn TrimGalore-%{version}
%patch0 -p 1

%build


%install
#remove some files and directories that should not be packaged...
mv Docs/RRBS_Guide.pdf Docs/Trim_Galore_User_Guide.md .
rm -fr test_files/ Docs/

mkdir -p %{buildroot}%{installroot}
cp -r * %{buildroot}%{installroot}


%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc LICENSE README.md Trim_Galore_User_Guide.md RRBS_Guide.pdf
%defattr(644,root,root,755)
%{_prefix}
%attr(755, root, root) /opt/bio/trim_galore/trim_galore

%postun
# if removed, the package leaves some extraneous files around. clean them up.
rm -fr  %{installroot}/

