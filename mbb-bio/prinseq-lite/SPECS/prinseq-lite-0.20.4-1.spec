### define _topdir	 	/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/prinseq-lite
%define name		prinseq-lite
%define release		1
%define version 	0.20.4
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	prinseq-lite is a preprocessing and information of sequence data.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
patch0:         prinseq-lite.pl.patch
patch1:         prinseq-graphs-noPCA.pl.patch
Packager:       Alex MacLean
URL:            http://prinseq.sourceforge.net/
Group: 		Development/Tools
License:        GPL v3
AutoReq:	yes
AutoProv:       yes

%description
prinseq-lite can be used to filter, reformat, or trim your genomic and
metagenomic sequence data. It generates summary statistics of your sequences in
graphical and tabular format. It is easily configurable and provides a
user-friendly interface. The standalone lite version is written in Perl and does
not require any non-core Perl modules. The lite version is primarily designed
for data preprocessing and does not generate summary statistics in graphical
form.

%prep
%setup -q
%patch -P 0
%patch -P 1

%build
mv prinseq-lite.pl prinseq-lite
mv prinseq-graphs-noPCA.pl prinseq-graphs
rm prinseq-graphs.pl
chmod 755 prinseq-lite
chmod 755 prinseq-graphs

%install
mkdir -p %{buildroot}%{installroot}
cp -r * %{buildroot}%{installroot}

%files
%defattr(755,root,root)
%{installroot}
