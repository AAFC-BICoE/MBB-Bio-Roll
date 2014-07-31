%define debug_package %{nil}


%define name			gcc491
%define src_name		gcc
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
Source: 		%{src_name}-%{version}.tar.bz2
Prefix: 		/opt/bio
Group: 			Development/Libraries/GIS
URL:			sdaf
AutoReq:		yes
Packager:   Glen Newton <glen.newton@agr.gc.ca>

%description
The GNU Compiler Collection includes front ends for C, C++, Objective-C, Fortran, Java, Ada, and Go, as well as libraries for these languages (libstdc++, libgcj,...). GCC was originally written as the compiler for the GNU operating system. The GNU system was developed to be 100% free software, free in the sense that it respects the user s freedom.

%prep
%setup -q

%build
./configure --prefix=/opt/bio/gdal
make prefix=%{installroot}

%install
make install prefix=$RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root,755)
%{installroot}
