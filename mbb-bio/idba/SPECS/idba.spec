%define name		idba
%define release		1
%define version 	1.1.3
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	IDBA includes IDBA-UD, IDBA-Hybrid, and IDBA-Tran, which is an iterative De Bruijn Graph De Novo short read assembler for transcriptome.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
Patch0:         maxshortsequence.patch
Patch1:         numu.patch
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>
URL:            http://i.cs.hku.hk/~alse/hkubrg/projects/idba_tran/
Prefix: 	%{installroot}
Group: 		BioInformatics/Assembler
License:        GPLv2
AutoReq:	yes

%description
All IDBA (iterative de Bruijn graph assembler) series assemblers are refined and
included in this package.
The basic IDBA is included only for comparison.  
IDBA-UD is a de novo genome assembler.  
IDBA-Hybrid is a reference-based genome assembler.  
IDBA-Tran is an iterative De Bruijn Graph De Novo short read assembler for
transcriptome. It is purely de novo assembler based on only RNA sequencing
reads. IDBA-Tran uses local assembly to reconstructing missing k-mers in
low-expressed transcripts and then employs progressive cutoff on contigs to
seperate the graph into components. Each component corresponds to one gene in
most cases and contains not many transcripts. A heuristic algorithm based on
pair-end reads is then used to find the isoforms. 

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
aclocal
autoconf
automake --add-missing
./configure --prefix=%{installroot}
make -pipe --jobs=`nproc`

%install
mkdir -p %{buildroot}%{installroot}
rm bin/*.o bin/Makefile* bin/test
rm -rf bin/.deps/
cp -r bin %{buildroot}%{installroot}

%files
%defattr(644,root,root)
%{installroot}
%doc AUTHORS
%doc README.md
%defattr(755,root,root,755)
%{installroot}/bin

