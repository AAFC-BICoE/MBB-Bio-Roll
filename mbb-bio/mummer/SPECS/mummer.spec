%define name		mummer
%define release		1
%define version 	4.0.0beta2
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}
%define	_libdir		%{_prefix}/lib

BuildRoot:		%{buildroot}
Summary: 		Ultra-fast alignment of large-scale DNA and protein sequences
License: 		Artistic License
Name: 			%{name}
URL:			http://mummer.sourceforge.net
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.tar.gz
Packager:		Glen Newton <glen.newton@agrc.gc.ca>
Prefix: 		%{_prefix}
Group: 			Bioinformatics/Alignment
AutoReq:		yes

# removing TIFR requirement because it's included in the RPM
#Requires:		opt-perl(TIGR::Foundation)
#Provides:		opt-perl(TIGR::Foundation)
Requires:		opt-perl(File::Spec::Functions)
Requires:		opt-perl(IO::Socket)
Requires:		opt-perl(lib)
Requires:		opt-perl(strict)
Requires:		opt-perl(warnings)
Provides:		libumdmummer.so.0()(64bit)

%global __requires_exclude ^perl
%global __provides_exclude ^perl

%description
MUMmer is a system for rapidly aligning entire genomes, whether in complete or draft form. For example, MUMmer 3.0 can find all 20-basepair or longer exact matches between a pair of 5-megabase genomes in 13.7 seconds, using 78 MB of memory, on a 2.4 GHz Linux desktop computer. MUMmer can also align incomplete genomes; it can easily handle the 100s or 1000s of contigs from a shotgun sequencing project, and will align them to another set of contigs or a genome using the NUCmer program included with the system. If the species are too divergent for a DNA sequence alignment to detect similarity, then the PROmer program can generate alignments based upon the six-frame translations of both input sequences. The original MUMmer system, version 1.0, is described in our 1999 Nucleic Acids Research paper. Version 2.1 appeared a few years later and is described in our 2002 Nucleic Acids Research paper, while MUMmer 3.0 was recently described in our 2004 Genome Biology paper. We have also developed a GPU accelerated version of MUMmer called MUMmerGPU.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make -j`nproc`

%install
mkdir -p %{buildroot}%{_prefix}
#cp -R %{_topdir}/BUILD/%{name}-%{version}/scripts $RPM_BUILD_ROOT%{installroot}
#cp -R %{_topdir}/BUILD/%{name}-%{version}/docs $RPM_BUILD_ROOT%{installroot}
#cp -R %{_topdir}/BUILD/%{name}-%{version}/aux_bin $RPM_BUILD_ROOT%{installroot}
#cd %{_topdir}/BUILD/%{name}-%{version}; cp mummer annotate combineMUMs delta-filter gaps mgaps repeat-match show-aligns show-coords show-tiling show-snps show-diff exact-tandems mapview mummerplot nucmer promer run-mummer1 run-mummer3 nucmer2xfig dnadiff $RPM_BUILD_ROOT%{installroot}
make install DESTDIR=%{buildroot}


%files
%defattr(644,root,root,755)
%dir %{_prefix}

%defattr(755,root,root,755)
%{_libdir}
%{_libexecdir}
%{_bindir}
