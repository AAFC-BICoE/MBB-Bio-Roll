#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Path-Class
#    Version:           0.37
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Path\:\:Class
#

Name:           opt-perl-Path-Class
Version:        0.37
Release:        1%{?dist}
Summary:        Cross-platform path specification manipulation
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Path-Class/
BuildRoot:      /tmp/cpantorpm/Path-Class-0.37-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/K/KW/KWILLIAMS/Path-Class-0.37.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Path::Class) = 0.37
Provides:       opt-perl(Path::Class::Dir) = 0.37
Provides:       opt-perl(Path::Class::Entity) = 0.37
Provides:       opt-perl(Path::Class::File) = 0.37
Requires:       opt-perl
Requires:       opt-perl(Carp)
Requires:       opt-perl(Cwd)
Requires:       opt-perl(Exporter)
Requires:       opt-perl(File::Copy)
Requires:       opt-perl(File::Path)
Requires:       opt-perl(File::Temp)
Requires:       opt-perl(File::stat)
Requires:       opt-perl(IO::Dir)
Requires:       opt-perl(IO::File)
Requires:       opt-perl(Perl::OSType)
Requires:       opt-perl(Scalar::Util)
Requires:       opt-perl(overload)
Requires:       opt-perl(parent)
Requires:       opt-perl(strict)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(Cwd)
BuildRequires:  opt-perl(Exporter)
BuildRequires:  opt-perl(File::Copy)
BuildRequires:  opt-perl(File::Path)
BuildRequires:  opt-perl(File::Temp)
BuildRequires:  opt-perl(File::stat)
BuildRequires:  opt-perl(IO::Dir)
BuildRequires:  opt-perl(IO::File)
BuildRequires:  opt-perl(Perl::OSType)
BuildRequires:  opt-perl(Scalar::Util)
BuildRequires:  opt-perl(overload)
BuildRequires:  opt-perl(parent)
BuildRequires:  opt-perl(strict)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Path::Class is a module for manipulation of file and directory
specifications (strings describing their locations, like
'/home/ken/foo.txt' or 'C:\Windows\Foo.txt') in a cross-platform
manner. It supports pretty much every platform Perl runs on, including
Unix, Windows, Mac, VMS, Epoc, Cygwin, OS/2, and NetWare.

%prep

%setup  -n Path-Class-0.37
chmod -R u+w %{_builddir}/Path-Class-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Build.PL optimize="$RPM_OPT_FLAGS" --installdirs site --install_path arch=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi --install_path lib=/opt/perl/lib/site_perl/5.26.0 --install_path script=/opt/perl/bin --install_path bin=/opt/perl/bin --install_path libdoc=/opt/perl/man/man3 --install_path bindoc=/opt/perl/man/man1
./Build

#
# This is included here instead of in the 'check' section because
# older versions of rpmbuild (such as the one distributed with RHEL5)
# do not do 'check' by default.
#

if [ -z "$RPMBUILD_NOTESTS" ]; then
   ./Build test
fi

%install

rm -rf $RPM_BUILD_ROOT
./Build pure_install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%clean

rm -rf $RPM_BUILD_ROOT

%files

%defattr(-,root,root,-)
/opt/perl/lib/site_perl/5.26.0/*
/opt/perl/man/man3/*

%changelog
* Thu Oct 04 2018 Rocks 0.37-1
- Generated using cpantorpm

