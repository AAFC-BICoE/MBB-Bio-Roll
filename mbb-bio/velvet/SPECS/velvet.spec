# This is a  spec file for velvet

%global debug_package %{nil}

%define		__os_install_post %{nil}
%define 	name		velvet
%define		src_name	velvet
%define		release		1
%define		version 	1.2.10
%define		buildroot       %{_topdir}/%{name}-%{version}-root
%define		installroot /opt/bio/%{name}
%define		_prefix	%{installroot}
%define		_libdir %{_prefix}/lib

BuildRoot:	%{buildroot}
Summary: 	velvet is a genome assembler
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Packager:	Christopher Lewis (lewisct@agr.gc.ca)
Source: 	%{src_name}_%{version}.tgz
Patch0:        	env-perl.patch 
Patch1:       	perl-libdir.patch 
URL:            http://www.ebi.ac.uk/~zerbino/velvet/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPL-3|http://www.ebi.ac.uk/~zerbino/velvet/
AutoReq:	yes

%global __requires_exclude ^perl
%global __provides_exclude ^perl

Requires:	opt-perl(Bio::DB::Fasta)
Requires:	opt-perl(Bio::Perl)
Requires:	opt-perl(Bio::PrimarySeq)
Requires:	opt-perl(Bio::SeqIO)
Requires:	opt-perl(Bio::Tools::GFF)
Requires:	opt-perl(Carp)
Requires:	opt-perl(Cwd)
Requires:	opt-perl(Data::Dumper)
Requires:	opt-perl(FindBin)
Requires:	opt-perl(Getopt::Long)
Requires:	opt-perl(List::Util)
Requires:	opt-perl(POSIX)
Requires:	opt-perl(Safe)
Requires:	opt-perl(Storable)
Requires:	opt-perl(lib)
Requires:	opt-perl(strict)
Requires:	opt-perl(threads)
Requires:	opt-perl(threads::shared)
Requires:	opt-perl(warnings)

%description
Velvet is a de novo multithreaded genomic assembler specially designed for
short read sequencing technologies, such as Solexa or 454, developed by Daniel
Zerbino and Ewan Birney at the European Bioinformatics Institute (EMBL-EBI),
near Cambridge, in the United Kingdom.  Velvet currently takes in short read
sequences, removes errors then produces high quality unique contigs. It then
uses paired-end read and long read information, when available, to retrieve the
repeated areas between contigs. 


%prep
%setup -q -n %{src_name}_%{version}
%patch0 -p 1
%patch1 -p 1

%build
for i in {31,61,91,121,151,181,211,241,271,301}; do
	make --jobs=`nproc` MAXKMERLENGTH=$i CATEGORIES=5
	cp velvetg Velvetg_$i
	cp velveth Velveth_$i 
	make clean
done

rename Velvet velvet Velvet*_*

%install
mkdir -p %{buildroot}%{_bindir}
strip velvet{g,h}_*
mv velveth_* velvetg_* %{buildroot}%{_bindir}

pushd %{buildroot}%{_bindir}
ln -s velveth_91 velveth
ln -s velvetg_91 velvetg
popd

cd contrib
cp afg_handling/*.pl %{buildroot}%{_bindir}
cp AssemblyAssembler*/*.py %{buildroot}%{_bindir}
cp columbus_scripts/*.pl %{buildroot}%{_bindir}
cp estimate-exp_cov/*.pl %{buildroot}%{_bindir}
cp extractContigReads/*.pl %{buildroot}%{_bindir}
cp fasta2agp/*.pl %{buildroot}%{_bindir}
cp observed-insert-length.pl/*.pl %{buildroot}%{_bindir}
cp select_paired/*.pl %{buildroot}%{_bindir}
cp show_repeats/*.pl %{buildroot}%{_bindir}
cp shuffleSequences_fasta/*.{pl,py,sh} %{buildroot}%{_bindir}
cp VelvetOptimiser-*/*.pl %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/VelvetOpt
cp -r VelvetOptimiser*/VelvetOpt %{buildroot}%{_libdir}


%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc CREDITS.txt
%doc LICENSE.txt
%doc Manual.pdf
%defattr(755,root,root,755)
%{_libdir}
%{_bindir}

%post
