### define _topdir	 	/home/rpmbuild/rpms/muscle
%define name		muscle	
%define release		1
%define version 	3.8.31
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 		MUSCLE - Multiple Sequence Alignment
License: 		Public Domain
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}%{version}_src.tar.gz
#Patch:			%{name}-%{version}.patch
Prefix: 		/opt/bio
URL:			http://www.drive5.com/muscle/
Group: 			Development/Tools
AutoReq:		yes

%description
GARLI (Genetic Algorithm for Rapid Likelihood Inference) performs phylogenetic
searches on aligned sequence datasets using the maximum-likelihood criterion.
Version 0.96 is a major revision from the previous version 0.951. It includes
many new features, including the ability to perform tree inference using amino
acid and codon-based models, in addition to the standard nucleotide-based
models available in previous versions. On a practical level, the program is
able to perform maximum-likelihood tree searches on large datasets in a number
of hours.

%prep
%setup -q -n %{name}%{version}/src
#%patch -p 1

%build
make

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp muscle $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
