# This is a  spec file for smalt

%global debug_package %{nil}

%define name		smalt
%define release		1
%define version 	0.7.3
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	SMALT efficiently aligns DNA sequencing reads with a reference genome.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tgz
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://www.sanger.ac.uk/resources/software/smalt/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GNU GPL
AutoReq:	yes

%description
SMALT is a pairwise sequence alignment program for the efficient mapping of DNA
sequencing reads onto genomic reference sequences. It uses a combination of
short-word hashing and dynamic programming.  Most types of sequencing platforms,
for example Illumina, Roche-454, Ion Torrent, PacBio or ABI-Sanger, are
supported including paired-end sequencing reads.


%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{installroot}
mkdir -p %{buildroot}/usr/man/man1

cp smalt_x86_64 %{buildroot}%{installroot}
cp smalt.1 %{buildroot}/usr/man/man1

%files
%defattr(755,root,root)
%doc
/usr/man/man1/smalt.1.gz
%{installroot}
