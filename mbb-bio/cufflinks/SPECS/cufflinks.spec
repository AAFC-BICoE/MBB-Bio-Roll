%define name		cufflinks
%define release		1
%define version 	2.2.1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		A program that assembles aligned RNA-Seq reads into transcripts, estimates their abundances, and tests for differential expression and regulation transcriptome-wide.
License: 		Boost Software License
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.tar.gz 
Prefix: 		%{installroot}
Group: 			Bioinformatics/Assembly
URL:			http://cufflinks.cbcb.umd.edu/index.html
AutoReq:		yes

BuildRequires:		samtools
Requires:		samtools
BuildRequires:		opt-eigen
Requires:		opt-eigen


%description
Cufflinks assembles transcripts, estimates their abundances, and tests for differential expression and regulation in RNA-Seq samples. It accepts aligned RNA-Seq reads and assembles the alignments into a parsimonious set of transcripts. Cufflinks then estimates the relative abundances of these transcripts based on how many reads support each one, taking into account biases in library preparation protocols. 


%prep
%setup -q 

%build
autoreconf --install

BAMLIB=$(rpm -ql samtools | grep include/bam/bam.h | head -n1 | sed 's#include/bam/bam.h##')
EIGENLIB=$(rpm -ql opt-eigen | grep include/Eigen/Core | head -n1 | sed 's#include/Eigen/Core##')
./configure --with-bam=$BAMLIB --with-eigen=$EIGENLIB --prefix=%{_prefix}
make -j`nproc` BOOST_LDFLAGS="-L/usr/lib -lboost_system -lboost_serialization -lboost_thread"


%install
mkdir -p %{buildroot}%{_prefix}
make install DESTDIR=%{buildroot}


%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc AUTHORS
%doc LICENSE
%doc README
%defattr(755,root,root,755)
%{_bindir}
