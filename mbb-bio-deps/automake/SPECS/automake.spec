%define name		opt-automake
%define release		1
%define version 	1.15
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/gnu-tools

BuildRoot:	%{buildroot}
Summary: 	A GNU tool for automatically creating Makefiles
# docs ~> GFDL, sources ~> GPLv2+, mkinstalldirs ~> PD and install-sh ~> MIT
License:    	GPLv2+ and GFDL and Public Domain and MIT
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	automake-%{version}.tar.gz
Prefix: 	/opt/bio
Group: 		Development/Tools
URL:		http://www.gnu.org/software/automake
AutoReqProv:	yes
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>

Provides:	automake
Requires:	autoconf >= 2.65
# requirements not detected automatically (#919810)
Requires:	perl(Thread::Queue)
Requires:	perl(threads)

BuildRequires:  autoconf >= 2.65
BuildRequires:  automake


%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Automake::
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Automake::

# filter out bogus perl(Autom4te*) dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Autom4te::
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Autom4te::

%description
Automake is a tool for automatically generating `Makefile.in'
files compliant with the GNU Coding Standards.

You should install Automake if you are developing software and would
like to use its ability to automatically generate GNU standard
Makefiles.

%prep
%setup -q -n automake-%{version}
#autoreconf -iv

%build
./configure --prefix=%{installroot}
make -j`nproc` PREFIX=%{installroot}

%install
make install DESTDIR=%{buildroot}

%files
%exclude %{installroot}/share/info/dir
%exclude %{installroot}/share/aclocal
%{installroot}/*
