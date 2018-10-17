#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Statistics-Descriptive
#    Version:           3.0701
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Statistics\:\:Descriptive
#

Name:           opt-perl-Statistics-Descriptive
Version:        3.0701
Release:        1%{?dist}
Summary:        Module of basic descriptive statistical functions.
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Statistics-Descriptive/
BuildRoot:      /tmp/cpantorpm/Statistics-Descriptive-3.0701-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/S/SH/SHLOMIF/Statistics-Descriptive-3.0701.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Statistics::Descriptive) = 3.0701
Provides:       opt-perl(Statistics::Descriptive::Full) = 3.0701
Provides:       opt-perl(Statistics::Descriptive::Smoother) = 3.0701
Provides:       opt-perl(Statistics::Descriptive::Smoother::Exponential) = 3.0701
Provides:       opt-perl(Statistics::Descriptive::Smoother::Weightedexponential) = 3.0701
Provides:       opt-perl(Statistics::Descriptive::Sparse) = 3.0701
Requires:       opt-perl
Requires:       opt-perl(Carp)
Requires:       opt-perl(List::MoreUtils)
Requires:       opt-perl(List::Util)
Requires:       opt-perl(POSIX)
Requires:       opt-perl(base)
Requires:       opt-perl(parent)
Requires:       opt-perl(strict)
Requires:       opt-perl(vars)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(List::MoreUtils)
BuildRequires:  opt-perl(List::Util)
BuildRequires:  opt-perl(POSIX)
BuildRequires:  opt-perl(base)
BuildRequires:  opt-perl(parent)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(vars)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides basic functions used in descriptive statistics. It has
an object oriented design and supports two different types of data storage
and calculation objects: sparse and full. With the sparse method, none of
the data is stored and only a few statistical measures are available. Using
the full method, the entire data set is retained and additional functions
are available.

%prep

%setup  -n Statistics-Descriptive-3.0701
chmod -R u+w %{_builddir}/Statistics-Descriptive-%{version}

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
* Thu Oct 04 2018 Rocks 3.0701-1
- Generated using cpantorpm

