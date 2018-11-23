%define name		bamtools
%define release		1
%define version 	2.4.1
%define installroot	/opt/bio/%{name}
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

BuildRoot:	%{buildroot}
Summary:	BamTools provides both a programmer's API and an end-user's toolkit for BAM files.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
URL:		https://github.com/pezmaster31/bamtools 
Prefix: 	%{_prefix}
Group: 		Bioinformatics/Alignment
License:        MIT
AutoReq:	yes

%description
BamTools is a project that provides both a C++ API and a command-line toolkit for reading, writing, and manipulating BAM (genome alignment) files.

%prep
%setup -q

%build
mkdir build 
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_RPATH=%{_libdir}/bamtools ..
make -pipe --jobs=`nproc`

%install
cd build
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc README
%doc LICENSE
%{_includedir}
%defattr(755,root,root,755)
%{_libdir}
%{_bindir}
