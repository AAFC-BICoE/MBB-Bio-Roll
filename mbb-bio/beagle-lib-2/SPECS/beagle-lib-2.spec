# you need the following packages installed to build:
# libtool 
# automake 
# autoconf 
%define name		beagle-lib2
%define release		2
%define version 	2.1
%define buildroot 	%{_topdir}/%{name}-2-root
%define installroot 	/opt/bio/%{name}


BuildRoot:		%{buildroot}
Summary: 		Makes calc Bayesian and Maximum Likelihood phylogenetics packages.
License: 		LGPL 
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		beagle-lib-2.rev1261.tar.bz2
Prefix: 		/opt/bio
Group: 			Applications/BioInformatics/Phylogenetics
AutoReq:		yes
URL:			http://code.google.com/p/beagle-lib/

%description
BEAGLE is a high-performance library that can perform the core calculations at the heart of most Bayesian and Maximum Likelihood phylogenetics packages. It can make use of highly-parallel processors such as those in graphics cards (GPUs) found in many PCs. 
A manuscript describes the BEAGLE API and library: http://sysbio.oxfordjournals.org/content/61/1/170 


%prep
%setup -qn beagle-lib-2.rev1261

%build
./autogen.sh 
./configure  --prefix=%{installroot} --with-jdk=$JAVA_HOME
make -j

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install prefix=$RPM_BUILD_ROOT%{installroot}


%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root) 
%{installroot}/lib/*


