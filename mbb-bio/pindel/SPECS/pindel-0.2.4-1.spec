# This is a  spec file for pindel

### define _topdir	 	/home/rpmbuild/rpms/pindel
%define name		pindel
%define release		1
%define version 	024t
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	pindel is a pattern growth approach to detect indels and structural variations.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}%{version}.tar.gz
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            https://trac.nbic.nl/pindel/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GNU GPL
AutoReq:	yes

%description
Pindel is a pattern growth approach to detect indels and structural variations.
Pindel can detect breakpoints of large deletions, medium sized insertions,
inversions, tandem duplications and other structural variants at single-based
resolution from next-gen sequence data. It uses a pattern growth approach to
identify the breakpoints of these variants from paired-end short reads. 

%prep
%setup -q -n pindel024t

%build

%install
mkdir -p %{buildroot}%{installroot}
./INSTALL $PWD/samtools
cp pindel pindel2vcf sam2pindel %{buildroot}%{installroot}

%files
%defattr(755,root,root)
%{installroot}
