# This is a  spec file for snpEff

### define _topdir	 	/home/rpmbuild/rpms/snpEff
%define name		snpEff
%define release		1
%define version 	3.2
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	snpEff is a fast variant effect predictor (SNP, MNP and InDels) for genomic data.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}_latest_core.zip
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://snpeff.sourceforge.net/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GNU LGPL
AutoReq:	yes

%description
snpEff is a fast variant effect predictor (SNP, MNP and InDels) for genomic
data. It is integrated with Galaxy so it can be used either as a command line or
as a web application.  
snpSift helps filtering and manipulating genomic annotated files (VCF). Once you
annotated your files using SnpEff, you can use SnpSift to help you filter large
genomic datasets in order to find the most significant variants.

%prep
%setup -q -n snpEff

%build

%install
mkdir -p %{buildroot}%{installroot}
cp -r * %{buildroot}%{installroot}
rm -r %{buildroot}%{installroot}/galaxy
rm %{buildroot}%{installroot}/demo.1kg.vcf

%files
%defattr(755,root,root)
%{installroot}
%defattr(644,root,root)
%{installroot}/snpEff.jar
%{installroot}/SnpSift.jar
%{installroot}/snpEff.config
%{installroot}/scripts/annotate_demo.sh
