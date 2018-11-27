  %define debug_package %{nil}

%define name			subread
%define src_name		subread
%define release			1
%define version 		1.6.3
%define buildroot 		%{_topdir}/%{name}-%{version}-root
%define installroot 		/opt/bio/%{name}
%define _prefix			%{installroot}

BuildRoot:		%{buildroot}
Summary: 		Suite of high-performance software programs for processing next-generation sequencing data.
License: 		GPLv3
Name: 			%{name}
Version: 		%{version}
Packager: 		Glen Newton <glen.newton@agr.gc.ca>
Release: 		%{release}
Source: 		%{src_name}-%{version}-source.tar.gz
Prefix: 		%{_prefix}
Group: 			Applications/BioInformatics
URL:			http://subread.sourceforge.net/
AutoReq:		yes

%description
The Subread package comprises a suite of software programs for processing next-gen sequencing read data including:
    - Subread: an accurate and efficient aligner for mapping both genomic DNA-seq reads and RNA-seq reads (for the purpose of expression analysis).
    - Subjunc: an RNA-seq aligner suitable for all purposes of RNA-seq analyses.
    - featureCounts: a highly efficient and accurate read summarization program.
    - exactSNP: a SNP caller that discovers SNPs by testing signals against local background noises.

Cite:
Liao Y, Smyth GK and Shi W. The Subread aligner: fast, accurate and scalable
read mapping by seed-and-vote. Nucleic Acids Research, 41(10):e108, 2013
http://www.ncbi.nlm.nih.gov/pubmed/23558742

Liao Y, Smyth GK and Shi W. featureCounts: an ecient general-purpose program
for assigning sequence reads to genomic features. Bioinformatics, 2013 Nov 30.
[Epub ahead of print]
http://www.ncbi.nlm.nih.gov/pubmed/24227677


%prep
%setup -q -n %{src_name}-%{version}-source

%build
cd src
make -f Makefile.Linux prefix=%{_prefix} -j`nproc`

%install
mkdir -p $RPM_BUILD_ROOT%{_prefix}
cp -r annotation bin doc LICENSE  README.txt $RPM_BUILD_ROOT%{_prefix}

%files
%defattr(755,root,root,755)
%{_bindir}

%defattr(644,root,root,755)
%dir %{_prefix}
%{_prefix}/doc
%{_prefix}/annotation
%{_prefix}/LICENSE
%{_prefix}/README.txt

