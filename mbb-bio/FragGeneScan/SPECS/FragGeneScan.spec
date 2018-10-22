%define name		FragGeneScan
%define release		1
%define version 	1.31
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define installroot	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	An application for finding (fragmented) genes in short reads.
License: 	GPL
Name: 		%{name}
Version: 	%{version}
Packager:	Glen Newton <glen.newton@agr.gc.ca>
Release: 	%{release}
Source: 	%{name}%{version}.tar.gz
Prefix: 	%{installroot}
Group: 		Applications/BioInformatics
URL:		http://sourceforge.net/projects/fraggenescan/
AutoReq:	yes

%description
FragGeneScan is an application for finding (fragmented) genes in short reads. It can also be applied to predict prokaryotic genes in incomplete assemblies or complete genomes.

FragGeneScan was first released through omics website (http://omics.informatics.indiana.edu/FragGeneScan/) in March 2010, where you can find its old releases. FragGeneScan migrated to SourceForge in October, 2013. 

%prep
%setup -q -n %{name}%{version}

%build
make clean
make fgs

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/bin
cp -r train  $RPM_BUILD_ROOT%{installroot}
cp FragGeneScan $RPM_BUILD_ROOT%{installroot}/bin/

%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc README
%doc releases
%{installroot}/train
%defattr(755,root,root,755)
%{installroot}/bin
