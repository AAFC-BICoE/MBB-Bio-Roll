# This is a sample spec file for wget
# TODO: Add documentation 
#
### define _topdir	 	/home/rpmbuild/rpms/tophat
%define name		tophat
%define release		1
%define version 	2.0.5 
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}


BuildRoot:		%{buildroot}
Summary: 		A spliced read mapper for RNA-Seq
License: 		BOOST Software License
URL:			http://tophat.cbcb.umd.edu/
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz 
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
TopHat is a fast splice junction mapper for RNA-Seq reads. It aligns RNA-Seq reads to mammalian-sized genomes using the ultra high-throughput short read aligner Bowtie, and then analyzes the mapping results to identify splice junctions between exons. 

%prep
%setup -q 

%build
./configure  --with-boost=/opt/bio/boost --with-bam=/opt/bio/samtools --prefix=%{installroot}
make 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install prefix=$RPM_BUILD_ROOT%{installroot}


%files
%defattr(755,root,root)
%{installroot}
