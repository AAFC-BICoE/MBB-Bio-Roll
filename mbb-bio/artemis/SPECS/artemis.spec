# This is a  spec file ifor artemis

### define _topdir	 	/home/rpmbuild/rpms/artemis
%define name		artemis
%define release		1
%define version 	17.0.1
%define installroot 	/opt/bio/%{name}

%define __jar_repack %{nil}

BuildRoot:	%{buildroot}
Summary: 	Artemis is a free genome browser and annotation tool. ACT is a free tool for displaying pairwise comparisons between two or more DNA sequences. DNAPlotter can be used to generate images of circular and linear DNA maps to display regions and features of interest.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-v%{version}.tar.gz
Patch0:		env-perl.patch 
#Patch1:         %{name}-%{version}-%{release}.patch1
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>	
URL:            http://www.sanger.ac.uk/resources/software/artemis/
Prefix: 	%{installroot}
Group: 		Development/Tools
License:        GPL|http://www.sanger.ac.uk/resources/software/artemis	
AutoReq:	yes

BuildRequires:	java-sdk >= 1:1.8.0

Requires:	java >= 1:1.8.0
Requires:	opt-perl
Requires:	opt-perl(Getopt::Long)
Requires:	opt-perl(GO::AppHandle)
Requires:	opt-perl(strict)

%global __requires_exclude ^perl

%description
Artemis is a free genome browser and annotation tool that allows visualisation
of sequence features, next generation data and the results of analyses within
the context of the sequence, and also its six-frame translation. Artemis is
writte in Java, and is available for UNIX, Macintosh and Windows systems. It can
read EMBL and GENBANK database entries or sequence in FASTA, indexed FASTA or
raw format. Other sequence features can be in EMBL, GENBANK or GFF format.  
ACT is a free tool for displaying pairwise comparisons between two or more DNA
sequences. It can be used to identify and analyse regions of similarity and
difference between genomes and to explore conservation of synteny, in the
context of the entire sequences and their annotation.
DNAPlotter can be used to generate images of circular and linear DNA maps to
display regions and features of interest. The images can be inserted into a
document or printed out directly. As this uses Artemis it can read in the common
file formats EMBL, GenBank and GFF3.

%prep
%setup -q -n Artemis-%{version}
%patch0 -p1

%build
# Building with -j`nproc` exceeds memory availability
JAVA_TOOL_OPTION="-Xmx4G" make -j 8

%install
mkdir -p %{buildroot}%{installroot}
JAVA_TOOL_OPTION="-Xmx1G" make dist
cp -r tar_build/artemis/. %{buildroot}%{installroot}/


%files
%defattr(644,root,root,755)
%dir %{installroot}
%{installroot}/artemis_sqlmap
%{installroot}/etc
%{installroot}/images
%{installroot}/lib
%{installroot}/org
%{installroot}/README.md
%{installroot}/setenv
%{installroot}/uk
%defattr(755,root,root,755)
%{installroot}/act
%{installroot}/art
%{installroot}/bamview
%{installroot}/dnaplotter

