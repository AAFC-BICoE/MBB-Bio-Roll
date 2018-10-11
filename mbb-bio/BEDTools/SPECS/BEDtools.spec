%define name		BEDTools
%define src_name	bedtools2
%define release		1
%define version 	2.27.1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 


BuildRoot:		%{buildroot}
Summary: 		Tool to address common genomics tasks such as finding feature overlaps and computing coverage.
License: 		GNU GPL 
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-v%{version}.tar.gz
Prefix: 		%{installroot}
Group: 			Bioinformatics/Tools
AutoReq:		yes
URL:			https://bedtools.readthedocs.io/en/latest/
Provides:		%{src_name} = %{version}


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
%setup -qn %{src_name}-%{version}

%build
make -j`nproc` prefix=%{installroot}

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install DESTDIR=%{buildroot} prefix=%{installroot}


%files 
%defattr(644,root,root,755)
%dir %{installroot}
%defattr(755,root,root,755)
%{installroot}/bin 
