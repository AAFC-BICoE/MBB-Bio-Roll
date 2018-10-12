### define _topdir	 	/home/rpmbuild/rpms/bowtie2
%define name		blat
%define	src_name	blatSrc
%define release		1
%define version 	3.5
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define debug_package	%{nil} 

BuildRoot:		%{buildroot}
Summary: 		A fast sequence alignment tool.
License: 		Artistic License
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.zip
Prefix: 		%{installroot}
Group: 			Bioinformatics/Aligner
URL:			https://github.com/BenLangmead/bowtie2
AutoReq:		yes
Packager:		Iyad Kandalaft <iyad.kandalaft@canada.ca>

%description
Blat is an alignment tool like BLAST, but it is structured differently. On DNA, Blat works by keeping an index of an entire genome in memory. Thus, the target database of BLAT is not a set of GenBank sequences, but instead an index derived from the assembly of the entire genome.

%prep
%setup -q -n %{name}Src

%build

%install
mkdir -p %{buildroot}%{installroot}/bin
MACHTYPE=x86_64 make -j`nproc` BINDIR=%{buildroot}%{installroot}/bin

%files
%defattr(755,root,root,755)
%{installroot}
