%define name		opt-beagle-lib2
%define src_name	beagle-lib
%define release		1
%define version 	2.1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/lib/%{src_name}2
%define _prefix		%{installroot}
%define	_libdir		%{installroot}/lib

BuildRoot:		%{buildroot}
Summary: 		Makes calc Bayesian and Maximum Likelihood phylogenetics packages.
License: 		Lesser GPL 
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-v%{version}.tar.gz
Prefix: 		%{_prefix}
Group: 			Development/Tools
AutoReq:		yes
URL:			http://code.google.com/p/beagle-lib/
Packager:		Iyad Kandalaft <iyad.kandalaft@canada.ca>

BuildRequires:		java-sdk >= 1:1.8.0
Requires:		java >= 1:1.8.0

%description
BEAGLE is a high-performance library that can perform the core calculations at the heart of most Bayesian and Maximum Likelihood phylogenetics packages. It can make use of highly-parallel processors such as those in graphics cards (GPUs) found in many PCs. 

%prep
%setup -qn beagle-lib

%build
./autogen.sh 
./configure --prefix=%{_prefix} --enable-static --enable-openmp
make -pipe --jobs=`nproc` 

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
