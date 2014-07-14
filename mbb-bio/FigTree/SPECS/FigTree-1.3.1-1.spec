# This is a sample spec file for wget

%define name		FigTree
### define _topdir	 	/home/rpmbuild/rpms/FigTree
%define release		1
%define version 	1.3.1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 
%define __jar_repack	0

BuildRoot:		%{buildroot}
Summary: 		Figtree is signed as a graphical viewer of phylogenetic trees.
License: 		GPL-2|https://code.google.com/p/figtree/
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tgz
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes
URL:			http://tree.bio.ed.ac.uk/software/figtree/

%description
FigTree is designed as a graphical viewer of phylogenetic trees and as a program for producing publication-ready figures. As with most of my programs, it was written for my own needs so may not be as polished and feature-complete as a commercial program. In particular it is designed to display summarized and annotated trees produced by BEAST.

%prep
%setup -q

%build
#jar already created, nothing to build 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
cp -r lib  $RPM_BUILD_ROOT%{installroot}/

%files
%defattr(755,root,root)
%{installroot}
