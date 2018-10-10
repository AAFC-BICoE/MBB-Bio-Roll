%define debug_package %{nil}

%define name		opt-bison
%define src_name	bison
%define release		1
%define version 	3.1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/gnu-tools

BuildRoot:		%{buildroot}
Summary: 		Bison is a general-purpose parser generator that converts an annotated context-free grammar into a deterministic LR or generalized LR parser employing LALR parser tables.
License: 		GPLv3
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz 
Prefix: 		%{installroot}
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
./configure --prefix=%{installroot}
make -pipe --jobs=`nproc` 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install prefix=$RPM_BUILD_ROOT%{installroot}
strip $RPM_BUILD_ROOT%{installroot}/bin/bison


%files
%defattr(644,root,root,755)
%{installroot}/lib/liby.a
%{installroot}/share/bison/*
%{installroot}/share/info/bison.info
%{installroot}/share/man/man1/*
%{installroot}/share/locale/*/LC_MESSAGES/*
%{installroot}/share/doc/*
%{installroot}/share/aclocal/bison-i18n.m4
%defattr(755,root,root,755)
%{installroot}/bin/bison
%{installroot}/bin/yacc

