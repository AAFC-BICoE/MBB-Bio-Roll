%define name		opt-bison
%define src_name	bison
%define release		1
%define version 	3.1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/gnu-tools
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

BuildRoot:		%{buildroot}
Summary: 		Bison is a general-purpose parser generator that converts an annotated context-free grammar into a deterministic LR or generalized LR parser employing LALR parser tables.
License: 		GPLv3
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz 
Prefix: 		%{_prefix}
Group: 			Development/Tools
AutoReq:		yes
Packager:		Iyad Kandalaft <iyad.kandalaft@canada.ca>

%description

Bison is a general-purpose parser generator that converts an annotated
context-free grammar into a deterministic LR or generalized LR (GLR) parser
employing LALR(1) parser tables. As an experimental feature, Bison can also
generate IELR(1) or canonical LR(1) parser tables. Once you are proficient with
Bison, you can use it to develop a wide range of language parsers, from those
used in simple desk calculators to complex programming languages.

%prep 
%setup -q -n %{src_name}-%{version}

%build
./configure --prefix=%{_prefix}
make -pipe --jobs=`nproc` 

%install
mkdir -p %{buildroot}%{_prefix}
make install DESTDIR=%{buildroot}
strip %{buildroot}%{_prefix}/bin/bison

%files
%defattr(644,root,root,755)
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%{installroot}/lib/liby.a
%{_datadir}/bison/*
%{_datadir}/info/bison.info
%{_datadir}/aclocal/bison-i18n.m4
%{_datadir}/locale/*/LC_MESSAGES/*
%{_docdir}/*
%{_mandir}/man1/*
%defattr(755,root,root,755)
%{_libdir}/liby.a
%{_bindir}/bison
%{_bindir}/yacc

