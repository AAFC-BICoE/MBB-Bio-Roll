%define name		FastQC
%define release		1
%define version 	0.11.8
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define	_prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		A quality control tool for high throughput sequence data.
License: 		GNU GPL
URL:			http://www.bioinformatics.babraham.ac.uk/projects/fastqc/
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.tar.gz
Prefix: 		%{installroot}
Group: 			Bioinformatics/QAQC
AutoReq:		yes
Patch0:			env-perl.patch

BuildRequires:		ant
BuildRequires:		java-sdk >= 1:1.8.0
Requires:		java >= 1:1.8.0
Requires:		opt-perl
Requires:		opt-perl(FindBin)
Requires:		opt-perl(Getopt::Long)
Requires:		opt-perl(strict)
Requires:		opt-perl(warnings)

%global __requires_exclude ^perl

%description
FastQC aims to provide a simple way to do some quality control checks on raw sequence data coming from high throughput sequencing pipelines. It provides a modular set of analyses which you can use to give a quick impression of whether your data has any problems of which you should be aware before doing any further analysis.

The main functions of FastQC are

    Import of data from BAM, SAM or FastQ files (any variant)
    Providing a quick overview to tell you in which areas there may be problems
    Summary graphs and tables to quickly assess your data
    Export of results to an HTML based permanent report
    Offline operation to allow automated generation of reports without running the interactive application

%prep
%setup -q -n %{name}-%{version}
%patch -P 0 -p 1

%build
ant

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/bin

cd bin

cp -r Configuration net org Templates uk $RPM_BUILD_ROOT%{installroot}
cp fastqc* jbzip2* sam* $RPM_BUILD_ROOT%{installroot}

cd $RPM_BUILD_ROOT%{installroot}/bin/
ln -s ../fastqc fastqc

%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc LICENSE
%doc Help
%{installroot}/Configuration
%{installroot}/net
%{installroot}/org
%{installroot}/Templates
%{installroot}/uk
%{installroot}/jbzip2*
%{installroot}/sam*
%{installroot}/fastqc_icon.ico
%defattr(0755,root,root,0755)
%{installroot}/fastqc  
%{installroot}/bin
