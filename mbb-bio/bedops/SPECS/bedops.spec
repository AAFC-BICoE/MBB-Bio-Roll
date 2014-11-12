# This is a sample spec file for wget

%global debug_package %{nil}

%define name		bedops
%define release		1
%define version 	2.4.2
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 


BuildRoot:		%{buildroot}
Summary: 		BEDOPS: the fast, highly scalable and easily-parallelizable genome analysis toolkit
License: 		GPLv2
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Packager:               Glen Newton <Glen.Newton@agr.gc.ca>
Prefix: 		/opt/bio
Group: 			Applications/BioInformatics/Genomics
AutoReq:		yes
URL:			http://bedops.readthedocs.org


%description
BEDOPS is an open-source command-line toolkit that performs highly efficient and scalable Boolean and other set operations, statistical calculations, archiving, conversion and other management of genomic data of arbitrary scale. Tasks can be easily split by chromosome for distributing whole-genome analyses across a computational cluster.


%prep
%setup -qn %{name}-%{version}

%build
make 


%install
make install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r bin $RPM_BUILD_ROOT%{installroot}


%files 
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin 
