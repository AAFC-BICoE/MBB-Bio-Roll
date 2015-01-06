

%define name			CEGMA
%define src_name		CEGMA
%define release		1
%define version 	2.5
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	CEGMA (Core Eukaryotic Genes Mapping Approach)
License: 		GPLv2
Name: 			%{name}
Version: 		%{version}
Packager:   Glen Newton <glen.newton@agr.gc.ca>
Release: 		%{release}
Source: 		CEGMA_v2.5.tar.gz
Patch0:			CEGMA_v2.5.patch0
Prefix: 		/opt/bio
Group: 			Applications/BioInformatics
URL:			http://genome.crg.es/software/geneid/
AutoReq:		yes

%description
CEGMA (Core Eukaryotic Genes Mapping Approach) is a pipeline for building a set
of high reliable set of gene annotations in virtually any eukaryotic genome. The
strategy relies on a simple fact: some highly conserved proteins are encoded in
essentially all eukaryotic genomes. We use the KOGs database to build a set of
these highly conserved ubiquitous proteins. We define a set of 458 core
proteins, and the protocol, CEGMA, to find orthologs of the core proteins in new
genomes and to determine their exon-intron structures.
Environment:
	export CEGMA=%{installroot}
	export CEGMATMP=%{installroot}
	export PERL5LIB=$PERL5LIB:$CEGMA/lib


%prep
%setup -qn CEGMA_v2.5
%patch -P 0 -p1  

%build
# Replaces the second line of Perl scripts which for some reason 
cd src; for f in `ls *.pl`; do sed -i 's/#!\/usr\/bin\/perl//' $f; done; cd ..
make prefix=%{installroot}

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r bin data lib GNU-GPL README.md release_notes.md sample $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root,755)
%{installroot}
