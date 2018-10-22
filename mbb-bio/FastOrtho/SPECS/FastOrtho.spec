# This is a  spec file for velvet

%define name		FastOrtho
%define release		1
%define version 	433320
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	FastOrtho generates ortholog groups of sequences
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Packager:	Glen Newton glen.newton@agr.gc.ca
Source: 	%{name}-%{version}.zip
URL:            http://enews.patricbrc.org/fastortho/
Prefix: 	%{installroot}
Group: 		Development/Tools
License:        GPL-3
AutoReq:	yes

Requires:	java

%description

orthomcl starts with gene protein sequences grouped by genomes and generates
ortholog groups by creating input for the mcl program with input based on the
all by all blast of the sequences.

FastOrtho is a reimplementation of the orthomcl program that does not require
the use of databases or perl.

%prep
%setup -q -n %{name}-master

%build
cd src
#sed -i s/enable-auto-import/-enable-auto-import/g Makefile
make --jobs=`nproc`
strip FastOrtho

%install
mkdir -p %{buildroot}%{installroot}/bin

cp src/FastOrtho SetFast.jar %{buildroot}%{installroot}/bin

%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc ReadMe.txt 
%{installroot}/bin/SetFast.jar
%defattr(755,root,root,755)
%{installroot}/bin/FastOrtho
