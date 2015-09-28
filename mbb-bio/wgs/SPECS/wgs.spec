### %define _topdir	/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/wgs
%define name	    	wgs
%define release     	1
%define version     	8.3rc2
%define installroot 	/opt/bio/%{name}

Summary:  	Celera Assembler: de novo whole-genome shotgun (WGS) DNA sequence assembler
License: 	GPLv2
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.bz2
Prefix: 	/opt/bio
Group: 		Applications/BioInformatics/Assembler
AutoReq:	yes
Url:            http://wgs-assembler.sourceforge.net
Packager: 	Alex MacLean <alex.maclean@agr.gc.ca>
Provides: 	perl(Statistics::Descriptive)
Patch12: asmToAGP.pl.patch12
Patch9: asmToFasta.pl.patch9
Patch10: ca2ace.pl.patch10
Patch11: caqc.pl.patch11
Patch7: dumpScores.pl.patch7
Patch13: greedy_layout_to_IUM.pl.patch13
Patch5: intronstats.pl.patch5
Patch6: plotScoresSingly.pl.patch6
Patch2: runConcurrently.pl.patch2
Patch15: run_greedy.csh.patch15
Patch1: scheduler.pm.patch1
Patch8: sim4polish.pm.patch8
Patch0: summarizeAtacStats.pl.patch0
Patch14: utg2fasta.pl.patch14

%description
Celera Assembler is a de novo whole-genome shotgun (WGS) DNA sequence assembler. It reconstructs long sequences of genomic DNA from fragmentary data produced by whole-genome shotgun sequencing. Celera Assembler has enabled many advances in genomics, including the first whole genome shotgun sequence of a multi-cellular organism (Myers 2000: http://www.sciencemag.org/cgi/content/abstract/287/5461/2196) and the first diploid sequence of an individual human <(Levy 2007: http://biology.plosjournals.org/perlserv/?request=get-document&amp;doi=10.1371/journal.pbio.0050254) Celera Assembler was developed at Celera Genomics http://www.celera.com starting in 1999. It was released to SourceForge in 2004 as the wgs-assembler under the GNU General Public License. The pipeline revised for 454 data was named CABOG (Miller 2008: http://bioinformatics.oxfordjournals.org/cgi/content/abstract/btn548).

%prep
%setup -q
%patch -P 0
%patch -P 1 
%patch -P 2 
%patch -P 5 
%patch -P 6 
%patch -P 7 
%patch -P 8 
%patch -P 9 
%patch -P 10
%patch -P 11 
%patch -P 12 
%patch -P 13 
%patch -P 14 
%patch -P 15 

%build
cd kmer && make install && cd ..
cd src && make

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
mkdir -p $RPM_BUILD_ROOT%{installroot}/Linux-amd64
cp -r LICENSE.txt README $RPM_BUILD_ROOT%{installroot}
cp -r Linux-amd64/* $RPM_BUILD_ROOT%{installroot}/Linux-amd64/

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/Linux-amd64/bin
%{installroot}/Linux-amd64/lib
