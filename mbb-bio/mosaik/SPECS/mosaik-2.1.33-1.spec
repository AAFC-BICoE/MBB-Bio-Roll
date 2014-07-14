# This is a  spec file for mosaik
# Note: the following rpm  packages should be installed:
# zlib-static-1.2.3-27.el6.x86_64.rpm
# glibc-static

### define _topdir	 	/home/rpmbuild/rpms/mosaik
%define name		MOSAIK
%define release		1
%define version 	2.1.33
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	MOSAIK is a reference-guided assembler
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}-source.tar
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://code.google.com/p/mosaik-aligner/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        MIT
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
%setup -q -n MOSAIK-2.1.33-source

%build
make

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r ../bin $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
