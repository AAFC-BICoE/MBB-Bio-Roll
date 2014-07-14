# This is a  spec file for mira genome assembler

### define _topdir	 	/home/rpmbuild/rpms/RAxML
%define name		RAxML
%define release		1
%define version 	7.3.1
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary:        Randomized Axelerated Maximum likelihood
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	stamatak-standard-%{name}-8495fec.zip
URL:            http://www.exelixis-lab.org/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GNU GPL
AutoReq:	yes

%description
RAxML (Randomized Axelerated Maximum Likelihood) is a program for sequential and parallel Maximum
Likelihood [1] based inference of large phylogenetic trees. It has originally been derived from fastDNAml
which in turn was derived from Joe Felsentein’s dnaml which is part of the PHYLIP [2] package.


%prep
%setup -q -n stamatak-standard-RAxML-8495fec

%build
make -f Makefile.gcc 

%install
#make -f Makefile.gcc install prefix=$RPM_BUILD_ROOT%{installroot}
mkdir -p $RPM_BUILD_ROOT%{installroot} 
cp ./raxmlHPC $RPM_BUILD_ROOT%{installroot} 

%files
%defattr(755,root,root)
%{installroot}
