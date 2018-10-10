### define _topdir	 	/home/rpmbuild/rpms/beagle-lib
%define name		opt-beagle-lib
%define	src_name	beagle-lib
%define release		1
%define version 	1.0
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/lib/%{src_name}


BuildRoot:		%{buildroot}
Summary: 		Makes calc Bayesian and Maximum Likelihood phylogenetics packages.
License: 		Lesser GPL 
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz 
Prefix: 		%{installroot}
Group: 			Development/Tools
AutoReq:		yes
URL:			http://code.google.com/p/beagle-lib/
Packager:		Iyad Kandalaft <iyad.kandalaft@canada.ca>

%description
BEAGLE is a high-performance library that can perform the core calculations at the heart of most Bayesian and Maximum Likelihood phylogenetics packages. It can make use of highly-parallel processors such as those in graphics cards (GPUs) found in many PCs. 

%prep
%setup -qn %{src_name}

%build
./autogen.sh 
./configure  --prefix=%{installroot}
make 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install prefix=$RPM_BUILD_ROOT%{installroot}


%files
%defattr(644,root,root,755)
%{installroot}
#%defattr(755,root,root) 
#%{installroot}/lib/libhmsbeagle.so.1.0.1 
#%{installroot}/lib/libhmsbeagle-jni.so 
#%{installroot}/lib/libhmsbeagle-cpu-sse.so.1.0.1 
#%{installroot}/lib/libhmsbeagle-cpu.so.1.0.1

