#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Path-Tiny
#    Version:           0.108
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Path\:\:Tiny
#

Name:           opt-perl-Path-Tiny
Version:        0.108
Release:        1%{?dist}
Summary:        File path utility
License:        Unknown license: apache_2_0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Path-Tiny/
BuildRoot:      /tmp/cpantorpm/Path-Tiny-0.108-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/D/DA/DAGOLDEN/Path-Tiny-0.108.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Path::Tiny) = 0.108
Provides:       opt-perl(Path::Tiny::Error) = 0.108
Requires:       opt-perl
Requires:       opt-perl(Carp)
Requires:       opt-perl(Cwd)
Requires:       opt-perl(Encode)
Requires:       opt-perl(Fcntl)
Requires:       opt-perl(File::Copy)
Requires:       opt-perl(File::Glob)
Requires:       opt-perl(File::stat)
Requires:       opt-perl(constant)
Requires:       opt-perl(overload)
Requires:       opt-perl(strict)
Requires:       opt-perl(warnings)
Requires:       opt-perl(warnings::register)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(Cwd)
BuildRequires:  opt-perl(Encode)
BuildRequires:  opt-perl(Fcntl)
BuildRequires:  opt-perl(File::Copy)
BuildRequires:  opt-perl(File::Glob)
BuildRequires:  opt-perl(File::stat)
BuildRequires:  opt-perl(constant)
BuildRequires:  opt-perl(overload)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(warnings)
BuildRequires:  opt-perl(warnings::register)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides a small, fast utility for working with file paths. It
is friendlier to use than L<File::Spec> and provides easy access to
functions from several other core file handling modules. It aims to be
smaller and faster than many alternatives on CPAN, while helping people do
many common things in consistent and less error-prone ways.

%prep

%setup  -n Path-Tiny-0.108
chmod -R u+w %{_builddir}/Path-Tiny-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS" INSTALLDIRS=site SITEPREFIX=/opt/perl INSTALLSITEARCH=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi INSTALLSITELIB=/opt/perl/lib/site_perl/5.26.0 INSTALLSITEBIN=/opt/perl/bin INSTALLSITESCRIPT=/opt/perl/bin INSTALLSITEMAN1DIR=/opt/perl/man/man1 INSTALLSITEMAN3DIR=/opt/perl/man/man3 INSTALLSCRIPT=/opt/perl/bin
make %{?_smp_mflags}

#
# This is included here instead of in the 'check' section because
# older versions of rpmbuild (such as the one distributed with RHEL5)
# do not do 'check' by default.
#

if [ -z "$RPMBUILD_NOTESTS" ]; then
   make test
fi

%install

rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
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
* Thu Oct 04 2018 Rocks 0.108-1
- Generated using cpantorpm

