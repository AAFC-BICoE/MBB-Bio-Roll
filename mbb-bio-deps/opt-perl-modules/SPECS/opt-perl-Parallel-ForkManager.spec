#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Parallel-ForkManager
#    Version:           1.20
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Parallel\:\:ForkManager
#

Name:           opt-perl-Parallel-ForkManager
Version:        1.20
Release:        1%{?dist}
Summary:        A simple parallel processing fork manager
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Parallel-ForkManager/
BuildRoot:      /tmp/cpantorpm/Parallel-ForkManager-1.20-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/Y/YA/YANICK/Parallel-ForkManager-1.20.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Parallel::ForkManager) = 1.20
Requires:       opt-perl
Requires:       opt-perl(Carp)
Requires:       opt-perl(File::Path)
Requires:       opt-perl(File::Spec)
Requires:       opt-perl(File::Temp)
Requires:       opt-perl(POSIX)
Requires:       opt-perl(Storable)
Requires:       opt-perl(strict)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(File::Path)
BuildRequires:  opt-perl(File::Spec)
BuildRequires:  opt-perl(File::Temp)
BuildRequires:  opt-perl(POSIX)
BuildRequires:  opt-perl(Storable)
BuildRequires:  opt-perl(strict)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module is intended for use in operations that can be done in parallel
where the number of processes to be forked off should be limited. Typical
use is a downloader which will be retrieving hundreds/thousands of files.

%prep

%setup  -n Parallel-ForkManager-1.20
chmod -R u+w %{_builddir}/Parallel-ForkManager-%{version}

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
* Thu Oct 04 2018 Rocks 1.20-1
- Generated using cpantorpm

