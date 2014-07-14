# This is a  spec file for IMAGE

%global debug_package %{nil}
%define name		IMAGE
%define release		4
%define version 	2.33
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	IMAGE stands for Iterative Mapping and Assembly for Gap Elimination.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}_version%{version}_64bit.zip
Patch0:         %{name}-%{version}-%{release}.patch0
Patch1:         %{name}-%{version}-%{release}.patch1
Patch2:         %{name}-%{version}-%{release}.patch2
Patch3:         %{name}-%{version}-%{release}.patch3
Patch4:         %{name}-%{version}-%{release}.patch4
Patch5:         %{name}-%{version}-%{release}.patch5
Patch6:         %{name}-%{version}-%{release}.patch6
Patch7:         %{name}-%{version}-%{release}.patch7
Patch8:         %{name}-%{version}-%{release}.patch8
Patch9:         %{name}-%{version}-%{release}.patch9
Patch10:         %{name}-%{version}-%{release}.patch10
Patch11:         %{name}-%{version}-%{release}.patch11
Patch12:         %{name}-%{version}-%{release}.patch12
Patch13:         %{name}-%{version}-%{release}.patch13
Patch14:         %{name}-%{version}-%{release}.patch14
Patch15:         %{name}-%{version}-%{release}.patch15
Patch16:         %{name}-%{version}-%{release}.patch16
Patch17:         %{name}-%{version}-%{release}.patch17
Patch18:         %{name}-%{version}-%{release}.patch18
Patch19:         %{name}-%{version}-%{release}.patch19
Patch20:         %{name}-%{version}-%{release}.patch20
Patch21:         %{name}-%{version}-%{release}.patch21
Patch22:         %{name}-%{version}-%{release}.patch22
Patch23:         %{name}-%{version}-%{release}.patch23
Patch24:         %{name}-%{version}-%{release}.patch24
Patch25:         %{name}-%{version}-%{release}.patch25
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://www.mybiosoftware.com/assembly-tools/4644
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GNU GPL
AutoReq:	yes

%description
IMAGE (Iterative Mapping and Assembly for Gap Elimination) is a software
designed to close gaps in any draft assembly using Illumina paired end reads.
IMAGE is best described in several stages: aligning of Illumina reads at contig
ends; local assembly of reads into new contigs; reference contigs are extended
or merged; iterating the whole process to extend and merge more contigs.

%prep
%setup -q -n IMAGE_version2
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
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%patch -P 17 -p1
%patch -P 18 -p1
%patch -P 19 -p1
%patch -P 20 -p1
%patch -P 21 -p1
%patch -P 22 -p1
%patch -P 23 -p1
%patch -P 24 -p1
%patch -P 25 -p1

%build

%install
mkdir -p %{buildroot}%{installroot}
cp -r * %{buildroot}%{installroot}
rm %{buildroot}%{installroot}/velvet?

%files
%defattr(755,root,root,755)
%{installroot}
%defattr(644,root,root,755)
%{installroot}/example/76bp_1.fastq
%{installroot}/example/76bp_2.fastq
%{installroot}/example/scaffolds.fa
%{installroot}/example/SpA_genome.dna
