%define name		bwa
%define release		1
%define version 	0.7.17
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define	_prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		Burrows-Wheeler Alignment Tool
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.bz2
Prefix: 		%{installroot}
Group: 			Bioinformatics/Alignment
URL:			http://bio-bwa.sourceforge.net/bwa.shtml
AutoReq:		yes

%description

BWA is a software package for mapping DNA sequences against a large reference genome, such as the human genome. It consists of three algorithms: BWA-backtrack, BWA-SW and BWA-MEM. The first algorithm is designed for Illumina sequence reads up to 100bp, while the rest two for longer sequences ranged from 70bp to a few megabases. BWA-MEM and BWA-SW share similar features such as the support of long reads and chimeric alignment, but BWA-MEM, which is the latest, is generally recommended as it is faster and more accurate. BWA-MEM also has better performance than BWA-backtrack for 70-100bp Illumina reads.

%prep
%setup -q

%build
make -j `nproc`

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/bin
cp bwa *.pl $RPM_BUILD_ROOT%{installroot}/bin

%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc README.md
%doc COPYING
%doc NEWS.md
%defattr(755,root,root,755)
%{installroot}/bin
