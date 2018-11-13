### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/sga
%define name		sga
%define release		15         
%define version		0.10  
%define src_name	%{name}-%{version}.%{release}.tar.gz
%define installroot	/opt/bio/%{name}
%define _prefix		%{installroot}
%define buildroot	%{_topdir}/%{name}-%{version}-root

Summary:		SGA is a genome assembler
Name:			%{name}
Version:		%{version}
Release:		%{release}
Source:			%{src_name}
License:		GPLv3
Packager:		Wilson Hodgson <wilson.hodgson@canada.ca>
Group:			Development/Tools
BuildRoot:		%{buildroot}
Prefix:			%{_prefix}
Vendor:			Jared Simpson (js18@sanger.ac.uk)
Url:			https://github.com/jts/sga/
AutoReq:		no

BuildRequires:		opt-sparsehash
BuildRequires:		bamtools
BuildRequires:		jemalloc
BuildRequires:		zlib
BuildRequires:		opt-perl-BioPerl
Patch0:			Makefile.am.patch
Patch1:			env-perl.patch

%description
SGA - String Graph Assembler is a de novo genome assembler based on the concept
of string graphs. The major goal of SGA is to be very memory efficient, which
is achieved by using a compressed representation of DNA sequence reads.


%prep
%setup -q -n %{name}-%{version}.%{release}/src
%patch -P 0
%patch -P 1 -p2

%build
JEMAL_CONFIG=$(rpm -ql jemalloc | grep 'jemalloc/lib$' | head -n1)
SPHASH_CONFIG=$(rpm -ql opt-sparsehash | grep 'sparsehash$' | head -n1)
BAM_CONFIG=$(rpm -ql bamtools | grep 'bamtools$' | head -n1)

./autogen.sh
./configure --with-sparsehash=$SPHASH_CONFIG --with-bamtools=$BAM_CONFIG --with-jemalloc=$JEMAL_CONFIG --prefix=%{_prefix}
make -j`nproc`


%install
mkdir -p %{buildroot}%{installroot}
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_docdir}
cd ..
mv README.md index.html %{buildroot}%{_docdir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%docdir %{_docdir}
%{_docdir}
%defattr(755,root,root,755)
%{_bindir}

