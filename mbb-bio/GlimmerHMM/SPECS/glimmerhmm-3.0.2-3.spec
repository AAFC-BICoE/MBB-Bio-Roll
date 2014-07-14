# This is a  spec file for GlimmerHH

### define _topdir	 	/home/rpmbuild/rpms/GlimmerHMM
%define name		GlimmerHMM
%define release		3
%define version 	3.0.2
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	GlimmerHMM is a new gene finder based on a Generalized Hidden Markov Model (GHMM).
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}-%{release}.patch0
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://cbcb.umd.edu/software/glimmerhmm/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        Open Source
AutoReq:	yes

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
%patch -P 0 -p1

%build
cd bin
mv glimmerhmm_linux glimmerhmm_linux_32bit
cd ..
cd train
make
cd ..
cd sources
make

%install
mkdir -p %{buildroot}%{installroot}
cp -r bin/ %{buildroot}%{installroot}
rm %{buildroot}%{installroot}/bin/glimmerhmm_linux_32bit
cp  sources/glimmerhmm %{buildroot}%{installroot}/bin/glimmerhmm_linux
cp -r train/ %{buildroot}%{installroot}
chmod -x %{buildroot}%{installroot}/train/trainGlimmerHMM
rm %{buildroot}%{installroot}/train/makefile 
rm %{buildroot}%{installroot}/train/readme.train
rm %{buildroot}%{installroot}/train/*.c
rm %{buildroot}%{installroot}/train/*.o
rm %{buildroot}%{installroot}/train/*.h

%files
%defattr(755,root,root)
%{installroot}
%defattr(644,root,root)
%{installroot}/train/cfgstat.pm
%{installroot}/train/dectree_allinfo.pm
%{installroot}/train/formtrain.pm
%{installroot}/train/orf.pm
%{installroot}/train/splitiso.pm

# make the file trainGlimmerHMM executable in the post section
%post
chmod +x %{installroot}/train/trainGlimmerHMM
