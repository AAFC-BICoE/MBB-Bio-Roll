%define name		mira
%define release		1
%define version 	4.0.2
%define installroot	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary:        MIRA - Sequence assembler and sequence mapping for whole genome shotgun and EST / RNASeq sequencing data. Can use Sanger, 454, Illumina and IonTorrent data. PacBio: CCS and error corrected data usable, uncorrected not yet.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.bz2
URL:            http://www.chevreux.org/projects_mira.html
Prefix: 	%{_prefix}	
Group: 		Bioinformatics/Assembly
License:        GPL
AutoReq:	yes

BuildRequires:	boost-devel

%description
MIRA is a whole genome shotgun and EST sequence assembler for Sanger, 454, Solexa (Illumina), IonTorrent data and PacBio (the later at the moment only CCS and error-corrected CLR reads). It can be seen as a Swiss army knife of sequence assembly developed and used in the past 16 years to get assembly jobs done efficiently - and especially accurately. That is, without actually putting too much manual work into finishing the assembly.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make -j`nproc`

%install
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc COPYING
%doc AUTHORS
%doc NEWS
%{_datadir}
%defattr(755,root,root,755)
%{_bindir}
