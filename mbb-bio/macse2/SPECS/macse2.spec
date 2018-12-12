%define name		macse2
%define release		1
%define version 	2.03
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		Multiple Alignment of Coding SEquences Accounting for Frameshifts and Stop Codons
License: 		Unknown
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.tar.gz
Patch0:			exec-script.patch
Prefix: 		%{_prefix}
Group: 			Bioinformatics/Alignment
AutoReq:		yes
URL: 			http://mbb.univ-montp2.fr/MBB/uploads/macse_v0.8b2.jar

%description
MACSE is the first automatic solution to align protein-coding gene datasets containing non-functional sequences (pseudogenes) without disrupting the underlying codon structure. It has also proved useful in detecting undocumented frameshifts in public database sequences and in aligning next-generation sequencing reads/contigs against a reference coding sequence.

%prep
%setup -q -c ./
%patch0 -p1

%build
#Source is not available. JAR already created. 

%install
mkdir -p %{buildroot}%{_bindir}
cp macse_v%{version}.jar  %{buildroot}%{_prefix}/%{name}.jar
mv bin/macse2 %{buildroot}%{_bindir}/

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%{_prefix}/%{name}.jar
%defattr(755,root,root,755)
%{_bindir}
