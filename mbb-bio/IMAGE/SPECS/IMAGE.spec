%define name		IMAGE
%define release		1
%define version 	2.4.1
%define src_version	2.4
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	Iterative Mapping and Assembly for Gap Elimination. It is a software designed to close gaps in any draft assembly using Illumina paired end reads.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}_version%{version}_64bit.zip
Patch0:         env-perl.patch
Patch1:		separate-scripts.patch
Patch2:		useless-import.patch
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>
URL:            http://www.mybiosoftware.com/assembly-tools/4644
Prefix: 	%{installroot}
Group: 		Bioinformatics/Assembly
License:        GPL
AutoReq:	yes

%global __requires_exclude ^perl
Requires:	opt-perl(Getopt::Long)
Requires:	opt-perl(lib)
Requires:	opt-perl(strict)
Requires:	opt-perl(warnings)

%description
IMAGE (Iterative Mapping and Assembly for Gap Elimination) is a software
designed to close gaps in any draft assembly using Illumina paired end reads.
IMAGE is best described in several stages: aligning of Illumina reads at contig
ends; local assembly of reads into new contigs; reference contigs are extended
or merged; iterating the whole process to extend and merge more contigs.

%prep
%setup -q -n %{name}_version%{src_version}
%patch0 -p 1
%patch1 -p 1
%patch2 -p 1

%build

%install
mkdir -p %{buildroot}%{installroot}/{bin,scripts}
rm -rf *.pl~ run.sh example
mv image.pl restartIMAGE.pl image_run_summary.pl %{buildroot}%{installroot}/bin
mv *.pl %{buildroot}%{installroot}/scripts/

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%defattr(755,root,root,755)
%{_bindir}
%{_prefix}/scripts
