%define name		opt-make
%define release		1
%define version 	4.2.1
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/gnu-tools

BuildRoot:	%{buildroot}
Summary: 	The GNU macro processor
License:    	GPLv2+
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	make-%{version}.tar.gz
Prefix: 	/opt/bio
Group: 		Development/Tools
URL:		http://www.gnu.org/software/make
AutoReqProv:	yes
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>
BuildRequires:	procps
Provides:	make

# filter out bogus perl(Autom4te*) dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Autom4te::
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Autom4te::

%description
A GNU tool for controlling the generation of executables and other
non-source files of a program from the program's source files. Make
allows users to build and install packages without any significant
knowledge about the details of the build process. The details about
how the program should be built are provided for make in the program's
makefile.

%prep
%setup -q -n make-%{version}

%build
./configure --prefix=%{installroot}
make -j`nproc` PREFIX=%{installroot}

%install
make install DESTDIR=%{buildroot}

%files
%exclude %{installroot}/share/info/dir
%{installroot}/*

