%define name		bam2fastq
%define release		1
%define version 	1.1.0
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 

BuildRoot:		%{buildroot}
Summary: 		Intended to extract sequence and quality data from binary BAM files
License: 		MIT License, Apache License Version 2 
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tgz
Prefix: 		%{installroot}
Group: 			Bioinformatics/Tools
AutoReq:		yes

%description
The BAM format is an efficient method for storing and sharing data from modern, highly parallel sequencers. While primarily used for storing alignment information, BAMs can (and frequently do) store unaligned reads as well.

There are a growing number of general-purpose SAM/BAM manipulation programs, including SAMtools, Picard, and Bamtools. This tool is not intended to duplicate the complex suite of tasks those programs perform. Rather, it is simply intended to extract raw sequences (with qualities). We envision this tool being primarily useful to those wishing to duplicate or extend previous analyses.

%prep
%setup -q 

%build
make 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
cp bam2fastq  $RPM_BUILD_ROOT%{installroot} 

%files
%defattr(755,root,root,755)
%{installroot}
