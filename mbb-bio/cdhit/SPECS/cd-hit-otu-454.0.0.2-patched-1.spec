
### define _topdir	 	/home/rpmbuild/rpms/cdhit
%define name		cd-hit-otu-454
%define release		1
%define version 	0.0.2
%define postfix		patched
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 		cd-hit
License: 		GPL-2|https://code.google.com/p/cdhit
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}-%{postfix}.tar.gz
Patch:			%{name}-%{version}-%{postfix}-1.patch
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
cd-hit-otu: Program for Operational Taxonomic Units (OTUs) finding in 454 data.

%prep
%setup -q -n %{name}-%{version}
%patch -p1

%build
cd cd-hit; make openmp=yes; make; cd ..
cd cdhit-dup; make

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -R *.pl cd-hit cd-hit-v4.5.5-2011-03-31 cdhit-dup $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
