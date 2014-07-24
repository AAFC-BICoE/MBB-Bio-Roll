%define debug_package %{nil}

%define name		sigoli 
%define release		1
%define version 	1.1
%define srcVersion 	1-1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}


BuildRoot:		%{buildroot}
Summary: 		Signature Oligo
License: 		GPL 
URL:			http://www.ncbi.nlm.nih.gov/pubmed/21564971
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{srcVersion}.tar.gz 
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes
BuildRequires: 		glibc-static 
BuildRequires: 		bison 
BuildRequires: 		flex 

%description
Part of Wen's automated oligo design pipeline, sigoli is used to search for
unique oligos, given a directory of FASTA-formatted sequences. 

%prep
%setup -qn %{name}-%{srcVersion}

%build
make 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp b/sigoli $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
