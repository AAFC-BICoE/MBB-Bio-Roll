%define debug_package %{nil}


%define name			gcc491
%define src_name		gcc491
%define release		1
%define version 	4.9.1
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	GNU Compiler Collection
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source0: 		gcc-4.9.1.tar.bz2
Source1: 		gmp-6.0.0.tar.bz2
Source2: 		mpc-1.0.2.tar.bz2
Source3: 		mpfr-3.1.2.tar.bz2
Prefix: 		/opt/bio
Group: 			Development/Languages
URL:			https://gcc.gnu.org/
AutoReq:		yes
Packager:   Glen Newton <glen.newton@agr.gc.ca>

%description
The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Java, Ada, and Go, as well as libraries for these languages (libstdc++, libgcj,...). GCC was originally written as the compiler for the GNU operating system. The GNU system was developed to be 100% free software, free in the sense that it respects the user s freedom.

%prep
%setup -q  -a 0 -n gcc-4.9.1
%setup -q -T -D -a 1 -n gcc-4.9.1
mv gmp-6.0.0  gmp
%setup -q -T -D -a 2 -n gcc-4.9.1
mv mpc-1.0.2  mpc 
%setup -q -T -D -a 3 -n gcc-4.9.1
mv mpfr-3.1.2 mpfr



%build
mkdir gcc-build

# See https://gcc.gnu.org/wiki/FAQ#configure
unset LIBRARY_PATH CPATH C_INCLUDE_PATH PKG_CONFIG_PATH CPLUS_INCLUDE_PATH INCLUDE;cd gcc-build; export LD_LIBRARY_PATH=;%{_topdir}/BUILD/gcc-4.9.1/configure --disable-multilib --enable-static --prefix=/opt/bio/gcc; make prefix=%{installroot} -pipe --jobs=`nproc`

%install
unset LIBRARY_PATH CPATH C_INCLUDE_PATH PKG_CONFIG_PATH CPLUS_INCLUDE_PATH INCLUDE;cd gcc-build;export LD_LIBRARY_PATH=;make install prefix=$RPM_BUILD_ROOT%{installroot}
cd $RPM_BUILD_ROOT%{installroot}/bin; file * | grep "not stripped"|grep -Eo '^[^ ]+'|sed "s/://"|xargs strip


%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,) 
%{installroot}/bin/*


