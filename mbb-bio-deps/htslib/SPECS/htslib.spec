%define name		opt-htslib
%define src_name	htslib
%define release		1
%define version		1.9
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot	/opt/bio/lib/%{name}
%define _prefix		%{installroot}
%define _libdir 	%{_prefix}/lib

BuildRoot:      	%{buildroot}
Summary:                A C library for reading/writing high-throughput sequencing data
License:                MIT
Name:                   %{name}
Version:                %{version}
Release:                %{release}
Source0:                %{src_name}-v%{version}.tar.gz
Prefix:                 %{installroot}
Group:                  Bioinformatics/Libraries
AutoReq:                yes
Url:                    http://samtools.sourceforge.net/
Packager:		Iyad Kandalaft <iyad.kandalaft@canada.ca>

%global __requires_exclude ^libhts

%description
HTSlib is an implementation of a unified C library for accessing common file formats, such as SAM, CRAM and VCF, used for high-throughput sequencing data, and is the core library used by samtools and bcftools. HTSlib only depends on zlib. It is known to be compatible with gcc, g++ and clang.

%prep
%setup -q -n %{src_name}-%{version}

%build
autoreconf
./configure --prefix=%{_prefix} --enable-libcurl
make -j`nproc`

%install
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc LICENSE
%{_includedir}
%{_datadir}
%defattr(755,root,root,755)
%{_bindir}
%{_libdir}
