# This is a sample spec file for wget

### define _topdir	 	/home/rpmbuild/rpms/phyml
%define name		phyml
%define release		1
%define version 	20120412
%define buildroot	 %{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}

BuildRoot:		%{buildroot}
Summary: 		Phylogenetic estimation using Maximum Likelihood
License: 		GNU GPL
URL:			http://code.google.com/p/phyml/
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
PhyML is a software that estimates maximum likelihood phylogenies from alignments of nucleotide or amino acid sequences. The main strength of PhyML lies in the large number of substitution models coupled to various options to search the space of phylogenetic tree topologies, going from very fast and efficient methods to slower but generally more accurate approaches. PhyML was designed to process moderate to large data sets. In theory, alignments with up to 4,000 sequences 2,000,000 character-long can be processed.

%prep
%setup -q 
mkdir mpi 
cp -r AUTHORS COPYING ChangeLog INSTALL Makefile.am Makefile.in NEWS README aclocal.m4 bin config.guess config.h.in config.sub configure configure.ac depcomp doc examples install-sh ltmain.sh missing src mpi 

%build
./configure --prefix /opt/bio/phyml 
make
cd mpi 
./configure --prefix /opt/bio/phyml --enable-mpi 
make

%install
make install prefix=$RPM_BUILD_ROOT%{installroot} 
cd mpi 
make install prefix=$RPM_BUILD_ROOT%{installroot} 

%files
%defattr(755,root,root)
%{installroot}
