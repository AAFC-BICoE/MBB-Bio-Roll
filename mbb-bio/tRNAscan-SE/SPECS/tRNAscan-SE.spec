%define		name		tRNAscan-SE
%define		src_name	trnascan-se
%define		release		1
%define		version 	2.0.0
%define		installroot 	/opt/bio/%{name}
%define		buildroot	%{_topdir}/%{src_name}-%{version}-root
%define		_prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	tRNAscan-SE is a program for improved detection of transfer RNA genes in genomic sequences.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{src_name}-%{version}.tar.gz
Patch0:         %{src_name}-%{version}-%{release}.patch0
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://lowelab.ucsc.edu/tRNAscan-SE/
Prefix: 	%{installroot}
Group: 		Development/Tools
License:        GPL-2
AutoReq:	yes

%global         __requires_exclude ^perl
%global         __provides_exclude ^perl

provides:	opt-perl(tRNAscan::Stats)
provides:	opt-perl(tRNAscanSE::ArrayCMscanResults)
provides:	opt-perl(tRNAscanSE::ArraytRNA)
provides:	opt-perl(tRNAscanSE::CM)
provides:	opt-perl(tRNAscanSE::CMscanResultFile)
provides:	opt-perl(tRNAscanSE::Configuration)
provides:	opt-perl(tRNAscanSE::Eufind)
provides:	opt-perl(tRNAscanSE::FpScanResultFile)
provides:	opt-perl(tRNAscanSE::GeneticCode)
provides:	opt-perl(tRNAscanSE::IntResultFile)
provides:	opt-perl(tRNAscanSE::LogFile)
provides:	opt-perl(tRNAscanSE::MultiResultFile)
provides:	opt-perl(tRNAscanSE::Options)
provides:	opt-perl(tRNAscanSE::ResultFileReader)
provides:	opt-perl(tRNAscanSE::SS)
provides:	opt-perl(tRNAscanSE::ScanResult)
provides:	opt-perl(tRNAscanSE::Sequence)
provides:	opt-perl(tRNAscanSE::SprinzlAlign)
provides:	opt-perl(tRNAscanSE::SprinzlAlignResults)
provides:	opt-perl(tRNAscanSE::SprinzlPos)
provides:	opt-perl(tRNAscanSE::Tscan)
provides:	opt-perl(tRNAscanSE::Utils)
provides:	opt-perl(tRNAscanSE::tRNA)



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
%setup -qn %{src_name}-%{version}
#%patch -P 0 -p1

%build
./configure --prefix=%{_prefix}
make 

%install

mkdir -p %{buildroot}%{installroot}/bin  %{buildroot}%{installroot}/lib %{buildroot}/usr/share/perl5 %{buildroot}/usr/share/man/man1
cp -r tRNAscan-SE bin/trnascan-1.4 bin/covels-SE bin/coves-SE bin/eufindtRNA %{buildroot}%{installroot}/bin

cp lib/models/*cm lib/gcode/gcode.* %{buildroot}%{installroot}/lib

cp -r lib/tRNAscanSE/  %{buildroot}/usr/share/perl5
#cp x y
#cp -r Cove Demo %{buildroot}%{installroot}/lib
#cp TPCsignal Dsignal *.cm gcode.* %{buildroot}%{installroot}/lib
#mv tRNAscan-SE.man tRNAscan-SE.1
#cp tRNAscan-SE.1 %{buildroot}/usr/share/man/man1
#cp -r tRNAscanSE %{buildroot}/usr/share/perl5
#chmod -x %{buildroot}%{installroot}/bin/*

%files
%defattr(644,root,root,755)
%doc LICENSE
%doc COPYING
%defattr(-,root,root)
%{_prefix}/lib

%defattr(0755,root,root,0755)
%{_bindir}
/usr/share/perl5/tRNAscanSE

#%defattr(644,root,root,755)
#%{installroot}
#%defattr(755,root,root,755)
#%{installroot}/bin/covels-SE
#%{installroot}/bin/coves-SE
#%{installroot}/bin/eufindtRNA
#%{installroot}/bin/trnascan-1.4
#%{installroot}/bin/tRNAscan-SE
#/usr/share/man/man1/tRNAscan-SE.1.gz
#
# make files in bin directory executables in post section
#%post
#chmod +x %{installroot}/bin/*
