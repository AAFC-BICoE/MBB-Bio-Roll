### define _topdir	 	/home/rpmbuild/rpms/bamtools
%define name		bamtools
%define release		1
%define version 	2.4.1
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary:	BamTools provides both a programmer's API and an end-user's toolkit for BAM files.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
URL:		https://github.com/pezmaster31/bamtools 
Prefix: 	/opt/bio
Group: 		Development/Libraries
License:        MIT License
AutoReq:	yes

%description
BamTools is a project that provides both a C++ API and a command-line toolkit for reading, writing, and manipulating BAM (genome alignment) files.

%prep
%setup -q

%build
mkdir build 
cd build
cmake ..
make -pipe --jobs=`nproc` 

%install
mkdir -p %{buildroot}%{installroot}
cp -R bin %{buildroot}%{installroot}
strip bin/*
cp -R lib %{buildroot}%{installroot}
cp -R include %{buildroot}%{installroot}



%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin


