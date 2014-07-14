# This is a sample spec file for wget

%define name		picard-tools
### define _topdir	 	/home/rpmbuild/rpms/picardtools
%define release		1
%define version 	1.77
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 
%define __jar_repack	0

BuildRoot:		%{buildroot}
Summary: 		A set of tools (in Java) for working with next generation sequencing data in the BAM format.
License: 		MIT, Apache License
URL:			http://picard.sourceforge.net/index.shtml
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.zip
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
Picard comprises Java-based command-line utilities that manipulate SAM files, and a Java API (SAM-JDK) for creating new programs that read and write SAM files. Both SAM text format and SAM binary (BAM) format are supported.
 
%prep
%setup -q

%build
#jar already created, nothing to build 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
cp -r *  $RPM_BUILD_ROOT%{installroot}/

%files
%defattr(755,root,root)
%{installroot}
