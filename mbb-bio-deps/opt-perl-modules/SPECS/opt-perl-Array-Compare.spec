#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Array-Compare
#    Version:           v3.0.1
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Array\:\:Compare
#

Name:           opt-perl-Array-Compare
Version:        v3.0.1
Release:        1%{?dist}
Summary:        Perl extension for comparing arrays.
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Array-Compare/
BuildRoot:      /tmp/cpantorpm/Array-Compare-v3.0.1-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/D/DA/DAVECROSS/Array-Compare-v3.0.1.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Array::Compare) = 3.0.1
Requires:       opt-perl
Requires:       opt-perl(Carp)
Requires:       opt-perl(Moo)
Requires:       opt-perl(Types::Standard)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(Moo)
BuildRequires:  opt-perl(Test::NoWarnings)
BuildRequires:  opt-perl(Types::Standard)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
If you have two arrays and you want to know if they are the same or
different, then Array::Compare will be useful to you.

%prep

%setup  -n Array-Compare-v3.0.1
chmod -R u+w %{_builddir}/Array-Compare-%{version}

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
* Thu Oct 04 2018 Rocks v3.0.1-1
- Generated using cpantorpm

