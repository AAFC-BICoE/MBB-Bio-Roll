%define debug_package %{nil}

# you need the following packages installed to build:
# libtool 
# automake 
# autoconf 
### define _topdir	 	/home/rpmbuild/rpms/beagle-lib-2.1
%define name		beagle-lib-2.1
%define release		1
%define version 	2.1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}


BuildRoot:		%{buildroot}
Summary: 		Makes calc Bayesian and Maximum Likelihood phylogenetics packages.
License: 		Lesser GPL 
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		beagle-lib-2.1rev1222.tar.gz
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes
URL:			http://code.google.com/p/beagle-lib/

%description
BEAGLE is a high-performance library that can perform the core calculations at the heart of most Bayesian and Maximum Likelihood phylogenetics packages. It can make use of highly-parallel processors such as those in graphics cards (GPUs) found in many PCs. 

%prep
%setup -qn beagle-lib

%build
./autogen.sh 
./configure  --prefix=%{installroot} --with-jdk=$JAVA_HOME
make -pipe --jobs=`nproc` 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install prefix=$RPM_BUILD_ROOT%{installroot}


%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root) 
%{installroot}/lib/*


