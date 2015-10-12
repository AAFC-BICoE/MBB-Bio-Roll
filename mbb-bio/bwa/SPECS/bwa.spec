# This is a sample spec file for wget

### define _topdir	 	/home/rpmbuild/rpms/bwa
%define name			bwa
%define release		1
%define version 	0.7.12
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 		Burrows-Wheeler Alignment Tool
License: 		GNU GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.bz2
Prefix: 		/opt/bio
Group: 			Development/Tools
URL:			http://bio-bwa.sourceforge.net/bwa.shtml
AutoReq:		yes

%description
BWA is a software package for mapping low-divergent sequences against a large reference genome, such as the human genome. It consists of three algorithms: BWA-backtrack, BWA-SW and BWA-MEM. The first algorithm is designed for Illumina sequence reads up to 100bp, while the rest two for longer sequences ranged from 70bp to 1Mbp. BWA-MEM and BWA-SW share similar features such as long-read support and split alignment, but BWA-MEM, which is the latest, is generally recommended for high-quality queries as it is faster and more accurate. BWA-MEM also has better performance than BWA-backtrack for 70-100bp Illumina reads.

%prep
%setup -q

%build
make --jobs

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
strip bwa
cp bwa *.pl $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
