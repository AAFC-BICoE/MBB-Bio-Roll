### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/jemalloc
%define name              jemalloc
%define release           3
%define version           4
%define installroot       /opt/bio/lib/%{name}

Summary:   general purpose memory allocation functions. 
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    jemalloc-4.0.3.tar.bz2
License:   BSD-derived license
Packager:  Xie Qiu <xie.qiu@agr.gc.ca>
Group:     Development/Libraries
#BuildRoot: %{buildroot}
Prefix:    /opt/bio/lib
Vendor:    Jason Evans <jasone@canonware.com>
Url:       http://www.canonware.com/jemalloc/
AutoReq:   yes

%description
jemalloc is a general purpose malloc implementation that emphasizes fragmentation avoidance and scalable concurrency support. jemalloc first came into use as the FreeBSD libc allocator in 2005, and since then it has found its way into numerous applications that rely on its predictable behavior. In 2010 jemalloc development efforts broadened to include developer support features such as heap profiling, Valgrind integration, and extensive monitoring/tuning hooks. Modern jemalloc releases continue to be integrated back into FreeBSD, and therefore versatility remains critical. Ongoing development efforts trend toward making jemalloc among the best allocators for a broad range of demanding applications, and eliminating/mitigating weaknesses that have practical repercussions for real world applications. 

%prep
%setup -n jemalloc-4.0.3

%build
./configure --prefix=%{installroot}
make -j


%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/lib
