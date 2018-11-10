%define name		nextclip
%define release		1
%define version 	1.3.1
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define installroot	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		Illumina Nextera Long Mate Pair analysis and processing tool.
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		%{_prefix}
Group: 			Development/Tools
URL:			https://github.com/richardmleggett/nextclip
AutoReq:		yes
Patch0:			env-perl.patch

%global __requires_exclude ^perl

Requires:	opt-perl(Cwd)
Requires:	opt-perl(File::Basename)
Requires:	opt-perl(Getopt::Long)
Requires:	opt-perl(strict)
Requires:	opt-perl(warnings)

%description
Illumina Nextera Long Mate Pair analysis and processing tool.

%prep
%setup -q -n %{name}-NextClip_v%{version}
%patch0 -p1

%build
make -j`nproc`

%install
mkdir -p %{buildroot}%{_prefix} 
cp -r bin scripts examples %{buildroot}%{_prefix} 

%files
%defattr(644,root,root,755)
%doc LICENSE
%doc README.md
%{_prefix}/examples
%defattr(755,root,root,755)
%{_prefix}/bin/nextclip
%{_prefix}/scripts/*.pl
%{_prefix}/scripts/*.sh
%{_prefix}/scripts/*.R
