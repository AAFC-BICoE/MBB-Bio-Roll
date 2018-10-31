%define name		FungalITSextractor
%define release		1
%define version 	1.0 
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		FungalITSextractor 
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}.zip
Patch0:			env-perl.patch
Patch1:			hardcode-paths.patch
Prefix: 		%{installroot}
Group: 			Bioinformatics/Genetics
AutoReq:		yes
URL:			http://www.emerencia.org/FungalITSextractor.html

Requires: 		hmmer2
Requires:		opt-perl
Requires:		opt-perl(strict)
Requires:		opt-perl(warnings)
Requires:		opt-perl(Cwd)

%global __requires_exclude ^perl

%description
Extraction of ITS1/ITS2 from fungal ITS sequences in the FASTA format

%prep 
%setup -q -n %{name}
mv ../gpl.txt LICENSE

%build
#program is a perl script, nothing to do 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp  -r %{name}.pl HMMs $RPM_BUILD_ROOT%{installroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc LICENSE
%doc manual.pdf
%{_prefix}/HMMs
%attr(0755,root,root) %{_prefix}/FungalITSextractor.pl 
