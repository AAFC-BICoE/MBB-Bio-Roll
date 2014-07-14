# This is a sample spec file for wget

%define name		macse 
### define _topdir	 	/home/rpmbuild/rpms/macse
%define release		1
%define version 	0.8b2
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 
%define __jar_repack	0

BuildRoot:		%{buildroot}
Summary: 		Multiple Alignment of Coding SEquences Accounting for Frameshifts and Stop Codons
License: 		Open Source
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes
URL: 			http://mbb.univ-montp2.fr/MBB/uploads/macse_v0.8b2.jar

%description
"MACSE is the first automatic solution to align protein-coding gene datasets containing non-functional sequences (pseudogenes) without disrupting the underlying codon structure. It has also proved useful in detecting undocumented frameshifts in public database sequences and in aligning next-generation sequencing reads/contigs against a reference coding sequence." (Ranwez, V et al., 2011) 

%prep
%setup -qcn %{name}-%{version}  

%build
#jar already created, nothing to build 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp %{name}_v%{version}.jar  $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
