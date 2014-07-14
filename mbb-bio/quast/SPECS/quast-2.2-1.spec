# This is a  spec file for QUAST

%global debug_package %{nil}
%define __os_install_post %{nil}

%define name		quast
%define release		1
%define version 	2.2
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	QUAST stands for QUality ASsesment Tool. The tool evaluates genome assemblies by computing various metrics.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://bioinf.spbau.ru/QUAST
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPL-2
AutoReq:	yes

%description
QUAST stands for QUality ASsesment Tool. The tool evaluates genome assemblies by
computing various metrics including:
    - N50, length of the shortest contig from all that cover 50% of all
      assembly,
    - NG50, where the reference genome is being covered,
    - NA50 and NGA50, where aligned blocks instead of contigs are taken,
    - misassemblies, misassembled and unaligned contigs or contigs bases, 
    - genes and operons covered.  
QUAST also builds convenient plots for different metrics:
    - cumulative contigs length,
    - all kinds of N-metrics,
    - genes and operons covered,
    - GC content.  
QUAST can work both with and without a given reference genome. The tool accepts
multiple assemblies, thus is suitable for comparison. QUAST utilizes MUMmer,
GeneMarkS, MetaGeneMark, GlimmerHMM and GAGE.  These tools are built in, so
there is no need to install them separately. 

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{installroot}
cp -r * %{buildroot}%{installroot}
rm -r %{buildroot}%{installroot}/libs/genemark/linux_32
rm -r %{buildroot}%{installroot}/libs/genemark/macosx
rm -r %{buildroot}%{installroot}/libs/metagenemark/linux_32
rm -r %{buildroot}%{installroot}/libs/metagenemark/macosx
rm -r %{buildroot}%{installroot}/libs/MUMmer3.23*
rm -r %{buildroot}%{installroot}/libs/glimmer


%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/quast.py
%{installroot}/metaquast.py
%{installroot}/libs/gage.py
%{installroot}/libs/gage/colsum.pl
%{installroot}/libs/gage/getMummerStats.sh
%{installroot}/libs/gage/getCorrectnessStats.sh
%{installroot}/libs/genemark/linux_64/gc
%{installroot}/libs/genemark/linux_64/gibbs
%{installroot}/libs/genemark/linux_64/gm
%{installroot}/libs/genemark/linux_64/gmhmmp
%{installroot}/libs/genemark/linux_64/gmhmmp_heuristic.pl
%{installroot}/libs/genemark/linux_64/gmsn.pl
%{installroot}/libs/genemark/linux_64/matinfo
%{installroot}/libs/genemark/linux_64/mkmat
%{installroot}/libs/genemark/linux_64/probuild
%{installroot}/libs/genemark/linux_64/viewmat
%{installroot}/libs/html_saver/static/bootstrap/bootstrap.min.css
%{installroot}/libs/html_saver/static/bootstrap/bootstrap-tooltip-5px-lower.min.js
%{installroot}/libs/metagenemark/linux_64/aa_from_gff.pl
%{installroot}/libs/metagenemark/linux_64/nt_from_gff.pl
%{installroot}/libs/metagenemark/linux_64/gmhmmp
