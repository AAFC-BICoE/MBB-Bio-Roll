### %define _topdir	/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/wgs
%define name	    	wgs
%define release     	1
%define version     	8.3rc2
%define buildroot   	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary:  	Celera Assembler: de novo whole-genome shotgun (WGS) DNA sequence assembler
License: 	GPLv2
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}-Linux_amd64.tar.bz2
Patch0:         %{name}-%{version}-%{release}.asmToAGP.patch0
Patch1:         %{name}-%{version}-%{release}.ca2ace.patch1
Patch2:         %{name}-%{version}-%{release}.caqc.patch2
Patch3:         %{name}-%{version}-%{release}.convert-fasta-to-v2.patch3
Patch4:         %{name}-%{version}-%{release}.fastaToCa.patch4
Patch5:         %{name}-%{version}-%{release}.greedy_layout_to_IUM.patch5
Patch6:         %{name}-%{version}-%{release}.mergqc.patch6
Patch7:         %{name}-%{version}-%{release}.replaceUIDwithName-fastq.patch7
Patch8:         %{name}-%{version}-%{release}.replaceUIDwithName-posmap.patch8
Patch9:         %{name}-%{version}-%{release}.run_greedy.patch9
Patch10:        %{name}-%{version}-%{release}.tracearchiveToCA.patch10
Patch11:        %{name}-%{version}-%{release}.tracedb-to-frg.patch11
Patch12:        %{name}-%{version}-%{release}.utg2fasta.patch12
Prefix: 	/opt/bio
Group: 		Applications/BioInformatics/Assembler
AutoReq:	no 
Url:            http://wgs-assembler.sourceforge.net
Packager: 	Alex MacLean <alex.maclean@agr.gc.ca>
Provides: 	perl(Statistics::Descriptive)
Requires:       glibc-2.14 = 2.14

%description
Celera Assembler is a de novo whole-genome shotgun (WGS) DNA sequence assembler. It reconstructs long sequences of genomic DNA from fragmentary data produced by whole-genome shotgun sequencing. Celera Assembler has enabled many advances in genomics, including the first whole genome shotgun sequence of a multi-cellular organism (Myers 2000: http://www.sciencemag.org/cgi/content/abstract/287/5461/2196) and the first diploid sequence of an individual human <(Levy 2007: http://biology.plosjournals.org/perlserv/?request=get-document&amp;doi=10.1371/journal.pbio.0050254) Celera Assembler was developed at Celera Genomics http://www.celera.com starting in 1999. It was released to SourceForge in 2004 as the wgs-assembler under the GNU General Public License. The pipeline revised for 454 data was named CABOG (Miller 2008: http://bioinformatics.oxfordjournals.org/cgi/content/abstract/btn548).

%prep
%setup -q
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
%patch -P 12 -p1

%build

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
mkdir -p $RPM_BUILD_ROOT%{installroot}/Linux-amd64
cp -r LICENSE.txt README $RPM_BUILD_ROOT%{installroot}
cp -r Linux-amd64/bin Linux-amd64/lib $RPM_BUILD_ROOT%{installroot}/Linux-amd64/

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/Linux-amd64/bin
%defattr(644,root,root,755)
%{installroot}/Linux-amd64/bin/TIGR
