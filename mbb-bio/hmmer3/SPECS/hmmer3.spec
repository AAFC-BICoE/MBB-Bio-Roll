%define name		hmmer3
%define src_name	hmmer
%define release		1
%define version 	3.2.1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		Biosequence analysis using profile hidden Markov models. For searching sequence databases for homologs of protein sequences, and for making protein sequence alignments.
License: 		GNU GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-v%{version}.tar.gz
Prefix: 		%{installroot}
Group:			Bioinformatics/Homology
URL:			http://hmmer.org
AutoReq:		yes

%description
HMMER is used for searching sequence databases for homologs of protein sequences, and for making protein sequence alignments. It implements methods using probabilistic models called profile hidden Markov models (profile HMMs).

Compared to BLAST, FASTA, and other sequence alignment and database search tools based on older scoring methodology, HMMER aims to be significantly more accurate and more able to detect remote homologs because of the strength of its underlying mathematical models. In the past, this strength came at significant computational expense, but in the new HMMER3 project, HMMER is now essentially as fast as BLAST.

As part of this evolution in the HMMER software, we are committed to making the software available to as many scientists as possible. Earlier releases of HMMER were restricted to command line use. To make the software more accessible to the wide scientific community, we now provide servers that allow sequence searches to be performed interactively via the Web.

%prep
%setup -qn %{src_name}-%{version}

%build
./configure --prefix=%{installroot}
make -pipe --jobs=`nproc` 

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{installroot}
%{installroot}/share
%defattr(755,root,root,755)
%{installroot}/bin
