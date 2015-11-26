# This is a sample spec file for wget

### define _topdir	 	/home/rpmbuild/rpms/nextclip
%define name			nextclip
%define release		1
%define version 	1.3.1
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 		Illumina Nextera Long Mate Pair analysis and processing tool.
License: 		GNU GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		/opt/bio
Group: 			Development/Tools
URL:			https://github.com/richardmleggett/nextclip
AutoReq:		yes
Patch0:			%{name}-%{version}-%{release}.patch0

%description
Illumina Nextera Long Mate Pair analysis and processing tool.

%prep
%setup -q -n %{name}-NextClip_v%{version}

%patch -P 0 -p1

%build
make --jobs

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r bin scripts examples $RPM_BUILD_ROOT%{installroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{installroot}/bin/nextclip
%attr(755, root, root) %{installroot}/scripts/*.pl
%attr(755, root, root) %{installroot}/scripts/*.sh
%{installroot}
