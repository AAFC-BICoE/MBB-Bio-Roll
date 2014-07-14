
### define _topdir	 	/home/rpmbuild/rpms/cdhit
%define name		cd-hit
%define release		2
%define prefix		v
%define version 	4.6.1
%define date		2012-08-27
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 		cd-hit
License: 		GPL-2|https://code.google.com/p/cdhit
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{prefix}%{version}-%{date}.tgz
Patch:			%{name}-%{prefix}%{version}-%{date}-1.patch
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
CD-HIT is a program for clustering DNA/protein sequence database at high
identity with tolerance.

%prep
%setup -q -n cd-hit-v4.6.1-2012-08-27
%patch -p1

%build
make openmp=yes

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install PREFIX=$RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
