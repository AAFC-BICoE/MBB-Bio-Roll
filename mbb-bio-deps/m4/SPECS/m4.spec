%define name		opt-m4	
%define src_name	m4
%define release		1
%define version 	1.4.17
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/gnu-tools
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	The GNU macro processor
License:    	GPLv3+
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{src_name}-%{version}.tar.gz
Prefix: 	%{_prefix}
Group: 		Development/Tools
URL:		http://www.gnu.org/software/m4
AutoReqProv:	yes
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>
Provides:	bundled(gnulib)
Provides:	m4

# filter out bogus perl(Autom4te*) dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Autom4te::
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Autom4te::

%description
A GNU implementation of the traditional UNIX macro processor.  M4 is
useful for writing text files which can be logically parsed, and is used
by many programs as part of their build process.  M4 has built-in
functions for including files, running shell commands, doing arithmetic,
etc.  The autoconf program needs m4 for generating configure scripts, but
not for running configure scripts.

Install m4 if you need a macro processor.

%prep
%setup -q -n m4-%{version}

%build
./configure --prefix=%{_prefix}
make -j`nproc`

%install
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%{_infodir}/m4*
%{_mandir}/man1/m4*
%defattr(755,root,root,755)
%{_bindir}/m4
