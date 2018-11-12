%define name		picard-tools
%define src_name	picard
%define release		1
%define version 	2.18.16
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib
%define __jar_repack	0

BuildRoot:		%{buildroot}
Summary: 		A set of tools (in Java) for working with next generation sequencing data in the BAM format.
License: 		MIT, Apache License
URL:			http://picard.sourceforge.net/index.shtml
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source0: 		%{name}-v%{version}.tar.gz
Source1: 		%{name}.sh
Prefix: 		%{_prefix}
Group: 			Bioinformatics/Utilities
AutoReq:		yes

Requires:		java >= 1:1.8.0

%description
Picard is a set of command line tools for manipulating high-throughput sequencing (HTS) data and formats such as SAM/BAM/CRAM and VCF. These file formats are defined in the Hts-specs repository. See especially the SAM specification and the VCF specification.

%prep
%setup -q -n %{src_name}-%{version}
cp %{SOURCE1} ./
mkdir .git

%build
./gradlew shadowJar

%install
mkdir -p %{buildroot}%{_bindir} 
mkdir -p %{buildroot}%{_libdir}
cp %{name}.sh %{buildroot}%{_bindir}
cp build/libs/picard.jar %{buildroot}%{_libdir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc LICENSE.txt
%doc README.md
%{_libdir}
%defattr(755,root,root,755)
%{_bindir}
