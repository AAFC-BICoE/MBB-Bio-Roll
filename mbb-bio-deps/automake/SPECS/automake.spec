%define name		opt-automake
%define release		1
%define version 	1.16.1
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
Prefix: 	%{installroot}
Group: 		Development/Tools
URL:		http://www.gnu.org/software/automake
AutoProv:	yes
AutoReq:	no
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>

Provides:	automake
Requires:	autoconf >= 2.65
# requirements not detected automatically (#919810)
Requires:	opt-perl
Requires:	opt-perl(Thread::Queue)
Requires:	opt-perl(threads)
Requires:	opt-perl(Carp)
Requires:	opt-perl(Class::Struct)
Requires:	opt-perl(Config)
Requires:	opt-perl(DynaLoader)
Requires:	opt-perl(Errno)
Requires:	opt-perl(Exporter)
Requires:	opt-perl(File::Basename)
Requires:	opt-perl(File::Compare)
Requires:	opt-perl(File::Copy)
Requires:	opt-perl(File::Path)
Requires:	opt-perl(File::Spec)
Requires:	opt-perl(File::stat)
Requires:	opt-perl(Getopt::Long)
Requires:	opt-perl(IO::File)
Requires:	opt-perl(POSIX)
Requires:	opt-perl(constant)
Requires:	opt-perl(strict)
Requires:	opt-perl(vars)
Requires:	opt-perl(warnings)

BuildRequires:  autoconf >= 2.65
BuildRequires:  automake
BuildRequires:  opt-perl(Thread::Queue)


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
./configure --prefix=%{installroot} PERL=/opt/perl/bin/perl
make PREFIX=%{installroot}

%install
export PERL5LIB=%{buildroot}
make install DESTDIR=%{buildroot}

%files
%{installroot}/share/aclocal*
%{installroot}/share/automake*
%{installroot}/share/doc/automake*
%{installroot}/share/info/automake*
%{installroot}/share/man/man1/*
%defattr(755,root,root,755)
%{installroot}/bin/*
