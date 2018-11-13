%define __brp_python_hardlink %{nil}

##define _topdir	 	/home/rpmbuild/rpms/saps
%define name		saps
%define src_name	saps.sspa
%define release		2	
%define version 	1996
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Prefix:		%{_prefix}
Summary: 	SAPS is a Statistical Analysis of Protein Sequences.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{src_name}.tar.gz
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
Prefix: 	%{_prefix}
Group: 		Development/Tools
License:	GNU GPL
URL:		http://brendelgroup.org/bioinformatics2go/
AutoReq:	yes

%description
SAPS (Statistical Analysis of Protein Sequences) evaluates by statistical
criteria a wide variety of protein sequence properties. A full description of
the methods is given in the paper: Methods and  algorithms for statistical
analysis of protein sequences (1992). The output is organized in the following
sections: file name, sequence printout, compositional analysis, charge
distributional analysis (charge  clusters;  high scoring  (un)charged segments;
charge runs and patterns), distribution of other amino acid types (high scoring
hydrophobic and transmembrane segments; cysteine spacings), repetitive
structures (in the amino acid alphabet and in a 11-letter reduced alphabet),
multiplets (counts, spacings, and clusters in the amino acid and charge
alphabets), periodicity analysis, spacing analysis. Each section is annotated
below under its section title.

%prep
%setup -q -n SAPS.SSPA

%build
cd src
make -j`nproc`

%install
mkdir -p %{buildroot}%{_docdir}/man/man1
mv saps.1 sspa.1 %{buildroot}%{_docdir}/man/man1
mv README sspa.doc saps.doc %{buildroot}%{_docdir}

cp -r * %{buildroot}%{installroot}
rm -r %{buildroot}%{installroot}/src
rm -r %{buildroot}%{installroot}/include

%files
%defattr(755,root,root,755)
%dir %{_prefix}
%{_bindir}
%defattr(644,root,root,755)
%docdir %{_docdir}/man/man1
%{_docdir}/man/man1
%doc %{_docdir}/README
%doc %{_docdir}/sspa.doc
%doc %{_docdir}/saps.doc

