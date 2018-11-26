%define name		tophat
%define release		1
%define version 	2.1.1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		A spliced read mapper for RNA-Seq
License: 		BOOST Software License
Packager:		Wilson Hodgson <wilson.hodgson@canada.ca>
URL:			http://tophat.cbcb.umd.edu/
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz 
Prefix: 		%{_prefix}
Group: 			Bioinformatics/Mapping
AutoReq:		yes

BuildRequires:		boost
BuildRequires:		samtools

%description
TopHat is a fast splice junction mapper for RNA-Seq reads. It aligns RNA-Seq reads to mammalian-sized genomes using the ultra high-throughput short read aligner Bowtie, and then analyzes the mapping results to identify splice junctions between exons. 

%prep
%setup -q 

%build
export BAM_CONFIG=$(rpm -ql samtools | grep 'samtools$' | head -n1)

./configure --with-bam=$BAM_CONFIG --with-bam-libdir=$BAM_CONFIG/lib64 --prefix=%{_prefix}
make BOOST_LDFLAGS="-L/usr/lib -lboost_thread"

%install
mkdir -p %{buildroot}%{_prefix}

cp README LICENSE README NEWS AUTHORS %{buildroot}
make install DESTDIR=%{buildroot}

%files
%dir %{_prefix}
%doc LICENSE
%doc README
%doc NEWS
%doc AUTHORS
%defattr(755,root,root,755)
%{_bindir}
