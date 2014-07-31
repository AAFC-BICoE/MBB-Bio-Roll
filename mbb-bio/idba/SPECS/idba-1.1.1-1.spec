# This is a  spec file for IDBA
%define debug_package %{nil}

%define name		idba
%define release		1
%define version 	1.1.1
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	IDBA includes IDBA-UD, IDBA-Hybrid, and IDBA-Tran, which is an iterative De Bruijn Graph De Novo short read assembler for transcriptome.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}-%{release}.patch0
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://i.cs.hku.hk/~alse/hkubrg/projects/idba_tran/
Prefix: 	/opt/bio
Group: 		Applications/BioInformatics/Assembler
License:        GPL-2|https://code.google.com/p/hku-idba/
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
%patch -P 0 -p1

%build
./configure
make   -pipe --jobs=`nproc` 

%install
mkdir -p %{buildroot}%{installroot}/bin
mkdir -p %{buildroot}%{installroot}/script
cp bin/* %{buildroot}%{installroot}/bin
cd bin;  file * | grep "not stripped"|grep -Eo '^[^ ]+'|sed "s/://"|xargs strip; cd ..
rm %{buildroot}%{installroot}/bin/*.*
rm %{buildroot}%{installroot}/bin/Makefile
cd script
cp *.py validate* %{buildroot}%{installroot}/script

%files
%defattr(755,root,root)
%{installroot}
