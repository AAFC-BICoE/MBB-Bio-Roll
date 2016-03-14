%define name		FastQC
### define _topdir	 	/home/rpmbuild/rpms/FastQC 
%define release		1
%define version 	0.11.5
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 

BuildRoot:		%{buildroot}
Summary: 		A quality control tool for high throughput sequence data.
License: 		GNU GPL
URL:			http://www.bioinformatics.babraham.ac.uk/projects/fastqc/
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		fastqc_v%{version}.zip
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes
Patch0:			fastqc_v%{version}.patch0

%description
FastQC aims to provide a simple way to do some quality control checks on raw sequence data coming from high throughput sequencing pipelines. It provides a modular set of analyses which you can use to give a quick impression of whether your data has any problems of which you should be aware before doing any further analysis.

The main functions of FastQC are

    Import of data from BAM, SAM or FastQ files (any variant)
    Providing a quick overview to tell you in which areas there may be problems
    Summary graphs and tables to quickly assess your data
    Export of results to an HTML based permanent report
    Offline operation to allow automated generation of reports without running the interactive application

%prep
%setup -q -n %{name} 
%patch -P 0 -p 1

%build
chmod 0775 fastqc #run this script to start the java compiled program

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
cp -r *  $RPM_BUILD_ROOT%{installroot} 
rm $RPM_BUILD_ROOT%{installroot}/*.bat 
#cp fastqc  $RPM_BUILD_ROOT%{installroot}/
#cp -r uk  $RPM_BUILD_ROOT%{installroot}/
#cp -r Contaminants  $RPM_BUILD_ROOT%{installroot}/
#cp -r Help  $RPM_BUILD_ROOT%{installroot}/
#cp README.txt  $RPM_BUILD_ROOT%{installroot}/

%files
%defattr(644,root,root,755)
%attr(0755,root,root) %{installroot}/fastqc  
#%attr(0766,root,root) %{installroot}/*.ico 
#%attr(0644,root,root) %{installroot}/*.txt
%{installroot}
