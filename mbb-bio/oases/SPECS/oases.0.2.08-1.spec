# This is a  spec file for oases

### define _topdir	 	/home/rpmbuild/rpms/oases
%define name		oases
%define release		1
%define version 	0.2.08
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	oases is a de-novo transcriptome assembler for very short reads 
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Packager:       Zaky Adam <zaky.adam@grc.gc.ca>
Source: 	%{name}-%{version}.tar.gz
Source1: 	velvet-1.2.07.tgz
URL:            http://www.ebi.ac.uk/~zerbino/oases/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPL|https://raw.githubusercontent.com/dzerbino/oases/master/LICENSE.txt
AutoReq:	yes

%description
Oases is a de novo transcriptome assembler designed to produce transcripts from
short read sequencing technologies, such as Illumina, SOLiD, or 454 in the
absence of any genomic assembly. It was developed by Marcel Schulz (MPI for
Molecular Genomics) and Daniel Zerbino (previously at the European
Bioinformatics Institute (EMBL-EBI), now at UC Santa Cruz).  Oases uploads a
preliminary assembly produced by Velvet, and clusters the contigs into small
groups, called loci. It then exploits the paired-end read and long read
information, when available, to construct transcript isoforms. 

%prep
%setup -q
%setup -q -b 1

%build
make 'MAXKMERLENGTH=31' 'VELVET_DIR=../velvet-1.2.07'
cp oases Oases_31
make clean -i 'VELVET_DIR=../velvet-1.2.07'

make 'MAXKMERLENGTH=63' 'VELVET_DIR=../velvet-1.2.07'
cp oases Oases_63
make clean -i 'VELVET_DIR=../velvet-1.2.07'

make 'MAXKMERLENGTH=127' 'VELVET_DIR=../velvet-1.2.07'
cp oases Oases_127
make clean -i 'VELVET_DIR=../velvet-1.2.07'

rename Oases oases Oases_*


%install
mkdir -p %{buildroot}%{installroot}
cp oases_* update_oases.sh %{buildroot}%{installroot}

%files
%defattr(755,root,root)
%{installroot}
