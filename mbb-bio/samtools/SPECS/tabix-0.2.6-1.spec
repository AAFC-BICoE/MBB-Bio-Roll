### define _topdir	 	/home/rpmbuild/rpms/samtools
%define name			tabix
%define release		1
%define version 	0.2.6
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 		Tabix: fast retrieval of sequence features from generic TAB-delimited files.
License: 		MIT|http://seqanswers.com/wiki/SAMtools
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.bz2
#Patch:			%{name}-%{version}.patch
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes
Url: http://samtools.sourceforge.net/

%description
Tabix indexes a TAB-delimited genome position file in.tab.bgz and creates an
index file in.tab.bgz.tbi when region is absent from the command-line. The
input data file must be position sorted and compressed by bgzip which has a
gzip(1) like interface. After indexing, tabix is able to quickly retrieve data
lines overlapping regions specified in the format "chr:beginPos-endPos". Fast
data retrieval also works over network if URI is given as a file name and in
this case the index file will be downloaded if it is not present locally.

%prep
%setup -q
#%patch -p 1

%build
make

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp tabix tabix.py bgzip $RPM_BUILD_ROOT%{installroot}

%files
%defattr(-,root,root)
%{installroot}
