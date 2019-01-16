%define name		opt-udunits
%define src_name	udunits
%define release		1
%define version 	2.2.26
%define installroot	/opt/bio/lib/%{src_name}
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

BuildRoot:	%{buildroot}
Summary:	Unidata units manipulation library, udunits(3), and conversion program udunits(1), UDUNITS.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{src_name}-%{version}.tar.gz
URL:		https://www.unidata.ucar.edu/software/udunits/ 
Prefix:		%{_prefix}
Group: 		Development/Tools
License:        BSD
AutoReq:	yes

%description
The UDUNITS-2 package provides support for units of physical quantities. Its three main components are: 1) (udunits2lib)a C library for units of physical quantities; 2) (udunits2prog)a utility; for obtaining the definition of a unit and for converting numeric values between compatible units; and 3) an extensive database of units.

%prep
%setup -q -n %{src_name}-%{version}

%build
./configure --prefix=%{_prefix}
make -j `nproc`

%install
mkdir -p  %{buildroot}%{_libdir}
make install DESTDIR=%{buildroot} 

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc COPYRIGHT
%doc CHANGE_LOG
%doc README
%docdir %{_docdir}/%{src_name}
%{_docdir}/%{src_name}
%{_infodir}
%{_includedir}
%defattr(755,root,root,755)
%{_libdir}
%{_bindir}
%exclude %{_datadir}/%{src_name}
