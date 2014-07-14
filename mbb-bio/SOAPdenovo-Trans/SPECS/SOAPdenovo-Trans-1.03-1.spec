# This is a sample spec file for wget

### define _topdir	 	/home/rpmbuild/rpms/SOAPdenovo-Trans
%define name		SOAPdenovo-Trans
%define release		1
%define version 	v1.03
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
License: 		GPL v3
Summary: 		SOAPdenovo-Trans
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-src-%{version}.tar.gz
Prefix: 		/opt/bio
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
mkdir -p $RPM_BUILD_ROOT%{installroot}/bin
cp ../SOAPdenovo-Trans-127mer  $RPM_BUILD_ROOT%{installroot}/bin
cp ../SOAPdenovo-Trans-31mer  $RPM_BUILD_ROOT%{installroot}/bin
cp ../MANUAL $RPM_BUILD_ROOT%{installroot}/
cp  ../VERSION $RPM_BUILD_ROOT%{installroot}/
cp  ../LICENSE $RPM_BUILD_ROOT%{installroot}/

%files
%defattr(755,root,root)
%{installroot}/bin/SOAPdenovo-Trans-127mer
%{installroot}/bin/SOAPdenovo-Trans-31mer

%defattr(644,root,root)
%{installroot}/MANUAL
%{installroot}/VERSION
%{installroot}/LICENSE
