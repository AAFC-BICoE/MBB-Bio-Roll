### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/DeconSeq
%define name DeconSeq
%define version 0.4.3
%define release 1
%define installroot       /opt/bio/%{name}

summary: The DeconSeq tool can be used to automatically detect and efficiently remove sequence contaminations from genomic and metagenomic datasets.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: deconseq-standalone-0.4.3.tar.gz
Group: Development/Tools
License: GNU General Purpose License v3 
Vendor: Robert Schmieder
Packager: Alex MacLean <alex.maclean@agr.gc.ca>
Url: http://deconseq.sourceforge.net/
AutoReq: yes
AutoProv: yes

%description
DeconSeq is a publicly available tool that is able to automatically detect and efficiently remove sequence condaminations from genomic and metagenomic datasets. It is easily configurable and provides a user-friendly interface.

%prep
%setup -q -n deconseq-standalone-0.4.3

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r bwa64 bwaMAC DeconSeqConfig.pm deconseq.pl README splitFasta.pl $RPM_BUILD_ROOT%{installroot}

%files 
%defattr(755,root,root,755)
%{installroot}
