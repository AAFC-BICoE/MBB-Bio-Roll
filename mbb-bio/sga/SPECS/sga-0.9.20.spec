# This is a  spec file for sga
#
### define _topdir	 	/home/rpmbuild/rpms/sga
%define name		sga
%define release		2
%define version 	0.9.20
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	sga is a genome assembler
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
Patch:		%{name}-%{version}-%{release}.patch
URL:            https://github.com/jts/sga/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GNU GPL
AutoReq:	yes

%description
SGA - String Graph Assembler is a de novo genome assembler based on the concept
of string graphs. The major goal of SGA is to be very memory efficient, which
is achieved by using a compressed representation of DNA sequence reads.


%prep
%setup -q -n %{name}-%{version}/src
%patch -p2

%build
./autogen.sh
mkdir -p %{buildroot}%{installroot}
./configure --with-sparsehash=/opt/bio/sparsehash --with-bamtools=/opt/bio/bamtools --with-hoard=/opt/bio/hoard --prefix=%{installroot}
make         

%install
make install   prefix=%{buildroot}%{installroot}

%files
%defattr(755,root,root)
%{installroot}
