# This is a  spec file for Trans-ABySS

%define name		transabyss
%define release		1
%define version 	1.5.2
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary:        Trans-ABySS is de novo assembly of RNA-Seq data using ABySS.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.zip
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://www.bcgsc.ca/platform/bioinfo/software/trans-abyss
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        BCCA (academic use)
AutoReq:	yes

%description 
The current version of the Trans-ABySS package comes with 3 main applications:
1. transabyss - assemble RNAseq data 
2. transabyss-merge - merge multipleassemblies from (1) 
3. transabyss-analyze - analyze assemblies, either from (1) or (2), for
structural variants and splice variants. Requires reference genome and
annotations.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{installroot}
cp -r * %{buildroot}%{installroot}
rm -r %{buildroot}%{installroot}/prereqs

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/transabyss
%{installroot}/transabyss-merge
%{installroot}/transabyss-analyze
%{installroot}/annotations/setup_hg19.sh
%{installroot}/bin/skip_psl_self.awk
%{installroot}/bin/skip_psl_self_ss.awk
%{installroot}/bin/strip_sam_qual.awk
%{installroot}/bin/strip_sam_seq_qual.awk
%{installroot}/bin/strip_sam_seq_qual_noself.awk
%{installroot}/configs/templates/gsc_local_array.txt
%{installroot}/configs/templates/gsc_local.txt
%{installroot}/configs/templates/gsc_sge_basic_array.txt
%{installroot}/configs/templates/gsc_sge_basic.txt
%{installroot}/configs/templates/gsc_sge_max_resources_array.txt
%{installroot}/configs/templates/gsc_sge_max_resources.txt
%{installroot}/configs/templates/gsc_sge_parallel_array.txt
%{installroot}/configs/templates/gsc_sge_parallel.txt
%{installroot}/sample_dataset/analyze.sh
%{installroot}/sample_dataset/assemble.sh
%{installroot}/sample_dataset/reads/rnaseq_1.fq.gz
%{installroot}/sample_dataset/reads/rnaseq_2.fq.gz
%{installroot}/utilities/sam_cid_extractor.py
