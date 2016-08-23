### define _topdir	 	/home/rpmbuild/rpms/mothur
%define name		mothur
%define release		1
%define version 	1.38.1.1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/mothur
%define boost_inc	/opt/bio/lib/boost/include
%define boost_lib	/opt/bio/lib/boost/lib

BuildRoot:		%{buildroot}
Summary: 		The mothur metagenomics analysis package
License: 		Open Source
URL:			http://www.mothur.org/
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Packager:		Iyad Kandalaft <iyad.kandalaft@agr.gc.ca>
Prefix: 		/opt/bio
Group: 			Development/Tools
BuildRequires:		boost-devel
BuildRequires:		boost-iostreams
AutoReq:		yes

%description
The goal of mothur is to have a single resource to analyze molecular data that is used by microbial ecologists. Many of these tools are available elsewhere as individual programs and as scripts, which tend to be slow or as web utilities, which limit your ability to analyze your data. mothur offers the ability to go from raw sequences to the generation of visualization tools to describe α and β diversity.

%prep
%setup -q 

%build
make -j$(nproc) BOOST_INCLUDE_DIR=%{boost_inc} BOOST_LIBRARY_DIR=%{boost_lib}

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp mothur uchime $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root,755)
%{installroot}/mothur
%{installroot}/uchime
