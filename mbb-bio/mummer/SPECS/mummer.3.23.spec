# This is a sample spec file for wget

%define name			MUMmer
%define release		cl3
%define version 	3.23
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 		Ultra-fast alignment of large-scale DNA and protein sequences
License: 		Artistic License
Name: 			%{name}
URL:			http://mummer.sourceforge.net
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Packager:	Glen Newton <glen.newton@agrc.gc.ca>
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		no
Requires: 		libc.so.6()(64bit), libc.so.6(GLIBC_2.2.5)(64bit), libc.so.6(GLIBC_2.3)(64bit), libgcc_s.so.1()(64bit), libgcc_s.so.1(GCC_3.0)(64bit), libm.so.6()(64bit), libm.so.6(GLIBC_2.2.5)(64bit), libstdc++.so.6()(64bit), libstdc++.so.6(CXXABI_1.3)(64bit), libstdc++.so.6(GLIBCXX_3.4)(64bit), perl(Cwd), perl(English), perl(File::Basename), perl(File::Spec::Functions), perl(Getopt::Long), perl(IO::Handle), perl(IO::Socket), perl(POSIX), perl(Sys::Hostname), perl(lib), perl(strict), rpmlib(CompressedFileNames) <= 3.0.4-1, rpmlib(PayloadFilesHavePrefix) <= 4.0-1, rpmlib(VersionedDependencies) <= 3.0.3-1, rtld(GNU_HASH)

%description
MUMmer is a system for rapidly aligning entire genomes, whether in complete or draft form. For example, MUMmer 3.0 can find all 20-basepair or longer exact matches between a pair of 5-megabase genomes in 13.7 seconds, using 78 MB of memory, on a 2.4 GHz Linux desktop computer. MUMmer can also align incomplete genomes; it can easily handle the 100s or 1000s of contigs from a shotgun sequencing project, and will align them to another set of contigs or a genome using the NUCmer program included with the system. If the species are too divergent for a DNA sequence alignment to detect similarity, then the PROmer program can generate alignments based upon the six-frame translations of both input sequences. The original MUMmer system, version 1.0, is described in our 1999 Nucleic Acids Research paper. Version 2.1 appeared a few years later and is described in our 2002 Nucleic Acids Research paper, while MUMmer 3.0 was recently described in our 2004 Genome Biology paper. We have also developed a GPU accelerated version of MUMmer called MUMmerGPU.

%prep
%setup -q

%build
mkdir -p $RPM_BUILD_ROOT%{installroot}/bin
mkdir -p $RPM_BUILD_ROOT%{installroot}/aux_bin
mkdir -p $RPM_BUILD_ROOT%{installroot}/scripts
make CUR_DIR=$RPM_BUILD_ROOT%{installroot}

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -R %{_topdir}/BUILD/%{name}-%{version}/scripts $RPM_BUILD_ROOT%{installroot}
cp -R %{_topdir}/BUILD/%{name}-%{version}/docs $RPM_BUILD_ROOT%{installroot}
cp -R %{_topdir}/BUILD/%{name}-%{version}/aux_bin $RPM_BUILD_ROOT%{installroot}
cd %{_topdir}/BUILD/%{name}-%{version}; cp mummer annotate combineMUMs delta-filter gaps mgaps repeat-match show-aligns show-coords show-tiling show-snps show-diff exact-tandems mapview mummerplot nucmer promer run-mummer1 run-mummer3 nucmer2xfig dnadiff $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
