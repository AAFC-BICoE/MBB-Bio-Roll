%define name		opt-pkgconfig
%define release		1
%define version 	0.29.1
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/gnu-tools

BuildRoot:	%{buildroot}
Summary: 	A tool for determining compilation options
License:    	GPLv2+
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	pkg-config-%{version}.tar.gz
Prefix: 	/opt/bio
Group: 		Development/Tools
URL:		http://pkgconfig.freedesktop.org
AutoReqProv:	yes
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>
Provides:	pkgconfig(pkg-config) = %{version}

BuildRequires:	glib2-devel

%description
The pkgconfig tool determines compilation options. For each required
library, it reads the configuration file and outputs the necessary
compiler and linker flags.

%prep
%setup -q -n pkg-config-%{version}

%build
./configure --prefix=%{installroot} --with-install-glib --with-pc-path=%{installroot}/share/pkgconfig
make -j`nproc` PREFIX=%{installroot}

%install
make install DESTDIR=%{buildroot}

%files
%{installroot}/*
