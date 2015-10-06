### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/ITSx
%define name              ITSx
%define release           11
%define version           1
%define installroot       /opt/bio/%{name}

Summary:   Identifies ITS sequences and extracts the ITS region.
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    ITSx_1.0.11.tar.gz
License:   GNU GENERAL PUBLIC LICENSE
Packager:  Xie Qiu <xie.qiu@agr.gc.ca>
Group:     Development/Tools
#BuildRoot: %{buildroot}
Prefix:    /opt/bio
Vendor:    Johan Bengtsson-Palme et al.
Url:       http://microbiology.se/software/itsx
AutoReq:   yes
patch0: ITSx.patch

%description
ITSx is an open source software utility to extract the highly variable ITS1 and ITS2 subregions from ITS sequences, which is commonly used as a molecular barcode for e.g. fungi. As the inclusion of parts of the neighbouring, very conserved, ribosomal genes (SSU, 5S and LSU rRNA sequences) in the sequence identification process can lead to severely misleading results, ITSx identifies and extracts only the ITS regions themselves. The software is a complete re-write of the fungal ITS extractor, and among the new features included in ITSx are support for a wide range of additional phylums, and multicore support.

%prep
%setup -n ITSx_1.0.11   
%patch -P 0

%build
mkdir bin
mv ITSx bin
mv ITSx_db bin

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r * $RPM_BUILD_ROOT%{installroot}/

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin

