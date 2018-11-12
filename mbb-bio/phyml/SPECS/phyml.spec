%define name		phyml
%define release		1
%define version 	3.3.20180621
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		Phylogenetic estimation using Maximum Likelihood
License: 		GPL
URL:			http://code.google.com/p/phyml/
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.tar.gz
Prefix: 		%{_prefix}
Group: 			Bioinformatics/Phylogenetics	
AutoReq:		yes

%description
PhyML is a software that estimates maximum likelihood phylogenies from alignments of nucleotide or amino acid sequences. The main strength of PhyML lies in the large number of substitution models coupled to various options to search the space of phylogenetic tree topologies, going from very fast and efficient methods to slower but generally more accurate approaches. PhyML was designed to process moderate to large data sets. In theory, alignments with up to 4,000 sequences 2,000,000 character-long can be processed.

%prep
%setup -q 
%setup -q -D -T -a 0
mv %{name}-%{version} phyml-mpi

%build
./autogen.sh
# BEAGLE build seems to have compile errors
#BEAGLE_PC=$(dirname $(rpm -ql opt-beagle-lib | grep 'hmsbeagle-1.pc$' | head -n 1))
#PKG_CONFIG_PATH=$BEAGLE_PC:$PKG_CONFIG_PATH ./configure --prefix %{_prefix}

./configure --enable-phyml --prefix=%{_prefix}
make -j`nproc`
pushd phyml-mpi
./configure --enable-mpi --enable-phyml --prefix=%{_prefix}
make -j

%install
make install DESTDIR=%{buildroot}
pushd phyml-mpi
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc doc/phyml-manual.pdf
%defattr(755,root,root,755)
%{_bindir}
