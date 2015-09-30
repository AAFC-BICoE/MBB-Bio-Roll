# This is a sample spec file for wget

%define name		BEDTools
### define _topdir	 	/home/rpmbuild/rpms/BEDTools
%define release		1
%define version 	2.25.0
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 


BuildRoot:		%{buildroot}
Summary: 		Tool to address common genomics tasks such as finding feature overlaps and computing coverage.
License: 		GNU GPL 
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		bedtools-%{version}.tar.gz
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes
URL:			http://code.google.com/p/bedtools/


%description
The BEDTools utilities allow one to address common genomics tasks such as finding feature overlaps and computing coverage. The utilities are largely based on four widely-used file formats: BED, GFF/GTF, VCF, and SAM/BAM. Using BEDTools, one can develop sophisticated pipelines that answer complicated research questions by "streaming" several BEDTools together. The following are examples of common questions that one can address with BEDTools.

   1. Intersecting two BED files in search of overlapping features.
   2. Culling/refining/computing coverage for BAM alignments based on genome features.
   3. Merging overlapping features.
   4. Screening for paired-end (PE) overlaps between PE sequences and existing genomic features.
   5. Calculating the depth and breadth of sequence coverage across defined "windows" in a genome.
   6. Screening for overlaps between "split" alignments and genomic features. 


%prep
#%setup -qn %{name}-Version-%{version}
%setup -qn bedtools2

%build
make 


%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r bin $RPM_BUILD_ROOT%{installroot}


%files 
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin 
