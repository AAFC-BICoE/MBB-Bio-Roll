%define name		hmmer2
%define release		1
%define version 	3.2
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary:		HMMER - Biosequence analysis using profile hidden Markov models
License: 		GPLv3
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		%{installroot}
Group: 			Bioinformatics/Homology
AutoReq:		yes

%description
HMMER is used for searching sequence databases for sequence homologs, and for making sequence alignments. It implements methods using probabilistic models called profile hidden Markov models (profile HMMs).

%prep
%setup -q

%build
./configure --prefix=%{installroot}
make -j `nproc`

%install
make install prefix=$RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root,755)
%dir %{installroot}
%{installroot}/man
%defattr(0755,root,root,0755)
%{installroot}/bin
