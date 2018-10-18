%define name 		DeconSeq
%define src_name 		deconseq
%define version		0.4.3
%define release 	1
%define installroot	/opt/bio/%{name}
%define _prefix		%{installroot}

Summary: 	The DeconSeq tool can be used to automatically detect and efficiently remove sequence contaminations from genomic and metagenomic datasets.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{src_name}-standalone-%{version}.tar.gz
Patch0:		env-perl.patch
Group: 		Bioinformatics/Decontamination
License: 	GNU General Purpose License v3 
Vendor: 	Robert Schmieder
Packager: 	Alex MacLean <alex.maclean@agr.gc.ca>
Url: 		http://deconseq.sourceforge.net
AutoReq: 	yes

Requires:	opt-perl(Exporter)
Requires:	opt-perl(base)
Requires:	opt-perl(constant)
Requires:	opt-perl(strict)
Requires:	opt-perl(vars)

%global __requires_exclude ^perl

%description
DeconSeq is a publicly available tool that is able to automatically detect and efficiently remove sequence condaminations from genomic and metagenomic datasets. It is easily configurable and provides a user-friendly interface.

%prep
%setup -q -n %{src_name}-standalone-%{version}
%patch0 -p 1
%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r bwa64 DeconSeqConfig.pm deconseq.pl splitFasta.pl $RPM_BUILD_ROOT%{installroot}

%files 
%defattr(644,root,root,755)
%dir %{installroot}
%{installroot}/DeconSeqConfig.pm
%doc ChangeLog
%doc COPYING
%doc README
%defattr(755,root,root,755)
%{installroot}/bwa64
%{installroot}/deconseq.pl
%{installroot}/splitFasta.pl
