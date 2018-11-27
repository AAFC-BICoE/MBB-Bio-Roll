### define _topdir	 	/home/rpmbuild/rpms/SOAPdenovo-Trans
%define name		SOAPdenovo-Trans
%define release		1
%define version 	v1.03
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
License: 		GPL v3
Summary: 		SOAPdenovo-Trans
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-src-%{version}.tar.gz
Prefix: 		%{_prefix}
Group: 			Development/Tools
AutoReq:		yes

%description
SOAPdenovo-Trans is a de novo transcriptome assembler basing on the SOAPdenovo framework, adapt to alternative splicing and different expression level among transcripts.The assembler provides a more accurate, complete and faster way to construct the full-length transcript sets. 

%prep
%setup -qn %{name}

%build

make
make 127mer=1

%install
mkdir -p $RPM_BUILD_ROOT%{_prefix}/bin
cp ../SOAPdenovo-Trans-127mer  $RPM_BUILD_ROOT%{_prefix}/bin
cp ../SOAPdenovo-Trans-31mer  $RPM_BUILD_ROOT%{_prefix}/bin
cp ../MANUAL $RPM_BUILD_ROOT%{_prefix}/
cp  ../VERSION $RPM_BUILD_ROOT%{_prefix}/
cp  ../LICENSE $RPM_BUILD_ROOT%{_prefix}/

%files
%defattr(755,root,root)
%{_bindir}/SOAPdenovo-Trans-127mer
%{_bindir}/SOAPdenovo-Trans-31mer

%defattr(644,root,root)
%doc %{_prefix}/MANUAL
%doc %{_prefix}/VERSION
%doc %{_prefix}/LICENSE

