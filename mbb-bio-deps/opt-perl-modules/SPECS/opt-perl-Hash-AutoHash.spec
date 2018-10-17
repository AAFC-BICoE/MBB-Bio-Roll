#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Hash-AutoHash
#    Version:           1.17
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Hash\:\:AutoHash
#

Name:           opt-perl-Hash-AutoHash
Version:        1.17
Release:        1%{?dist}
Summary:        Object-oriented access to real and tied hashes
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Hash-AutoHash/
BuildRoot:      /tmp/cpantorpm/Hash-AutoHash-1.17-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/N/NA/NATG/Hash-AutoHash-1.17.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Hash::AutoHash) = 1.17
Provides:       opt-perl(Hash::AutoHash::alias) = 1.17
Provides:       opt-perl(Hash::AutoHash::helper) = 1.17
Requires:       opt-perl
BuildRequires:  opt-perl
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This is yet another module that lets you access or change the elements of a
hash using methods with the same name as the element's key. It follows in
the footsteps of L<Hash::AsObject>, L<Hash::Inflator>,
L<Data::OpenStruct::Deep>, L<Object::AutoAccessor>, and probably others.
The main difference between this module and its forebears is that it
supports tied hashes, in addition to regular hashes. This allows a modular
division of labor: this class is generic and treats all hashes the same;
any special semantics come from the tied hash.

%prep

%setup  -n Hash-AutoHash-1.17
chmod -R u+w %{_builddir}/Hash-AutoHash-%{version}

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
* Thu Oct 04 2018 Rocks 1.17-1
- Generated using cpantorpm

