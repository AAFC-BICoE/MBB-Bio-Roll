# This is a  spec file for velvet
%define debug_package %{nil}

%define name		allpathslg
%define release		1
%define version 	50960
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	Short read whole‐genome shotgun assembler
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Packager:	Glen Newton glen.newton@agr.gc.ca
Source: 	allpathslg-50960.tar.bz2
URL:            ftp://ftp.broadinstitute.org/pub/crd/ALLPATHS/Release-LG/
Prefix: 	/opt/bio
Group: 		Applications/BioInformatics/Assembler
License:        MIT
AutoReq:	yes

%description
"ALLPATHS‐LG is a whole‐genome shotgun assembler that can generate high‐quality genome assemblies using short reads (~100bp) such as those produced by the new generation of sequencers. The significant difference between ALLPATHS and traditional assemblers such as Arachne is that ALLPATHS assemblies are not necessarily linear, but instead are presented in the form of a graph. This graph representation retains ambiguities, such as those arising from polymorphism, uncorrected read errors, and unresolved repeats, thereby providing information that has been absent from previous genome assemblies."
Citation: Gnerre S, MacCallum I, Przybylski D, Ribeiro F, Burton J, Walker B, Sharpe T, Hall G, Shea T, Sykes S, Berlin A, Aird D, Costello M, Daza R, Williams L, Nicol R, Gnirke A, Nusbaum C, Lander ES, Jaffe DB. 2010. High-quality draft assemblies of mammalian genomes from massively parallel sequence data. Proceedings of the National Academy of Sciences USA (epub ahead of print, Dec. 27, 2010).
NB: In order to run on AAFC cluster, must set 'export LD_LIBRARY_PATH=/opt/bio/gcc491/lib64:$LD_LIBRARY_PATH'

%prep
%setup -q 


%build
export PATH=/opt/bio/gcc491/bin:$PATH
./configure  --prefix=%{installroot}
make --jobs=`nproc`


%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install prefix=$RPM_BUILD_ROOT%{installroot}
cd $RPM_BUILD_ROOT%{installroot}/bin; file * | grep "not stripped"|grep -Eo '^[^ ]+'|sed "s/://"|xargs strip


%files
%defattr(755,root,root,755)
%{installroot}
%defattr(644,root,root,755)


