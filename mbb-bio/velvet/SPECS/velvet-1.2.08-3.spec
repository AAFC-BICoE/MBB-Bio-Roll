# This is a  spec file for velvet

%define name		velvet
%define release		3
%define version 	1.2.08
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	velvet is a genome assembler
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Packager:	Christopher Lewis (lewisct@agr.gc.ca)
Source: 	%{name}_%{version}.tgz
Patch0:         %{name}-%{version}-%{release}.afg_handling.patch0
Patch1:         %{name}-%{version}-%{release}.AssemblyAssembler.patch1
Patch2:         %{name}-%{version}-%{release}.columbus_scripts.patch2
Patch3:         %{name}-%{version}-%{release}.estimate-exp_cov.patch3
Patch4:         %{name}-%{version}-%{release}.extractContigReads.patch4
Patch5:         %{name}-%{version}-%{release}.fasta2agp.patch5
Patch6:         %{name}-%{version}-%{release}.MetaVelvet.patch6
Patch7:         %{name}-%{version}-%{release}.observed-insert-length.patch7
Patch8:         %{name}-%{version}-%{release}.select_paired.patch8
Patch9:         %{name}-%{version}-%{release}.show_repeats.patch9
Patch10:         %{name}-%{version}-%{release}.shuffleSequences_fasta.patch10
Patch11:         %{name}-%{version}-%{release}.VelvetOptimiser.patch11
URL:            http://www.ebi.ac.uk/~zerbino/velvet/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPL-3|http://www.ebi.ac.uk/~zerbino/velvet/
AutoReq:	yes

%description
Velvet is a de novo multithreaded genomic assembler specially designed for
short read sequencing technologies, such as Solexa or 454, developed by Daniel
Zerbino and Ewan Birney at the European Bioinformatics Institute (EMBL-EBI),
near Cambridge, in the United Kingdom.  Velvet currently takes in short read
sequences, removes errors then produces high quality unique contigs. It then
uses paired-end read and long read information, when available, to retrieve the
repeated areas between contigs. 


%prep
%setup -q -n velvet
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p1
%patch -P 11 -p1

%build
make --jobs=`nproc` 'MAXKMERLENGTH=31' 'CATEGORIES=5'
cp velvetg Velvetg_31 
cp velveth Velveth_31 
make clean
make --jobs=`nproc` 'MAXKMERLENGTH=63' 'CATEGORIES=5'
cp velvetg Velvetg_63 
cp velveth Velveth_63 
make clean
make --jobs=`nproc` 'MAXKMERLENGTH=127' 'CATEGORIES=5'
cp velvetg Velvetg_127
cp velveth Velveth_127
make clean
make --jobs=`nproc` 'MAXKMERLENGTH=145' 'CATEGORIES=5'
cp velvetg Velvetg_145
cp velveth Velveth_145
make clean
make --jobs=`nproc` 'MAXKMERLENGTH=195' 'CATEGORIES=5'
cp velvetg Velvetg_195
cp velveth Velveth_195
make clean
make --jobs=`nproc` 'MAXKMERLENGTH=245' 'CATEGORIES=5'
cp velvetg Velvetg_245
cp velveth Velveth_245
make clean

rename Velvet velvet Velvet*_*

#cd contrib/MetaVelvet-1.2.01
#make

%install
mkdir -p %{buildroot}%{installroot}
strip velvet*
cp velveth_* velvetg_* update_velvet.sh %{buildroot}%{installroot}
cp -r contrib %{buildroot}%{installroot}
rm %{buildroot}%{installroot}/contrib/shuffleSequences_fasta/kseq.h
rm %{buildroot}%{installroot}/contrib/shuffleSequences_fasta/shuffleSeqs-fast.c
rm -r %{buildroot}%{installroot}/contrib/solaris
rm  %{buildroot}%{installroot}/contrib/MetaVelvet-v0.3.1/Makefile
rm -r %{buildroot}%{installroot}/contrib/MetaVelvet-v0.3.1/src
rm %{buildroot}%{installroot}/contrib/MetaVelvet-1.2.01/Makefile
rm -r %{buildroot}%{installroot}/contrib/MetaVelvet-1.2.01/Apps
rm -r %{buildroot}%{installroot}/contrib/MetaVelvet-1.2.01/Common
rm -r %{buildroot}%{installroot}/contrib/MetaVelvet-1.2.01/ISGraph
rm -r %{buildroot}%{installroot}/contrib/MetaVelvet-1.2.01/Peak
rm -r %{buildroot}%{installroot}/contrib/MetaVelvet-1.2.01/Utils
rm -r %{buildroot}%{installroot}/contrib/MetaVelvet-1.2.01/Velvet-1.1.06
rm -r %{buildroot}%{installroot}/contrib/MetaVelvet-1.2.01/VelvetAPI
rm -r %{buildroot}%{installroot}/contrib

%files
%defattr(755,root,root,755)
%{installroot}
%defattr(644,root,root,755)


