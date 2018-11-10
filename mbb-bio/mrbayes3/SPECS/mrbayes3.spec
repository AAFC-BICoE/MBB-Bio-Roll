%define name		MrBayes
%define src_name	mrbayes
%define release		1
%define version 	3.2.6
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		A free software program which performs Bayesian inference of phylogeny. 
License: 		GNU GPL
URL:			http://mrbayes.sourceforge.net/
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz
Patch0:			beagle-getversion-undefined.patch
Prefix: 		%{_prefix}
Group:			Bioinformatics/Phylogenetics
AutoReq:		yes

BuildRequires:		opt-beagle-lib
Requires:		opt-beagle-lib

%description
MrBayes is a program for Bayesian inference and model choice across a wide range of phylogenetic and evolutionary models. MrBayes uses Markov chain Monte Carlo (MCMC) methods to estimate the posterior distribution of model parameters.

%prep
%setup -qn %{src_name}-%{version}
%patch0 -p 1

%build

BEAGLELIB_PREFIX=$(dirname $(dirname $(rpm -ql opt-beagle-lib | grep libhmsbeagle.so | head -n 1)))
BEAGLELIB_LIBDIR=$(dirname $(rpm -ql opt-beagle-lib | grep libhmsbeagle.so | head -n 1))

export LDFLAGS=-Wl,-rpath,$BEAGLELIB_LIBDIR

cd ./src 
autoconf 
./configure --with-beagle=$BEAGLELIB_PREFIX --enable-mpi 
make -j

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cd ./src
# Custom make file: DESTDIR is not supported.
make install prefix=%{buildroot}%{installroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc documentation/commref*
%doc documentation/Manual_%{name}_*.pdf
%doc documentation/release_note.txt
%doc examples
%defattr(755,root,root,755)
%{_bindir}
