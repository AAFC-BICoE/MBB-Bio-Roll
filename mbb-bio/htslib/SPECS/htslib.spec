%define name            htslib
%define release         1
%define version         1.9
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot	/opt/bio/lib/%{name}
%define _prefix		%{installroot}

BuildRoot:      	%{buildroot}
Summary:                A C library for reading/writing high-throughput sequencing data
License:                MIT
Name:                   %{name}
Version:                %{version}
Release:                %{release}
Source0:                %{name}-v%{version}.tar.gz
Prefix:                 %{installroot}
Group:                  Bioinformatics/Libraries
AutoReq:                yes
Url:                    http://samtools.sourceforge.net/
Packager:		Iyad Kandalaft <iyad.kandalaft@canada.ca>

%global __requires_exclude ^libhts

%description
HTSlib is an implementation of a unified C library for accessing common file formats, such as SAM, CRAM and VCF, used for high-throughput sequencing data, and is the core library used by samtools and bcftools. HTSlib only depends on zlib. It is known to be compatible with gcc, g++ and clang.

%prep
%setup -q

%build
autoreconf
./configure --prefix=%{installroot} --enable-libcurl
make -j`nproc`

%install
#mkdir -p $RPM_BUILD_ROOT%{installroot}/include/htslib
#mkdir -p $RPM_BUILD_ROOT%{installroot}/lib/pkgconfig
#cp htslib/*.h $RPM_BUILD_ROOT%{installroot}/include/htslib
#cp libhts.a $RPM_BUILD_ROOT%{installroot}/lib
#cp libhts.so $RPM_BUILD_ROOT%{installroot}/lib
#mv $RPM_BUILD_ROOT%{installroot}/lib/libhts.so $RPM_BUILD_ROOT%{installroot}/lib/libhts.so.%{version}
#ln -sf libhts.so.%{version} $RPM_BUILD_ROOT%{installroot}/lib/libhts.so
#ln -sf libhts.so.%{version} $RPM_BUILD_ROOT%{installroot}/lib/libhts.so.%{release}
#sed -e 's#@includedir@#/opt/bio/include#g;s#@libdir@#/opt/bio/lib#g;s#@PACKAGE_VERSION@#%{version}#g' htslib.pc.in > $RPM_BUILD_ROOT%{installroot}/lib/pkgconfig/htslib.pc
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc LICENSE
%{installroot}/include
%{installroot}/share
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/lib
