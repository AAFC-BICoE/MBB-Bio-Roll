%define debug_package %{nil}
### define _topdir	 	/home/rpmbuild/rpms/%{name}
%define name			ClonalFrame
%define src_name		ClonalFrame
%define release		1
%define version 	1.2
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	Inference of bacterial microevolution using multilocus sequence data. 
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz
Patch0:                 ClonalFrame.pro.patch
Prefix: 		/opt/bio
Group: 			Applications/Bioinformatics
URL:			http://www.xavierdidelot.xtreemhost.com/clonalframe.htm
AutoReq:		yes
Packager:   Glen Newton <glen.newton@agr.gc.ca>

%description
"In a nutshell, ClonalFrame identifies the clonal relationships between the members of a sample, while also estimating the chromosomal position of homologous recombination events that have disrupted the clonal inheritance.
ClonalFrame can be applied to any kind of sequence data, from a single fragment of DNA to whole genomes. It is well suited for the analysis of MLST data, where 7 gene fragments have been sequenced, but becomes progressively more powerful as the sequenced regions increase in length and number up to whole genomes. However, it requires the sequences to be aligned. If you have genomic data that is not aligned, we recommend using Mauve which produces alignment of whole bacterial genomes in exactly the format required for analysis with ClonalFrame.
The methods used in ClonalFrame are presented in the paper "Inference of bacterial microevolution using multilocus sequence data" by Didelot and Falush (2007), which is the appropriate citation for this program."


%prep
%setup -q -n ClonalFrame
%patch -P 0 -p1

%build
qmake-qt4 
make

%install
strip bin/*
mkdir -p %{buildroot}%{installroot}
cp -r bin COPYING %{buildroot}%{installroot}



%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
