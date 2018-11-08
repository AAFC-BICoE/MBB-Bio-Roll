%define name		mothur
%define release		1
%define version 	1.40.5
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/mothur
%define	_prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		The mothur metagenomics analysis package
License: 		Open Source
URL:			http://www.mothur.org/
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.tar.gz
Packager:		Iyad Kandalaft <iyad.kandalaft@agr.gc.ca>
Prefix: 		%{_prefix}
Group: 			Bioinformatics/Metagenomics

BuildRequires:		opt-boost-devel
BuildRequires:		opt-boost-iostreams
Requires:		opt-boost-iostreams
AutoReq:		yes

%description
The goal of mothur is to have a single resource to analyze molecular data that is used by microbial ecologists. Many of these tools are available elsewhere as individual programs and as scripts, which tend to be slow or as web utilities, which limit your ability to analyze your data. mothur offers the ability to go from raw sequences to the generation of visualization tools to describe α and β diversity.

%prep
%setup -q 

%build

BOOST_INCLUDE=$(dirname $(dirname $(rpm -ql opt-boost-devel | grep 'any.hpp$' | head -n 1)))
BOOST_LIB=$(dirname $(rpm -ql opt-boost-iostreams | grep 'libboost_iostreams.so' | head -n 1))
export LD_RUN_PATH=$BOOST_LIB
make -j$(nproc) BOOST_INCLUDE_DIR=$BOOST_INCLUDE BOOST_LIBRARY_DIR=$BOOST_LIB USEREADLINE=no 

%install
mkdir -p %{buildroot}%{_bindir}
mv mothur uchime %{buildroot}%{_bindir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc LICENSE.md
%defattr(755,root,root,755)
%{_bindir}
