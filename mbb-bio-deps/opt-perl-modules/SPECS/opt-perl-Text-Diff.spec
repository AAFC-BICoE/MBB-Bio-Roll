#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Text-Diff
#    Version:           1.45
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Text\:\:Diff
#

Name:           opt-perl-Text-Diff
Version:        1.45
Release:        1%{?dist}
Summary:        Perform diffs on files and record sets
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Text-Diff/
BuildRoot:      /tmp/cpantorpm/Text-Diff-1.45-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/N/NE/NEILB/Text-Diff-1.45.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Text::Diff) = 1.45
Provides:       opt-perl(Text::Diff::Base) = 1.45
Provides:       opt-perl(Text::Diff::Config) = 1.44
Provides:       opt-perl(Text::Diff::Table) = 1.44
Requires:       opt-perl
Requires:       opt-perl(Exporter)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Exporter)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
diff() provides a basic set of services akin to the GNU diff utility.
It is not anywhere near as feature complete as GNU diff, but it is
better integrated with Perl and available on all platforms. It is often
faster than shelling out to a system's diff executable for small files,
and generally slower on larger files.

%prep

%setup  -n Text-Diff-1.45
chmod -R u+w %{_builddir}/Text-Diff-%{version}

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
* Thu Oct 04 2018 Rocks 1.45-1
- Generated using cpantorpm

