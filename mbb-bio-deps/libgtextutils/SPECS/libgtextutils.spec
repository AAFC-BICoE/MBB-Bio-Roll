%define name		opt-libgtextutils
%define src_name	libgtextutils
%define release		1
%define version 	0.7
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/lib/%{src_name}
%define	_prefix		%{installroot}
%define _libdir		%{_prefix}/lib

BuildRoot:		%{buildroot}
Summary: 		Gordon's Text utils Library
License: 		GPLv3
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source:         	%{src_name}-v%{version}.tar.gz
Prefix: 		%{_prefix}
Group:          	Libraries/Text Manipulation
AutoReq:		yes
Url:			https://github.com/agordon/libgtextutils
Packager:		Iyad Kandalaft <iyad.kandalaft@canada.ca>

%description
Gordon's Text utils Library used within fastx

%prep
%setup -qn %{src_name}-%{version}

%build
./reconf
./configure --prefix=%{installroot}
make -j `nproc`

%install
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc AUTHORS
%doc COPYING
%doc ChangeLog
%{_includedir}
%{_datadir}
%defattr(755,root,root,755)
%{_libdir}
