%define name		fastx
%define release		1
%define version 	0.0.14
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		The FASTX-Toolkit is a collection of command line tools for Short-Reads FASTA/FASTQ files preprocessing.
License: 		AGPLv3
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}_toolkit-%{version}.tar.bz2 
Patch0:			env-perl.patch
Prefix: 		%{installroot}
Group: 			Bioinforamtics/QAQC
AutoReq:		yes
URL:			http://hannonlab.cshl.edu/fastx_toolkit/

BuildRequires:		opt-libgtextutils >= 0.7

Requires:	opt-perl(Carp)
Requires:	opt-perl(Data::Dumper)
Requires:	opt-perl(GD::Graph::bars)
Requires:	opt-perl(Getopt::Long)
Requires:	opt-perl(IO::Handle)
Requires:	opt-perl(PerlIO::gzip)
Requires:	opt-perl(strict)
Requires:	opt-perl(warnings)

%global __requires_exclude ^perl

%description

The FASTX-Toolkit is a collection of command line tools for Short-Reads FASTA/FASTQ files preprocessing.  Next-Generation sequencing machines usually produce FASTA or FASTQ files, containing multiple short-reads sequences (possibly with quality information).  It is sometimes more productive to preprocess the FASTA/FASTQ files before mapping the sequences to the genome - manipulating the sequences to produce better mapping results.  The FASTX-Toolkit tools perform some of these preprocessing tasks.

%prep
%setup -qn %{name}_toolkit-%{version}
%patch0 -p1

%build
PKG_CONFIG_PATH=$(dirname $(rpm -ql opt-libgtextutils | grep gtextutils.pc | head -n1)) ./configure --prefix=%{installroot}
LD_RUN_PATH=$(dirname $(rpm -ql opt-libgtextutils | grep libgtextutils-0.7.so.0 | head -n 1)) make -j `nproc`

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install prefix=$RPM_BUILD_ROOT%{installroot}


%files
%defattr(755,root,root)
%{installroot}
