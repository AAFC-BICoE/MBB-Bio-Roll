%define name		pindel
%define release		1
%define version 	0.2.5b8
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	pindel is a pattern growth approach to detect indels and structural variations.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	https://github.com/genome/pindel/archive/v%{version}.tar.gz
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>
URL:            https://trac.nbic.nl/pindel/
Prefix: 	%{_prefix}
Group: 		Bioinformatics/Indels	
License:        GNU GPL
AutoReq:	yes

BuildRequires:	opt-htslib
Requires:	opt-htslib

%global __requires_exclude ^libhts.so.2

%description
Pindel is a pattern growth approach to detect indels and structural variations.
Pindel can detect breakpoints of large deletions, medium sized insertions,
inversions, tandem duplications and other structural variants at single-based
resolution from next-gen sequence data. It uses a pattern growth approach to
identify the breakpoints of these variants from paired-end short reads. 

%prep
%setup -q -n %{name}-%{version}

%build
HTSLIB_LIBDIR=$(dirname $(rpm -ql opt-htslib | grep libhts.so | head -n1 ))
HTSLIB_PREFIX=$(rpm -q --queryformat '%{instprefixes}' opt-htslib)
LDFLAGS=-L$HTSLIB_LIBDIR ./INSTALL $HTSLIB_PREFIX

%install
mkdir -p %{buildroot}%{_bindir}
cp pindel pindel2vcf sam2pindel %{buildroot}%{_bindir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc COPYING.txt
%doc README.md
%defattr(755,root,root,755)
%{_bindir}
