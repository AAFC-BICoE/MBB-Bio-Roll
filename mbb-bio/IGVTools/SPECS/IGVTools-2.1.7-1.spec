# This is a sample spec file for wget

%define name		IGVTools
### define _topdir	 	/home/rpmbuild/rpms/IGVTools
%define release		1
%define version 	2.1.7
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 
%define __jar_repack	0

BuildRoot:		%{buildroot}
Summary: 		The igvtools utility provides a set of tools for pre-processing data files 
License: 		GNU LGPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		igvtools_nogenomes_%{version}.zip
URL:			http://www.broadinstitute.org/igv/igvtools
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
The igvtools utility provides a set of tools for pre-processing data files.  These include:

    * tile
      Converts a sorted data input file to a binary tiled data (.tdf) file. 
      Used to preprocess large datasets for improved IGV performance.
      Supported input file formats: .wig, .cn, .snp, .igv, .res, and .gct

    * count
      Computes average alignment or feature density for over a specified window size across the genome. 
      Used to create a track that can be displayed in IGV, for example as a bar chart.
      Supported input file formats: .sam, .bam, .aligned, .psl, .pslx, and .bed

    * index
      Creates an index file for an ASCII alignment or feature file.
      Index files are required for loading alignment files into IGV, and can significantly improve performance for large feature files.
      Supported input file formats: .sam, .aligned, .vcf, .psl, and .bed

    * sort
      Sorts the input file by start position. 
      Used to prepare data files for tools that required sorted input files.
      Supported input file formats: .cn, .igv, .sam, .aligned, .psl, .bed, and .vcf

%prep
%setup -q -n %{name} 

%build
#jar already created, and binaries compiled, nothing to build 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
cp igvtools igvtools_gui igvtools.jar  $RPM_BUILD_ROOT%{installroot}/

%files
%defattr(755,root,root)
%{installroot}
