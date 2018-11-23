%define name		opt-argtable2
%define src_name	argtable2
%define release		1
%define version 	13
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/lib/%{src_name}
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

BuildRoot:	%{buildroot}
Summary: 	Argtable is an ANSI C command line parser.
License: 	LGPL
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{src_name}-%{version}.tar.gz
Prefix: 	%{installroot}
Group: 		Development/Libraries
URL:		http://argtable.sourceforge.net/
AutoReq:	yes

%description
Argtable is an ANSI C library for parsing GNU style command line
options with a minimum of fuss. It enables a programs command line
syntax to be defined in the source code as an array of argtable
structs. The command line is then parsed according to that
specification and the resulting values are returned in those same
structs where they are accessible to the main program. Both tagged
(-v, --verbose, --foo=bar) and untagged arguments are supported, as
are multiple instances of each argument. Syntax error handling is
automatic and the library also provides the means for generating a
textual description of the command line syntax. 


%prep
%setup -q -n %{src_name}-%{version}

%build
./configure --prefix=%{_prefix}
make prefix=%{_prefix}

%install
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%{_includedir}
%{_datadir}
%defattr(755,root,root,755)
%{_libdir}
