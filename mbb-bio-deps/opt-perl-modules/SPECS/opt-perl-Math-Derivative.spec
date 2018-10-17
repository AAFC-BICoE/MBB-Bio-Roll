#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Math-Derivative
#    Version:           1.01
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Math\:\:Derivative
#

Name:           opt-perl-Math-Derivative
Version:        1.01
Release:        1%{?dist}
Summary:        Numeric 1st and 2nd order differentiation.
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Math-Derivative/
BuildRoot:      /tmp/cpantorpm/Math-Derivative-1.01-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/J/JG/JGAMBLE/Math-Derivative-1.01.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Math::Derivative) = 1.01
Requires:       opt-perl
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Module::Build)
BuildRequires:  opt-perl(Test::More)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This Perl package exports functions that numerically approximate first and
second order differentiation on vectors of data. The accuracy of the
approximation will depend upon the differences between the successive
values in the X array.

%prep

%setup  -n Math-Derivative-1.01
chmod -R u+w %{_builddir}/Math-Derivative-%{version}

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
* Thu Oct 04 2018 Rocks 1.01-1
- Generated using cpantorpm

