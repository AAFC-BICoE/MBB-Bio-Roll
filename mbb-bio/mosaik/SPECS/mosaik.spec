%define name		MOSAIK
%define release		1
%define version 	2.2.3
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	MOSAIK is a reference-guided assembler
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}-source.tar
Patch0:		makefile-bad-ldflag.patch
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://code.google.com/p/mosaik-aligner/
Prefix: 	%{_prefix}
Group: 		Bioinformatics/Assembler
License:        GPLv2
AutoReq:	yes

%description
MOSAIK is a reference-guided assembler comprising of four main modular programs:
- MosaikBuild
- MosaikAligner
- MosaikSort
- MosaikAssembler.  
MosaikBuild converts various sequence formats into Mosaik’s native read format.
MosaikAligner pairwise aligns each read to a specified series of reference
sequences. MosaikSort resolves paired-end reads and sorts the alignments by the
reference sequence coordinates. Finally, MosaikAssembler parses the sorted
alignment archive and produces a multiple sequence alignment which is then saved
into an assembly file format.  At this time, the workflow consists of supplying
sequences in FASTA, FASTQ, Illumina Bustard & Gerald, or SRF file formats and
producing assembly files (phrap ace and GigaBayes gig formats) which can be
viewed with utilities such as consed or EagleView. 

%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p 1

%build
make -j`nproc`

%install
mkdir -p %{buildroot}%{_bindir}
mv ../bin/* %{buildroot}%{_bindir}

%files
%defattr(644,root,rooti,755)
%dir %{_prefix}
%defattr(755,root,root,755)
%{_bindir}
