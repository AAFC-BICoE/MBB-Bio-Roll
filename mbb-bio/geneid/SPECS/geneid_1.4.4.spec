  %define debug_package %{nil}

%define name			geneid
%define src_name		geneid
%define release		1
%define version 	1.4.4
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	geneid is a program to predict genes in anonymous genomic sequences designed with a hierarchical structure.
License: 		GPLv2
Name: 			%{name}
Version: 		%{version}
Packager:   Glen Newton <glen.newton@agr.gc.ca>
Release: 		%{release}
Source: 		geneid_v1.4.4.Jan_13_2011.tar.gz
Prefix: 		/opt/bio
Group: 			Applications/BioInformatics
URL:			http://genome.crg.es/software/geneid/
AutoReq:		yes

%description
geneid is a program to predict genes in anonymous genomic sequences designed with a hierarchical structure. In the first step, splice sites, start and stop codons are predicted and scored along the sequence using Position Weight Arrays (PWAs). In the second step, exons are built from the sites. Exons are scored as the sum of the scores of the defining sites, plus the the log-likelihood ratio of a Markov Model for coding DNA. Finally, from the set of predicted exons, the gene structure is assembled, maximizing the sum of the scores of the assembled exons. geneid offers some type of support to integrate predictions from multiple source via external gff files and the redefinition of the general gene structure or model is also feasible. The accuracy of geneid compares favorably to that of other existing tools, but geneid is likely more efficient in terms of speed and memory usage. Currently, geneid v1.2 analyzes the whole human genome in 3 hours (approx. 1 Gbp / hour) on a processor Intel(R) Xeon CPU 2.80 Ghz. 

%prep
%setup -q -n geneid

%build
make prefix=%{installroot}

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r bin include param GNU_PL $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root,755)
%{installroot}
