### define _topdir	 	/home/rpmbuild/rpms/samtools
%define name	        wgs
%define release		1
%define version 	8.2
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 		Celera Assembler: de novo whole-genome shotgun (WGS) DNA sequence assembler
License: 		GPLv2
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.bz2
Prefix: 		/opt/bio
Group: 			Applications/BioInformatics/Assembler
AutoReq:		yes
Url:                   http://wgs-assembler.sourceforge.net/
Packager:	Glen Newton <glen.newton@agr.gc.ca>\
Provides: perl(Statistics::Descriptive)

%description
Celera Assembler is a de novo whole-genome shotgun (WGS) DNA sequence assembler. It reconstructs long sequences of genomic DNA from fragmentary data produced by whole-genome shotgun sequencing. Celera Assembler has enabled many advances in genomics, including the first whole genome shotgun sequence of a multi-cellular organism (Myers 2000: http://www.sciencemag.org/cgi/content/abstract/287/5461/2196) and the first diploid sequence of an individual human <(Levy 2007: http://biology.plosjournals.org/perlserv/?request=get-document&amp;doi=10.1371/journal.pbio.0050254) Celera Assembler was developed at Celera Genomics http://www.celera.com starting in 1999. It was released to SourceForge in 2004 as the wgs-assembler under the GNU General Public License. The pipeline revised for 454 data was named CABOG (Miller 2008: http://bioinformatics.oxfordjournals.org/cgi/content/abstract/btn548).

%prep
%setup -qn wgs

%build


%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
cp -r LICENSE.txt  Linux-amd64/*  README $RPM_BUILD_ROOT%{installroot}

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin




