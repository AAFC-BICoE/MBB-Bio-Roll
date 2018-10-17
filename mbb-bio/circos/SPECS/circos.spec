%define name		circos
%define release		1
%define version 	0.69
%define	patch		6
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	Circo is a flexible and automatable circular data visualization.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}-%{patch}.tgz
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>
URL:            http://circos.ca/software/download/circos
Prefix: 	%{installroot}
Group: 		Development/Tools
License:        GPL-2|https://code.google.com/p/circos	
AutoReq:	yes
AutoProv:	no

Requires:	opt-perl(Carp)
Requires:	opt-perl(Config::General)
Requires:	opt-perl(Cwd)
Requires:	opt-perl(Data::Dumper)
Requires:	opt-perl(File::Basename)
Requires:	opt-perl(FindBin)
Requires:	opt-perl(GD)
Requires:	opt-perl(Getopt::Long)
Requires:	opt-perl(IO::File)
Requires:	opt-perl(Math::Round)
Requires:	opt-perl(Math::VecStat)
Requires:	opt-perl(POSIX)
Requires:	opt-perl(Pod::Usage)
Requires:	opt-perl(Set::IntSpan) >= 1.11
Requires:	opt-perl(Storable)
Requires:	opt-perl(Time::HiRes)
Requires:	opt-perl(constant)
Requires:	opt-perl(lib)
Requires:	opt-perl(strict)
Requires:	opt-perl(warnings)

%global __requires_exclude ^perl

%description
Circos is a program for the generation of publication-quality, circularly
composited renditions of genomic data and related annotations.  Circos is
particularly suited for visualizing alignments, conservation and intra and
inter-chromosomal relationships.  Also, Circos is useful to visualize any type
of information that benefits from a circular layout. Thus, although it has been
designed for the field of genomics, it is sufficiently flexible to be used in
other data domains.

%prep
%setup -q -n %{name}-%{version}-%{patch}

%build

%install
mkdir -p %{buildroot}%{installroot}
cp -r bin/ data/ etc/ fonts/ lib/ tiles/ gddiag.png %{buildroot}%{installroot}

%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc CHANGES
%doc CITATION
%doc README
%doc SUPPORT
%{installroot}/data/
%{installroot}/etc/
%{installroot}/fonts/
%{installroot}/lib/
%{installroot}/tiles/
%{installroot}/gddiag.png
%defattr(755,root,root,755)
%{installroot}/bin/circos
%{installroot}/bin/gddiag

