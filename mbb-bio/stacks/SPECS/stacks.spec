### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/stacks
%define name              stacks
%define release           1 
%define version           1.35
%define installroot       /opt/bio/%{name}

Summary:   Stacks is a software pipeline for building loci from short-read sequences, such as those generated on the Illumina platform. 
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    stacks-1.35.tar.gz
License:   GNU GPL license
Packager:  Xie Qiu <xie.qiu@agr.gc.ca>
Group:     Development/Libraries
#BuildRoot: %{buildroot}
Prefix:    /opt/bio
Vendor:    Julian Catchen <jcatchen@illinois.edu>, Angel Amores <amores@uoregon.edu >, Paul Hohenlohe <hohenlohe@uidaho.edu >, Bill Cresko <wcresko@uoregon.edu >
Url:       http://catchenlab.life.illinois.edu/stacks/
AutoReq:   yes
Patch0:	   load_sequences.pl.patch

%description
Stacks is a software pipeline for building loci from short-read sequences, such as those generated on the Illumina platform. Stacks was developed to work with restriction enzyme-based data, such as RAD-seq, for the purpose of building genetic maps and conducting population genomics and phylogeography. 
%prep
%setup -q -n stacks-1.35
%patch -P 0

%build
./configure --prefix=%{installroot} --enable-bam --with-bam-include-path=/opt/bio/samtools/include/bam --with-bam-lib-path=/opt/bio/samtools/lib --enable-sparsehash --with-sparsehash-include-path=/opt/bio/sparsehash/include

make -j

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install DESTDIR=$RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/share
