# This is a sample spec file for wget

### define _topdir	 	/home/rpmbuild/rpms/%{name}
%define name			clustal-omega
%define src_name		clustal-omega
%define release		1
%define version 	1.2.1
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	Multiple alignment of nucleic acid and protein sequences 
License: 		GPL
Packager:	Glen Newton <Glen.Newton@agr.gc.ca>
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz
Prefix: 		/opt/bio
Group: 			Applications/BioInformatics
URL:			http://www.clustal.org/omega/
AutoReq:		yes
requires: argtable2


%description
Clustal Omega is the latest addition to the Clustal family. It offers a significant increase in scalability over previous versions, allowing hundreds of thousands of sequences to be aligned in only a few hours. It will also make use of multiple processors, where present. In addition, the quality of alignments is superior to previous versions, as measured by a range of popular benchmarks. 


%prep
%setup -q

%build
./configure  CFLAGS='-I /opt/bio/argtable2/include' LDFLAGS='-L/opt/bio/argtable2/lib'
make prefix=%{installroot}

%install
make install prefix=$RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root,755)
%{installroot}
