%define name		FungalITSextractor
%define release		1
%define version 	1.0 
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 


BuildRoot:		%{buildroot}
Summary: 		FungalITSextractor 
License: 		GNU GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}.zip
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes
URL:			http://www.emerencia.org/FungalITSextractor.html

Requires: 		hmmer2
Requires:		perl(strict)

%global __requires_exclude ^perl

%description
Extraction of ITS1/ITS2 from fungal ITS sequences in the FASTA format


%prep 
%setup -q -n %{name}

%build
#program is a perl script, nothing to do 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
chmod 0755 * 
chmod 666 HMMs/* 
cp  -r %{name}.pl HMMs $RPM_BUILD_ROOT%{installroot}
mkdir $RPM_BUILD_ROOT%{installroot}/indata 
mkdir $RPM_BUILD_ROOT%{installroot}/outdata 

%files
%defattr(-,root,root)
%dir %attr(0755,root,root) %{installroot}
%dir %attr(0755,root,root) %{installroot}/HMMs
%dir %attr(0755,root,root) %{installroot}/indata
%dir %attr(0755,root,root) %{installroot}/outdata
%attr(0755,root,root) %{installroot}/FungalITSextractor.pl 
%{installroot}
