### define _topdir	 	/home/rpmbuild/rpms/bowtie2
%define name		bowtie2
%define release		1
%define version 	2.3.4.3
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define debug_package	%{nil} 

BuildRoot:		%{buildroot}
Summary: 		An ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences.
License: 		Artistic License
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.tar.gz
Patch0:			env-perl.patch
Prefix: 		%{installroot}
Group: 			Bioinformatics/Aligner
URL:			https://github.com/BenLangmead/bowtie2
AutoReq:		yes
Packager:	Glen Newton <Glen.Newton@agr.gc.ca>

BuildRequires:		tbb-devel

Requires:	opt-perl(Carp)
Requires:	opt-perl(Config)
Requires:	opt-perl(Data::Dumper)
Requires:	opt-perl(File::Spec)
Requires:	opt-perl(FindBin)
Requires:	opt-perl(Getopt::Long)
Requires:	opt-perl(List::Util)
Requires:	opt-perl(Math::Random)
Requires:	opt-perl(POSIX)
Requires:	opt-perl(Sys::Hostname)
Requires:	opt-perl(Sys::Info)
Requires:	opt-perl(Sys::Info::Constants)
Requires:	opt-perl(lib)
Requires:	opt-perl(strict)
Requires:	opt-perl(vars)
Requires:	opt-perl(warnings)

%global __requires_exclude ^perl

%description
Bowtie 2 is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences. It is particularly good at aligning reads of about 50 up to 100s or 1,000s of characters, and particularly good at aligning to relatively long (e.g. mammalian) genomes. Bowtie 2 indexes the genome with an FM Index to keep its memory footprint small: for the human genome, its memory footprint is typically around 3.2 GB. Bowtie 2 supports gapped, local, and paired-end alignment modes.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
make -j`nproc` prefix=%{installroot}

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install DESTDIR=%{buildroot} prefix=%{installroot}
cp -r doc %{buildroot}%{installroot}/
cp -r scripts %{buildroot}%{installroot}/
cp -r example %{buildroot}%{installroot}/

%files
%defattr(644,root,root,755)
%dir %{installroot}
%{installroot}/doc
%{installroot}/scripts
%{installroot}/example
%defattr(755,root,root,755)
%{installroot}/bin
