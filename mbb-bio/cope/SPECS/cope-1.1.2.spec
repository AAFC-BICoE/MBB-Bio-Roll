


%define name			cope
%define src_name		cope
%define release		1
%define version 	1.1.2
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	COPE (Connecting Overlapped Pair-End reads)
License: 		GPL3
Name: 			%{name}
Version: 		%{version}
Packager:   Glen Newton <glen.newton@agr.gc.ca>
Release: 		%{release}
Source: 		cope-src-v1.1.2.tgz
Prefix: 		/opt/bio
Group: 			Applications/BioInformatics
URL:			http://sourceforge.net/projects/coperead/
AutoReq:		yes

%description
COPE (Connecting Overlapped Pair-End reads) is a method to align and connect the illumina sequenced Pair-End reads of which the insert size is smaller than the sum of the two read length.The connected reads can be used in genome assembly, resequencing and transcriptome research.
The full citation:
COPE: An accurate k-mer based pair-end reads connection tool to facilitate genome assembly
Binghang Liu; Jianying Yuan; Siu-Ming Yiu; Zhenyu Li; Yinlong Xie; Yanxiang Chen; Yujian Shi; Hao Zhang; Yingrui Li; Tak-Wah Lam; Ruibang Luo
Bioinformatics (2012) 28(22): 2870-2874; doi: 10.1093/bioinformatics/bts563

%prep
%setup -q -n src

%build
chmod +x src/cope/configure
cd src/cope; ./configure --prefix /opt/bio/cope; cd ../..
make prefix=%{installroot}

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/bin
cp src/cope/src/cope src/kmerfreq/kmerfreq $RPM_BUILD_ROOT%{installroot}/bin

%files
%defattr(755,root,root,755)
%{installroot}
