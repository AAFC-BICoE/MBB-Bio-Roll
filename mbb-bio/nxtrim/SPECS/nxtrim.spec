### %define _topdir     /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/nxtrim
%define name            nxtrim
%define release		1         
%define version         0.4  
%define installroot     /opt/bio/%{name}

Summary:   Software to remove Nextera Mate Pair adapters and categorise reads according to the orientation implied by the adapter location.
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    %{name}-%{version}.zip
License:   BSD 2-Clause
Packager:  Alex MacLean <alex.maclean@agr.gc.ca>
Group:     Development/Tools
Prefix:    /opt/bio
Vendor:    Illumina, Inc. <joconnell@illumina.com>
Url:       https://github.com/sequencing/NxTrim
AutoReq:   no

%description
Software to remove Nextera Mate Pair adapters and categorise reads according to the orientation implied by the adapter location.

%prep
%setup -q -n NxTrim-master

%build
make


%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp nxtrim mergeReads $RPM_BUILD_ROOT%{installroot}/

%clean

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/nxtrim
%{installroot}/mergeReads
