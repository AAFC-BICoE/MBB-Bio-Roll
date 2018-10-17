%define name		clustal-omega
%define src_name	clustal-omega
%define release		1
%define version 	1.2.4
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		Multiple alignment of nucleic acid and protein sequences 
License: 		GPL
Packager:		Glen Newton <Glen.Newton@agr.gc.ca>
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz
Prefix: 		%{installroot}
Group: 			BioInformatics/Alignment
URL:			http://www.clustal.org/omega/
AutoReq:		yes

BuildRequires: 		opt-argtable2
Requires:		opt-argtable2

%description
Clustal Omega is the latest addition to the Clustal family. It offers a significant increase in scalability over previous versions, allowing hundreds of thousands of sequences to be aligned in only a few hours. It will also make use of multiple processors, where present. In addition, the quality of alignments is superior to previous versions, as measured by a range of popular benchmarks. 

%prep
%setup -q

%build
ARGTABLE_INCLUDE=$(dirname $(rpm -ql opt-argtable2 | grep "argtable2.h$" | head -n 1))
ARGTABLE_LIB=$(dirname $(rpm -ql opt-argtable2 | grep "libargtable2.so$" | head -n 1))
./configure prefix=%{installroot} CFLAGS="-I$ARGTABLE_INCLUDE" LDFLAGS="-L$ARGTABLE_LIB"
make -j`nproc`

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc COPYING
%doc NEWS
%doc AUTHORS
%doc ChangeLog
%defattr(755,root,root,755)
%{installroot}/bin
