#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Config-General
#    Version:           2.63
#    cpantorpm version: 1.08
#    Date:              Wed Oct 17 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Config\:\:General
#

Name:           opt-perl-Config-General
Version:        2.63
Release:        1%{?dist}
Summary:        unknown
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Config-General/
BuildRoot:      /tmp/cpantorpm/Config-General-2.63-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/T/TL/TLINDEN/Config-General-2.63.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Config::General) = 2.63
Provides:       opt-perl(Config::General::Extended) = 2.07
Provides:       opt-perl(Config::General::Interpolated) = 2.15
Requires:       opt-perl
Requires:       opt-perl(File::Glob)
Requires:       opt-perl(File::Spec::Functions)
Requires:       opt-perl(FileHandle)
Requires:       opt-perl(IO::File)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(File::Glob)
BuildRequires:  opt-perl(File::Spec::Functions)
BuildRequires:  opt-perl(FileHandle)
BuildRequires:  opt-perl(IO::File)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module opens a config file and parses its contents for you. The new
method requires one parameter which needs to be a filename. The method
getall returns a hash which contains all options and its associated
values of your config file.

%prep

%setup  -n Config-General-2.63
chmod -R u+w %{_builddir}/Config-General-%{version}

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
* Wed Oct 17 2018 Rocks 2.63-1
- Generated using cpantorpm

