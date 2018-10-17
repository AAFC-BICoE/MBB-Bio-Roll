#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-File-pushd
#    Version:           1.016
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only File\:\:pushd
#

Name:           opt-perl-File-pushd
Version:        1.016
Release:        1%{?dist}
Summary:        change directory temporarily for a limited scope
License:        Unknown license: apache_2_0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/File-pushd/
BuildRoot:      /tmp/cpantorpm/File-pushd-1.016-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/D/DA/DAGOLDEN/File-pushd-1.016.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(File::pushd) = 1.016
Requires:       opt-perl
Requires:       opt-perl(Carp)
Requires:       opt-perl(Cwd)
Requires:       opt-perl(Exporter)
Requires:       opt-perl(File::Path)
Requires:       opt-perl(File::Spec)
Requires:       opt-perl(File::Temp)
Requires:       opt-perl(overload)
Requires:       opt-perl(strict)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(Cwd)
BuildRequires:  opt-perl(Exporter)
BuildRequires:  opt-perl(File::Path)
BuildRequires:  opt-perl(File::Spec)
BuildRequires:  opt-perl(File::Temp)
BuildRequires:  opt-perl(overload)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
File::pushd does a temporary chdir that is easily and automatically
reverted, similar to pushd in some Unix command shells. It works by
creating an object that caches the original working directory. When the
object is destroyed, the destructor calls chdir to revert to the
original working directory. By storing the object in a lexical variable
with a limited scope, this happens automatically at the end of the scope.

%prep

%setup  -n File-pushd-1.016
chmod -R u+w %{_builddir}/File-pushd-%{version}

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
* Thu Oct 04 2018 Rocks 1.016-1
- Generated using cpantorpm

