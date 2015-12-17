### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/sga
%define name              sga
%define release		13         
%define version         0.10  
%define installroot       /opt/bio/%{name}

Summary:   SGA is a genome assembler
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    master.zip
License:   GPLv3
Packager:  Xie Qiu <xie.qiu@agr.gc.ca>
Group:     Development/Tools
#BuildRoot: %{buildroot}
Prefix:    /opt/bio
Vendor:    Jared Simpson (js18@sanger.ac.uk)
Url:       https://github.com/jts/sga/
AutoReq:   no
Requires:  sparsehash, bamtools, zlib, opt-perl-BioPerl
Patch0:    Makefile.am.patch
Patch1:    sga-asqg2dot.pl.patch
Patch2:    sga-bam2de.pl.patch
Patch3:    sga-beetl-index.pl.patch
Patch4:    sga-deinterleave.pl.patch
Patch5:    sga-diffCalls.pl.patch
Patch6:    sga-mergeDriver.pl.patch
Patch7:    sga-popcat.pl.patch
Patch8:    sga-rename.pl.patch
Patch9:	   sga-call-variants.pl.patch
Patch10:   sga-vcf-dedup.pl.patch

%description
SGA - String Graph Assembler is a de novo genome assembler based on the concept
of string graphs. The major goal of SGA is to be very memory efficient, which
is achieved by using a compressed representation of DNA sequence reads.


%prep
%setup -q -n sga-master/src
%patch -P 0
%patch -P 1
%patch -P 2
%patch -P 3
%patch -P 4
%patch -P 5
%patch -P 6
%patch -P 7
%patch -P 8
%patch -P 9
%patch -P 10

%build
./autogen.sh
./configure --with-sparsehash=/opt/bio/sparsehash --with-bamtools=/opt/bio/bamtools --with-jemalloc=/opt/bio/lib/jemalloc/lib/ --prefix=%{installroot}
make -j


%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install prefix=$RPM_BUILD_ROOT%{installroot} 

# %%clean
#echo NOOP

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin

