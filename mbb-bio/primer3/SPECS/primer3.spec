%define name		primer3
%define release		1
%define version 	2.4.0
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		Primer3 - PCR primer design tool
License: 		GPL
URL:			https://github.com/primer3-org/primer3
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.tar.gz
Prefix: 		%{_prefix}
Group: 			Bioinformatics/Primer Design
AutoReq:		yes

%description
Primer3 is a widely used program for designing PCR primers (PCR = "Polymerase
Chain Reaction"). PCR is an essential and ubiquitous tool in genetics and
molecular biology. Primer3 can also design hybridization probes and sequencing
primers.

%prep
%setup -q -n %{name}-%{version}/src

%build
make -j`nproc`

%install
mkdir -p %{buildroot}%{_bindir}
cp -r primer3_core primer3_masker ntdpal ntthal oligotm long_seq_tm_test %{buildroot}%{_bindir}
cp -r primer3_config  %{buildroot}%{_prefix}

%clean
cd ../../
rm -rf %{name}-%{version}

%files
%defattr(644,root,root,755) 
%dir %{_prefix}
%doc LICENSE
%doc primer3_manual.htm
%doc release_notes.txt
%{_prefix}/primer3_config
%defattr(755,root,root,755)
%{_bindir}
