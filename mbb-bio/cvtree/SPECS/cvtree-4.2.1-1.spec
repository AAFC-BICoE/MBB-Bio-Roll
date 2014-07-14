# This is a  spec file for CVTree

### define _topdir	 	/home/rpmbuild/rpms/cvtree
%define name		cvtree
%define release		1
%define version 	4.2.1
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	CVTree is an alignment free program which generates a dissimilarity matrix from comparatively large collection of DNA or Amino Acid sequences, preferably whole genome data.

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://tlife.fudan.edu.cn/cvtree
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPL-2 or GPL-3|http://www.inside-r.org/packages/cran/tree/docs/cv.tree	
AutoReq:	yes

%description
CVTree is an alignment free program which generates a dissimilarity matrix from
comparatively large collection of DNA or Amino Acid sequences, preferably whole
genome data.

%prep
%setup -q

%build
make

%install
mkdir -p %{buildroot}%{installroot}
cp cvtree dist *.pl %{buildroot}%{installroot}

%files
%defattr(755,root,root)
%{installroot}
