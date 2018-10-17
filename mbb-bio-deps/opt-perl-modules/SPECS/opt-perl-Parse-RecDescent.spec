#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Parse-RecDescent
#    Version:           1.967015
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Parse\:\:RecDescent
#

Name:           opt-perl-Parse-RecDescent
Version:        1.967015
Release:        1%{?dist}
Summary:        Generate Recursive-Descent Parsers
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Parse-RecDescent/
BuildRoot:      /tmp/cpantorpm/Parse-RecDescent-1.967015-inst
BuildArch:      %{_arch}
Source0:        http://search.cpan.org/authors/id/authors/id/J/JT/JTBRAUN/Parse-RecDescent-1.967015.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Parse::RecDescent) = 1.967015
Provides:       opt-perl(Parse::RecDescent::Action) = 1.967015
Provides:       opt-perl(Parse::RecDescent::ColCounter) = 1.967015
Provides:       opt-perl(Parse::RecDescent::Directive) = 1.967015
Provides:       opt-perl(Parse::RecDescent::Error) = 1.967015
Provides:       opt-perl(Parse::RecDescent::Expectation) = 1.967015
Provides:       opt-perl(Parse::RecDescent::InterpLit) = 1.967015
Provides:       opt-perl(Parse::RecDescent::LineCounter) = 1.967015
Provides:       opt-perl(Parse::RecDescent::Literal) = 1.967015
Provides:       opt-perl(Parse::RecDescent::OffsetCounter) = 1.967015
Provides:       opt-perl(Parse::RecDescent::Operator) = 1.967015
Provides:       opt-perl(Parse::RecDescent::Production) = 1.967015
Provides:       opt-perl(Parse::RecDescent::Repetition) = 1.967015
Provides:       opt-perl(Parse::RecDescent::Result) = 1.967015
Provides:       opt-perl(Parse::RecDescent::Rule) = 1.967015
Provides:       opt-perl(Parse::RecDescent::Subrule) = 1.967015
Provides:       opt-perl(Parse::RecDescent::Token) = 1.967015
Provides:       opt-perl(Parse::RecDescent::UncondReject) = 1.967015
Requires:       opt-perl
Requires:       opt-perl(Test::More)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Test::More)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
=head2 Overview

%prep

%setup  -n Parse-RecDescent-1.967015
chmod -R u+w %{_builddir}/Parse-RecDescent-%{version}

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
* Thu Oct 04 2018 Rocks 1.967015-1
- Generated using cpantorpm

