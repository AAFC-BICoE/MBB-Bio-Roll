# This is a  spec file for mauve

### define _topdir	 	/home/rpmbuild/rpms/mauve
%define name		mauve
%define release		1
%define version 	2.3.1
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	Mauve is a Multiple Genome Alignment.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}_linux_%{version}.tar.gz
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://asap.ahabs.wisc.edu/mauve/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPL|http://asap.ahabs.wisc.edu/mauve/download.php	
AutoReq:	yes

%description
Mauve is a system for efficiently constructing multiple genome alignments in the
presence of large-scale evolutionary events such as rearrangement and inversion.
Multiple genome alignment provides a basis for research into comparative
genomics and the study of evolutionary dynamics. Aligning whole genomes is a
fundamentally different problem than aligning short sequences. Mauve has been
developed with the idea that a multiple genome aligner should require only
modest computational resources. It employs algorithmic techniques that scale
well in the amount of sequence being aligned. For example, a pair of Y. pestis
genomes can be aligned in under a minute, while a group of 9 divergent
Enterobacterial genomes can be aligned in a few hours.

%prep 
%setup -q -n mauve_2.3.1

%build

%install
mkdir -p %{buildroot}%{installroot}
cp Mauve Mauve.jar mauveAligner progressiveMauve %{buildroot}%{installroot}
cp -r ext/ linux-x64/  %{buildroot}%{installroot}

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/Mauve
%{installroot}/mauveAligner
%{installroot}/progressiveMauve
%{installroot}/linux-x64/progressiveMauve
%{installroot}/linux-x64/mauveAligner
