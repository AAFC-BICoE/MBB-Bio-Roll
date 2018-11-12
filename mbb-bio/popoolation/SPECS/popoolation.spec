%define name		popoolation 
%define release		1
%define version 	1.2.2
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

BuildRoot:		%{buildroot}
Summary: 		PoPoolation is a collection of tools to facilitate population genetic studies of next generation sequencing data from pooled individuals
License: 		BSD
URL:			https://code.google.com/p/popoolation/
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}_%{version}.zip
Patch0:			perl-lib-path.patch
Patch1:			env-perl.patch
Prefix: 		%{_prefix}
Group: 			Bioinformatics/Population Genetics
AutoReq:		yes

%global __requires_exclude ^perl
%global __provides_exclude ^perl
Requires:		opt-perl(Data::Dumper)
Requires:		opt-perl(Exporter)
Requires:		opt-perl(FindBin)
Requires:		opt-perl(Math::BigRat)
Requires:		opt-perl(lib)
Requires:		opt-perl(strict)
Requires:		opt-perl(warnings)

%description
Currently next generation sequencing (NGS) technologies are mainly used to sequence individuals. However, the high coverage required and the resulting costs may be prohibitive for population scale studies. Sequencing pools of individuals instead may often be more cost effective and more accurate than sequencing individuals. PoPoolation is a pipeline for analysing pooled next generation sequencing data. PoPoolation builds upon open source tools (bwa, samtools) and uses standard file formats (gtf, sam, pileup) to ensure a wide compatibility. Currently PoPoolation allows to calculate Tajima’s Pi, Watterson’s Theta and Tajima’s D for reference sequences using a sliding window approach. Alternatively these population genetic estimators may be calculated for a set of genes (provided as gtf). One of the main challenges in population genomics is to identify regions of intererest on a genome wide scale. We believe that PoPoolation will greatly aid this task by allowing a fast and user friendly analysis of NGS data from DNA pools. 

%prep
%setup -qn %{name}_%{version}
%patch0 -p 1
%patch1 -p 1

%build
#poopolation is a collection of perl scrips and modules

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
cp -r Modules/* %{buildroot}%{_libdir}
cp -r basic-pipeline syn-nonsyn %{buildroot}%{_prefix}
cp -r *.pl %{buildroot}%{_bindir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%{_libdir}
%{_prefix}/syn-nonsyn/*.txt
%defattr(755,root,root,755)
%{_prefix}/basic-pipeline
%{_prefix}/syn-nonsyn/*.pl
%{_bindir}
