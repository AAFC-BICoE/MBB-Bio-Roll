%define name		opt-autoconf
%define src_name	autoconf
%define release		1
%define version 	2.69
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/gnu-tools

BuildRoot:	%{buildroot}
Summary: 	A GNU tool for automatically configuring source code
License:    	GPLv2+ and GFDL
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	autoconf-%{version}.tar.gz
Prefix: 	%{installroot}
Group: 		Development/Tools
URL:		http://www.gnu.org/software/autoconf/autoconf.html	
AutoReq:	no
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>

# m4 >= 1.4.6 is required, >= 1.4.14 is recommended.
# Downgraded to 1.4.13 beacuse it ships with CentOS 6
BuildRequires:      m4 >= 1.4.13
Requires:           m4 >= 1.4.13
# the filtering macros are currently in /etc/rpm/macros.perl:
BuildRequires:      perl(Data::Dumper)
# from f19, Text::ParseWords is not the part of 'perl' package
BuildRequires:      opt-perl(Text::ParseWords)

Provides:	%{src_name} = %{version}
Requires:	opt-perl >= 0:5.006
Requires:	opt-perl(Carp)
Requires:	opt-perl(Class::Struct)
Requires:	opt-perl(Cwd)
Requires:	opt-perl(Data::Dumper)
Requires:	opt-perl(DynaLoader)
Requires:	opt-perl(Errno)
Requires:	opt-perl(Exporter)
Requires:	opt-perl(File::Basename)
Requires:	opt-perl(File::Compare)
Requires:	opt-perl(File::Copy)
Requires:	opt-perl(File::Find)
Requires:	opt-perl(File::Path)
Requires:	opt-perl(File::Spec)
Requires:	opt-perl(File::stat)
Requires:	opt-perl(Getopt::Long)
Requires:	opt-perl(IO::File)
Requires:	opt-perl(POSIX)
Requires:	opt-perl(Text::ParseWords)
Requires:	opt-perl(constant)
Requires:	opt-perl(strict)
Requires:	opt-perl(vars)
Requires:	opt-perl(warnings)
Requires:	rpmlib(CompressedFileNames) <= 3.0.4-1
Requires:	rpmlib(FileDigests) <= 4.6.0-1
Requires:	rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires:	rpmlib(PayloadIsXz) <= 5.2-1



# filter out bogus perl(Autom4te*) dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Autom4te::
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Autom4te::

%description
GNU's Autoconf is a tool for configuring source code and Makefiles.
Using Autoconf, programmers can create portable and configurable
packages, since the person building the package is allowed to
specify various configuration options.

You should install Autoconf if you are developing software and
would like to create shell scripts that configure your source code
packages. If you are installing Autoconf, you will also need to
install the GNU m4 package.

Note that the Autoconf package is not required for the end-user who
may be configuring software with an Autoconf-generated script;
Autoconf is only required for the generation of the scripts, not
their use.

%prep
%setup -q -n autoconf-%{version} PERL=/opt/perl/bin/perl

%build
./configure --prefix=%{installroot}
# Not parallel safe - do not use -j`nproc`
M4=/opt/bio/gnu-tools/bin/m4 make PREFIX=%{installroot}

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/share

%files
%{installroot}/share/autoconf
%{installroot}/share/emacs/site-lisp/autoconf*
%{installroot}/share/info/autoconf.info
%{installroot}/share/info/standards.info
%{installroot}/share/man/man1/*
%defattr(755,root,root,755)
%{installroot}/bin/*
