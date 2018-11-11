%define name            NxTrim
%define release		1      
%define version         0.4.3
%define installroot     /opt/bio/%{name}
%define _prefix		%{installroot}

Summary:	Software to remove Nextera Mate Pair adapters and categorise reads according to the orientation implied by the adapter location.
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source:		%{name}-v%{version}.tar.gz
License:	BSD
Packager:	Alex MacLean <alex.maclean@agr.gc.ca>
Group:		Development/Tools
Prefix:		%{_prefix}
Vendor:		Illumina, Inc. <joconnell@illumina.com>
Url:		https://github.com/sequencing/NxTrim
AutoReq:	yes

%description
Software to remove Nextera Mate Pair adapters and categorise reads according to the orientation implied by the adapter location.

%prep
%setup -q -n %{name}-%{version}

%build
make 

%install
mkdir -p %{buildroot}%{_bindir}
cp nxtrim scripts/*.py %{buildroot}%{_bindir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc LICENSE.txt
%doc README.md
%doc Changelog
%defattr(755,root,root,755)
%{_bindir}
