### define _topdir	 	/home/rpmbuild/rpms/snap

%define name 		snap
%define release 	1
%define version 	2013.11.29
%define installroot 	/opt/bio/%{name}
%define _prefix 	%{installroot}

BuildRoot: 	%{buildroot}
Summary: 	(Semi-HMM-based Nucleic Acid Parser) gene prediction tool
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
Patch0:		env-perl.patch
Packager: 	Newton,Glen <glen.newton@agr.gc.ca>
URL: 		http://korflab.ucdavis.edu/Software/snap-2013-02-16.tar.gz
Prefix: 	%{_prefix}
Group: 		Development/Tools
License: 	GPL|http://korflab.ucdavis.edu/Software/snap-2013-02-16.tar.gz|Specified in the contents of the package
AutoReq: 	yes

Requires:	opt-perl(Getopt::Std)
Requires:	opt-perl(sigtrap)
Requires:	opt-perl(strict)
Requires:	opt-perl(vars)
Requires:	opt-perl(warnings)

%global __requires_exclude ^perl 

%description
SNAP is a general purpose gene finding program suitable for both eukaryotic
and prokaryotic genomes. SNAP is an acroynm for Semi-HMM-based Nucleic Acid
Parser. 
Korf I. Gene finding in novel Genomes. BMC Bioinformatics 2004, 5:59
http://www.biomedcentral.com/1471-2105/5/59
From 00README
Needs Zoe in PATH


%prep 

%setup -c -q -n %{name}-%{version}/%{name}

%patch -P 0 

%build
cd %{name}
make -j`nproc`

%install
mkdir -p %{buildroot}%{installroot}
cp snap/LICENSE snap/exonpairs snap/fathom snap/forge snap/hmm-assembler.pl snap/hmm-info snap/patch-hmm.pl snap/snap snap/zff2gff3.pl %{buildroot}%{installroot}
cp -r snap/DNA/ snap/HMM/ %{buildroot}%{installroot}
mkdir -p %{buildroot}%{installroot}/Zoe
cp snap/Zoe/zoe-loop %{buildroot}%{installroot}/Zoe/
cp snap/Zoe/blosum62 %{buildroot}%{installroot}/Zoe/

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%{_prefix}
%defattr(755,root,root,755)
%{_prefix}/exonpairs
%{_prefix}/fathom
%{_prefix}/forge
%{_prefix}/hmm-assembler.pl
%{_prefix}/patch-hmm.pl
%{_prefix}/snap
%{_prefix}/hmm-info
%{_prefix}/zff2gff3.pl
%{_prefix}/Zoe/zoe-loop

%changelog
* Tue Apr  2 2013 glen newton <newtong@onottr624241.agr.gc.ca> - 16-1
- Initial build.

