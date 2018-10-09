%define debug_package %{nil}

%define name		bison
%define release		1
%define version 	2.6
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}


BuildRoot:		%{buildroot}
Summary: 		bison
License: 		GPL 
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz 
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description

Bison is a general-purpose parser generator that converts an annotated
context-free grammar into a deterministic LR or generalized LR (GLR) parser
employing LALR(1) parser tables. As an experimental feature, Bison can also
generate IELR(1) or canonical LR(1) parser tables. Once you are proficient with
Bison, you can use it to develop a wide range of language parsers, from those
used in simple desk calculators to complex programming languages.

%prep
%setup -q 

%build
./configure  --prefix=%{installroot}
make -pipe --jobs=`nproc` 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install prefix=$RPM_BUILD_ROOT%{installroot}
strip $RPM_BUILD_ROOT%{installroot}/bin/bison


%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
