# This is a  spec file for snpEff

### define _topdir	 	/home/rpmbuild/rpms/snpEff
%define name		snpEff
%define release		1
%define version 	4.3t
%define installroot 	/opt/bio/%{name}
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	snpEff is a fast variant effect predictor (SNP, MNP and InDels) for genomic data.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}_latest_core.zip
Packager:	Wilson Hodgson <wilson.hodgson@canada.ca>
URL: 		http://snpeff.sourceforge.net/
Prefix: 	%{_prefix}
Group: 		Development/Tools
License:	GNU LGPL
AutoReq:	yes

Requires:	opt-perl(POSIX)
Requires:	opt-perl(strict)
Requires:	java >= 1:1.8.0

%global __requires_exclude ^perl

%description
snpEff is a fast variant effect predictor (SNP, MNP and InDels) for genomic
data. It is integrated with Galaxy so it can be used either as a command line or
as a web application.  
snpSift helps filtering and manipulating genomic annotated files (VCF). Once you
annotated your files using SnpEff, you can use SnpSift to help you filter large
genomic datasets in order to find the most significant variants.

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}%{installroot}
cp -r * %{buildroot}%{installroot}
rm -r %{buildroot}%{installroot}/galaxy
rm -r %{buildroot}%{installroot}/examples

%files
%defattr(755,root,root,755)
%{_prefix}
%defattr(644,root,root,755)
%{_prefix}/snpEff.jar
%{_prefix}/SnpSift.jar
%{_prefix}/snpEff.config
%{_prefix}/scripts/annotate_demo.sh

