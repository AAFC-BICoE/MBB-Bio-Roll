%define name		jemalloc
%define release		1
%define version		5.1.0
%define installroot	/opt/bio/lib/%{name}
%define _prefix		%{installroot}

Summary:		General purpose malloc(3) implementation that emphasizes fragmentation avoidance and scalable concurrency support. 
Name:			%{name}
Version:		%{version}
Release:		%{release}
Source:			%{name}-v%{version}.tar.gz
License:		BSD Derivative
Packager:		Iyad Kandalaft <iyad.kandalaft@canada.ca>
Group:			Development/Libraries
BuildRoot:		%{buildroot}
Prefix:			%{_prefix}
Vendor:			Jason Evans <jasone@canonware.com>
Url:			http://jemalloc.net/
AutoReq:		yes

%description
jemalloc is a general purpose malloc(3) implementation that emphasizes
fragmentation avoidance and scalable concurrency support.  jemalloc first came
into use as the FreeBSD libc allocator in 2005, and since then it has found its
way into numerous applications that rely on its predictable behavior.  In 2010
jemalloc development efforts broadened to include developer support features
such as heap profiling and extensive monitoring/tuning hooks.  Modern jemalloc
releases continue to be integrated back into FreeBSD, and therefore versatility
remains critical.  Ongoing development efforts trend toward making jemalloc
among the best allocators for a broad range of demanding applications, and
eliminating/mitigating weaknesses that have practical repercussions for real
world applications.


%prep
%setup -n %{name}-%{version}

%build
autoconf
./configure --prefix=%{_prefix} --enable-autogen
make -j`nproc`

%install
mkdir -p %{buildroot}%{_prefix}
make install_bin install_include install_lib DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc ChangeLog
%doc COPYING
%doc VERSION
%{_includedir}
%defattr(755,root,root,755)
%{_bindir}
%{_prefix}/lib
