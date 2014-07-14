# This is a  spec file for tRNAscan-SE

### define _topdir	 	/home/rpmbuild/rpms/tRNAscan-SE
%define name		tRNAscan-SE
%define release		2
%define version 	1.3.1
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	tRNAscan-SE is a program for improved detection of transfer RNA genes in genomic sequences.

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}.tar.gz
Patch0:         %{name}-%{version}-%{release}.patch0
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://lowelab.ucsc.edu/tRNAscan-SE/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPL-2|http://lowelab.ucsc.edu/tRNAscan-SE/Manual/node22.html#SECTION000100000000000000000
AutoReq:	yes

%description
tRNAscan-SE is is a program for improved detection of transfer RNA genes in
genomic sequences. tRNAscan-SE was written in the PERL (version 5.0) script
language.  Input consists of DNA or RNA sequences in FASTA format. tRNA
predictions are output in standard tabular or ACeDB format.  tRNAscan-SE does
no tRNA detection itself, but instead combines the strengths of three
independent tRNA prediction programs by negotiating the flow of information
between them, performing a limited amount of post-processing, and outputting
the results in one of several formats.

%prep
%setup -q
%patch -P 0 -p1

%build
make

%install
mkdir -p %{buildroot}%{installroot}/bin  %{buildroot}%{installroot}/lib %{buildroot}/usr/share/perl5 %{buildroot}/usr/share/man/man1
cp -r tRNAscan-SE trnascan-1.4 covels-SE coves-SE eufindtRNA %{buildroot}%{installroot}/bin
cp -r Cove Demo %{buildroot}%{installroot}/lib
cp TPCsignal Dsignal *.cm gcode.* %{buildroot}%{installroot}/lib
mv tRNAscan-SE.man tRNAscan-SE.1
cp tRNAscan-SE.1 %{buildroot}/usr/share/man/man1
cp -r tRNAscanSE %{buildroot}/usr/share/perl5
chmod -x %{buildroot}%{installroot}/bin/*

%files
%defattr(644,root,root,755)
%{installroot}
/usr/share/perl5/tRNAscanSE
%defattr(755,root,root,755)
%{installroot}/bin/covels-SE
%{installroot}/bin/coves-SE
%{installroot}/bin/eufindtRNA
%{installroot}/bin/trnascan-1.4
%{installroot}/bin/tRNAscan-SE
%doc
/usr/share/man/man1/tRNAscan-SE.1.gz

# make files in bin directory executables in post section
%post
chmod +x %{installroot}/bin/*
