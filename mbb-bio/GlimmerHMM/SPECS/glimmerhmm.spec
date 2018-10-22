%define name		GlimmerHMM
%define release		1
%define version 	3.0.4
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	GlimmerHMM is a new gene finder based on a Generalized Hidden Markov Model (GHMM).
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>
URL:            http://cbcb.umd.edu/software/glimmerhmm/
Prefix: 	%{installroot}
Group: 		Bioinformatics/Gene Finding
License:        Open Source
AutoReq:	yes

%global __requires_exclude ^perl

%description
GlimmerHMM is a new gene finder based on a Generalized Hidden Markov Model
(GHMM). Although the gene finder conforms to the overall mathematical framework
of a GHMM, additionally it incorporates splice site models adapted from the
GeneSplicer program and a decision tree adapted from GlimmerM. It also utilizes
Interpolated Markov Models for the coding and noncoding models . Currently,
GlimmerHMM's GHMM structure includes introns of each phase, intergenic regions,
and four types of exons (initial, internal, final, and single).

%prep
%setup -q -n GlimmerHMM

%build
rm bin/*
pushd train
make -j `nproc`
popd
pushd sources
make -j `nproc`
popd 

%install
mkdir -p %{buildroot}%{installroot}/bin
cp -r bin/ %{buildroot}%{installroot}/bin
cp  sources/glimmerhmm %{buildroot}%{installroot}/bin/
cp -r train/ %{buildroot}%{installroot}
rm %{buildroot}%{installroot}/train/makefile 
rm %{buildroot}%{installroot}/train/readme.train
rm %{buildroot}%{installroot}/train/*.c
rm %{buildroot}%{installroot}/train/*.o
rm %{buildroot}%{installroot}/train/*.h

%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc LICENSE
%{installroot}/train/*.pm
%defattr(755,root,root)
%{installroot}/bin
%{installroot}/train/build-icm
%{installroot}/train/build-icm-noframe
%{installroot}/train/build1
%{installroot}/train/build2
%{installroot}/train/erfapp
%{installroot}/train/falsecomp
%{installroot}/train/findsites
%{installroot}/train/karlin
%{installroot}/train/score
%{installroot}/train/score2
%{installroot}/train/scoreATG
%{installroot}/train/scoreATG2
%{installroot}/train/scoreSTOP
%{installroot}/train/scoreSTOP2
%{installroot}/train/splicescore
%{installroot}/train/trainGlimmerHMM

