%define name		FigTree
%define release		1
%define version 	1.4.3
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 
%define	_prefix		%{installroot}
%define __jar_repack	0


BuildRoot:		%{buildroot}
Summary: 		Figtree is signed as a graphical viewer of phylogenetic trees.
License: 		GPL-2|https://code.google.com/p/figtree/
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tgz
Prefix: 		%{installroot}
Group: 			Bioinformatics/Phylogenetics Viewer
AutoReq:		yes
URL:			http://tree.bio.ed.ac.uk/software/figtree/

Requires:		java

%description
FigTree is designed as a graphical viewer of phylogenetic trees and as a program for producing publication-ready figures. As with most of my programs, it was written for my own needs so may not be as polished and feature-complete as a commercial program. In particular it is designed to display summarized and annotated trees produced by BEAST.

%prep
%setup -q -n %{name}_v%{version}

%build
#jar already created, nothing to build

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
cp -r bin images lib  $RPM_BUILD_ROOT%{installroot}/

%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc README.txt
%{installroot}/lib
%{installroot}/images
%defattr(755,root,root,755)
%{installroot}/bin

