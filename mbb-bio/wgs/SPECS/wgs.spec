%define name	    	wgs
%define release     	1
%define version     	8.3rc2
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}
%define buildroot       %{_topdir}/%{name}-%{version}-root

Summary:  	Celera Assembler: de novo whole-genome shotgun (WGS) DNA sequence assembler
License: 	GPLv2
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.bz2
Prefix: 	/opt/bio
Group: 		Bioinformatics/Assembler
AutoReq:	yes
Url:            http://wgs-assembler.sourceforge.net
Packager: 	Tim Forbes <timothy.forbes@canada.ca>
Patch0:		env-perl.patch
Patch1:		bin-tcsh.patch

%global		__requires_exclude ^perl
%global		__provides_exclude ^perl
provides: 	opt-perl(Statistics::Descriptive)
provides:	opt-perl(TIGR::Foundation)
requires:	opt-perl(lib)
requires:	opt-perl(strict)
requires:	opt-perl(Carp)
requires:	opt-perl(Config)
requires:	opt-perl(Cwd)
requires:	opt-perl(DB_File)
requires:	opt-perl(Exporter)
requires:	opt-perl(File::Basename)
requires:	opt-perl(File::Copy)
requires:	opt-perl(FileHandle)
requires:	opt-perl(FindBin)
requires:	opt-perl(Getopt::Long)
requires:	opt-perl(IO::File)
requires:	opt-perl(IO::Handle)
requires:	opt-perl(Math::BigFloat)
requires:	opt-perl(POSIX)
requires:	opt-perl(Statistics::Descriptive)
requires:	opt-perl(Sys::Hostname)
requires:	opt-perl(lib)
requires:	opt-perl(strict)
requires:	opt-perl(vars)


%description
Celera Assembler is a de novo whole-genome shotgun (WGS) DNA sequence assembler. It reconstructs long sequences of genomic DNA from fragmentary data produced by whole-genome shotgun sequencing. Celera Assembler has enabled many advances in genomics, including the first whole genome shotgun sequence of a multi-cellular organism (Myers 2000: http://www.sciencemag.org/cgi/content/abstract/287/5461/2196) and the first diploid sequence of an individual human <(Levy 2007: http://biology.plosjournals.org/perlserv/?request=get-document&amp;doi=10.1371/journal.pbio.0050254) Celera Assembler was developed at Celera Genomics http://www.celera.com starting in 1999. It was released to SourceForge in 2004 as the wgs-assembler under the GNU General Public License. The pipeline revised for 454 data was named CABOG (Miller 2008: http://bioinformatics.oxfordjournals.org/cgi/content/abstract/btn548).

%prep
%setup -q
%patch0 -p 1
%patch1 -p 1

%build
cd kmer && make install && cd ..
cd src && make

%install
mkdir -p %{buildroot}%{installroot}/bin
mkdir -p %{buildroot}%{installroot}/lib

cp -r Linux-amd64/bin/ %{buildroot}%{installroot}
cp -r Linux-amd64/lib/ %{buildroot}%{installroot}

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%doc README
%dir %{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/lib
