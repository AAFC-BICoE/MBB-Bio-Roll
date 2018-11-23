%define name		opt-beagle-lib
%define	src_name	beagle-lib
%define release		1
%define version 	1.1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/lib/%{src_name}
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

BuildRoot:		%{buildroot}
Summary: 		Makes calc Bayesian and Maximum Likelihood phylogenetics packages.
License: 		LGPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz 
Patch0:			cpu-makefile-sseconditional.patch
Prefix: 		%{_prefix}
Group: 			Development/Tools
AutoReq:		yes
URL:			http://code.google.com/p/beagle-lib/
Packager:		Iyad Kandalaft <iyad.kandalaft@canada.ca>

%description
BEAGLE is a high-performance library that can perform the core calculations at the heart of most Bayesian and Maximum Likelihood phylogenetics packages. It can make use of highly-parallel processors such as those in graphics cards (GPUs) found in many PCs. 

%prep
%setup -qn %{src_name}-beagle_release_1_1
%patch0 -p 1

%build
./autogen.sh 
CXXFLAGS=-fpermissive ./configure --enable-openmp --enable-sse --enable-static --prefix=%{_prefix}
# parallel builds are not supported. Do no use -j`nproc`
make 

%install
mkdir -p %{buildroot}%{_prefix}
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%doc COPYING.LESSER
%{_includedir}
%defattr(755,root,root,755)
%{_libdir}

