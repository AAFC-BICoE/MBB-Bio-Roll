### define _topdir	 	/home/rpmbuild/rpms/sgp2
%define name		sgp2
%define release		1
%define version 	v1.1.May_8_2012
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}
%define buildroot	%{_topdir}/%{name}-%{version}-root

BuildRoot:		%{buildroot}
Summary:		sgp2 is a program to predict genes by comparing anonymous genomic sequences from two different species.
Name: 			%{name}
Version:		%{version}
Release:		%{release}
Source:			%{name}_%{version}.tar.gz
Patch0:			%{name}_%{version}.patch0
Packager:		Zaky Adam <zaky.adam@grc.gc.ca>
URL:			http://genome.crg.es/software/sgp2/index.html
Prefix:			%{_prefix}
Group:			Development/Tools
License:		GPL-2|ftp://genome.crg.es/pub/software/sgp2/sgp2_v1.1.May_8_2012.tar.gz|Specified in the contents of the package
AutoReq:		yes

Requires:		opt-perl(Benchmark)
Requires:		opt-perl(Getopt::Long)
Requires:		opt-perl(strict)
Requires:		opt-perl(warnings)

%global __requires_exclude ^perl

%description
sgp2 is a program to predict genes by comparing anonymous genomic sequences from
two different species. It combines tblastx, a sequence similarity search
program, with geneid, an "ab initio" gene prediction program. In "assymetric"
mode, genes are predicted in one sequence from one species (the target
sequence), using a set of sequences (maybe only one) from the other species (the
reference set). Essentially, geneid is used to predict all potential exons along
the target sequence. Scores of exons are computed as log-likelihood ratios,
function of the splice sites defining the exon, the coding bias in composition
of the exon sequence as measured by a Markov Model of order five, and of the
optimal alignment at the amino acid level between the target exon sequence and
the counterpart homologous sequence in the reference set. From the set of
predicted exons, the gene structure is assembled (eventually multiple genes in
both strands) maximizing the sum of the scores of the assembled exons. 

%prep
%setup -q -n %{name}
%patch -P 0 -p1

%build
make -j`nproc`
patch -p1 < /home/rpmbuild/rpms/sgp2/SOURCES/sgp2_v1.1.May_8_2012.patch1
patch -p1 < /home/rpmbuild/rpms/sgp2/SOURCES/sgp2_v1.1.May_8_2012.patch2

%install
mkdir -p %{buildroot}%{_docdir}
mkdir -p %{buildroot}%{_bindir}

cp README %{buildroot}%{_docdir}

make install INSTALLDIR=%{buildroot}/%{_bindir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%docdir %{_docdir}
%{_docdir}
%defattr(755,root,root,755)
%{_bindir}

