%define name		ITSx
%define release		1
%define version		1.1b
%define src_version	1.1
%define installroot	/opt/bio/%{name}
%define _prefix		%{installroot}

Summary:		Identifies ITS sequences and extracts the ITS region.
Name:			%{name}
Version:   		%{version}
Release:		%{release}
Source:			%{name}_%{version}.tar.gz
Patch0:			env-perl.patch
License:		GNU GENERAL PUBLIC LICENSE
Packager:		Iyad Kandalaft <iyad.kandalaft@canada.ca>
Group:			Bioinformatics/Genetics
BuildRoot:		%{buildroot}
Prefix:			%{_prefix}
Vendor:			Johan Bengtsson-Palme et al.
Url:			http://microbiology.se/software/itsx
AutoReq:		yes

Requires:		hmmer3
Requires:		opt-perl
Requires:		opt-perl(List::Util)

%global __requires_exclude ^perl

%description
ITSx is an open source software utility to extract the highly variable ITS1 and ITS2 subregions from ITS sequences, which is commonly used as a molecular barcode for e.g. fungi. As the inclusion of parts of the neighbouring, very conserved, ribosomal genes (SSU, 5S and LSU rRNA sequences) in the sequence identification process can lead to severely misleading results, ITSx identifies and extracts only the ITS regions themselves. The software is a complete re-write of the fungal ITS extractor, and among the new features included in ITSx are support for a wide range of additional phylums, and multicore support.

%prep
%setup -n %{name}_%{src_version}   
%patch0 -p 1

%build

%install
mkdir -p %{buildroot}%{_bindir}
mv ITSx ITSx_db %{buildroot}%{_bindir}/

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc README.txt
%doc ITSx User's Guide.pdf
%doc license.txt
%{_bindir}/ITSx_db
%attr(755,root,root) %{_bindir}/ITSx
