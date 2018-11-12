%define name		phylobayesmpi
%define src_name	pbmpi
%define release		1
%define version 	1.8_2f1ff98
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		A Bayesian software for phylogenetic reconstruction using mixture models, MPI
License: 		GPL3
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.zip
Packager:		Glen Newton <glen.newton@grc.gc.ca>
Prefix: 		%{_prefix}	
Url:                    http://megasun.bch.umontreal.ca/People/lartillot/www/downloadmpi.html
Group: 			Bioinformatics/Phylogenetics	
AutoReq:		yes

%description
PhyloBayes-MPI is a Bayesian Markov chain Monte Carlo (MCMC) sampler for phyloge-
netic inference exploiting a message-passing-interface system for multi-core computing. The
program will perform phylogenetic reconstruction using either nucleotide, protein, or codon
sequence alignments. Compared to other phylogenetic MCMC samplers, the main distin-
guishing feature of PhyloBayes is the use of non-parametric methods for modeling among-site
variation in nucleotide or amino-acid propensities.

%prep
%setup -q -n %{src_name}-master

%build
cd sources
make -j`nproc`

%install
mkdir -p %{buildroot}%{_bindir} 
cp -r data/* %{buildroot}%{_bindir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc LICENSE
%doc pb_mpiManual1.8.pdf
%defattr(755,root,root,755)
%{_bindir}
