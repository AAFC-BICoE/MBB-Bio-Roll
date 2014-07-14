# for use with QIIME, the environment variable RDP_JAR_PATH must be set to the location of the .jar, which in this case 
# will be /opt/bio/rdp_classifier/

%define name		rdp_classifier 
### define _topdir	 	/home/rpmbuild/rpms/rdp_classifier 
%define release		1
%define version 	2.2 
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 
%define __jar_repack	0

BuildRoot:		%{buildroot}
Summary: 		RDP Classifier
License: 		GNU GPL
URL:			http://rdp-classifier.sourceforge.net/
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}_%{version}.zip
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
The RDP Classifier is a naive Bayesian classifier that can rapidly and accurately provides taxonomic assignments from domain to genus, with confidence estimates for each assignment. More information can be found at http://rdp.cme.msu.edu/.

%prep
%setup -qn %{name}_%{version}


%build
#jar already created, nothing to build 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
cp -r rdp_classifier-2.2.jar lib  $RPM_BUILD_ROOT%{installroot}/

%files
%defattr(644,root,root,755)
%{installroot}
