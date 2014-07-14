# This is a  spec file for pftools

### define _topdir	 	/home/rpmbuild/rpms/pftools
%define name		pftools
%define release		1
%define version 	2.3
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	The pftools package contains all the software necessary to build protein and DNA generalized profiles and use them to scan and align sequences, and search databases.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	latest.tar.gz
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://web.expasy.org/pftools/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GNU GPL
AutoReq:	yes

%description
The pftools package contains all the software necessary to build protein and DNA
generalized profiles and use them to scan and align sequences, and search
databases. PFTOOLS are algorithms for searching the PROSITE database. There are
two tools: PFSCAN and PFSEARCH. PFSCAN compares a protein or nucleic acid
sequence against the PROSITE profile library. PFSEARCH compares a query profile
against the PROSITE. The result is an unsorted list of profile-sequence matches.
A variety of output formats containing different informations can be specified. 

%prep
%setup -q -n pftools

%build
make all

%install
mkdir -p %{buildroot}%{installroot}/bin
mkdir -p %{buildroot}/usr/share/man/man1
mkdir -p %{buildroot}/usr/share/man/man5
cp 2ft 6ft gtop pfmake pfscan pfw ptof htop pfscale pfsearch psa2msa ptoh %{buildroot}%{installroot}/bin
cp *.cmp *.prf *HUMAN CVPBR322 *.hmm *.txt *.seq *.lis *.gpr *.msf *.random test* README %{buildroot}%{installroot}
cd man
cp 2ft.1 6ft.1 gtop.1 htop.1 pfmake.1 pfscale.1 pfscan.1 pfsearch.1 pfw.1 psa2msa.1 ptof.1 ptoh.1 %{buildroot}/usr/share/man/man1
cp psa.5 xpsa.5  %{buildroot}/usr/share/man/man5


%files
%defattr(644,root,root)
%{installroot}
%doc 
/usr/share/man/man1/2ft.1.gz
/usr/share/man/man1/6ft.1.gz
/usr/share/man/man1/gtop.1.gz
/usr/share/man/man1/htop.1.gz
/usr/share/man/man1/pfmake.1.gz
/usr/share/man/man1/pfscale.1.gz
/usr/share/man/man1/pfscan.1.gz
/usr/share/man/man1/pfsearch.1.gz
/usr/share/man/man1/pfw.1.gz
/usr/share/man/man1/psa2msa.1.gz
/usr/share/man/man1/ptof.1.gz
/usr/share/man/man1/ptoh.1.gz
/usr/share/man/man5/psa.5.gz
/usr/share/man/man5/xpsa.5.gz
%defattr(755,root,root)
%{installroot}/bin/gtop
%{installroot}/bin/pfmake
%{installroot}/bin/pfscan
%{installroot}/bin/pfw
%{installroot}/bin/ptof
%{installroot}/bin/2ft
%{installroot}/bin/6ft
%{installroot}/bin/htop
%{installroot}/bin/pfscale
%{installroot}/bin/pfsearch
%{installroot}/bin/psa2msa
%{installroot}/bin/ptoh
