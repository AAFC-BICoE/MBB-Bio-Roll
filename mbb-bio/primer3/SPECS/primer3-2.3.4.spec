### define _topdir	 	/home/rpmbuild/rpms/primer3
%define name		primer3
%define release		3
%define version 	2.3.4
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 		Primer3 - PCR primer design tool
License: 		GNU GPL
URL:			AAFC-AAC/limic
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
#Patch:			%{name}-%{version}.patch
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
Primer3 is a widely used program for designing PCR primers (PCR = "Polymerase
Chain Reaction"). PCR is an essential and ubiquitous tool in genetics and
molecular biology. Primer3 can also design hybridization probes and sequencing
primers.

%prep
%setup -q -n %{name}-%{version}/src
#%patch -p 1

%build
make

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r primer3_core ntdpal ntthal oligotm long_seq_tm_test $RPM_BUILD_ROOT%{installroot}
cp -r primer3_config  $RPM_BUILD_ROOT/opt

%files
%defattr(755,root,root) 
%{installroot} 
%defattr(644,root,root,755)
/opt/primer3_config 

