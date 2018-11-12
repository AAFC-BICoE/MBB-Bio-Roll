%define name		oases
%define release		1
%define version 	0.2.09
%define installroot	/opt/bio/%{name}
%define	_prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	oases is a de-novo transcriptome assembler for very short reads 
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>
Source: 	%{name}-%{version}.tar.gz
Source1:	velvet_1.2.10.tgz
URL:            http://www.ebi.ac.uk/~zerbino/oases/
Prefix: 	%{_prefix}	
Group: 		Bioinformatics/Assembler	
License:        GPL
AutoReq:	yes

BuildRequires:	texlive-pdftex

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
%setup -q -a 1

%build
for i in {31,61,91,121,151,191}; do
	make MAXKMERLENGTH=$i VELVET_DIR=velvet_1.2.10 CATEGORIES=5 OPENMP=1
	cp oases Oases_$i
	make clean -i VELVET_DIR=velvet_1.2.10
done
rename Oases oases Oases_*
cd doc
make

%install
mkdir -p %{buildroot}%{_bindir}
cp oases_* %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -s oases_91 oases

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc README.md 
%doc ChangeLog
%doc OasesManual.pdf
%defattr(755,root,root,755)
%{_bindir}
