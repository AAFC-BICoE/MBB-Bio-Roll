#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-App-CPANtoRPM
#    Version:           1.08
#    cpantorpm version: 1.06
#    Date:              Thu October 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --NO-TESTS --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only App\:\:CPANtoRPM
#

Name:           opt-perl-App-CPANtoRPM
Version:        1.08
Release:        1%{?dist}
Summary:        An RPM packager for perl modules
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/App-CPANtoRPM/
BuildRoot:      /tmp/cpantorpm/App-CPANtoRPM-1.08-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/S/SB/SBECK/App-CPANtoRPM-1.08.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(App::CPANtoRPM) = 1.08
Provides:       opt-perl(cpantorpm) = 1.08
Requires:       opt-perl
Requires:       opt-perl(IO::File)
Requires:       opt-perl(POSIX)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(IO::File)
BuildRequires:  opt-perl(POSIX)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A perl module

%prep

%setup  -n App-CPANtoRPM-1.08
chmod -R u+w %{_builddir}/App-CPANtoRPM-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS" INSTALLDIRS=site SITEPREFIX=/opt/perl INSTALLSITEARCH=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi INSTALLSITELIB=/opt/perl/lib/site_perl/5.26.0 INSTALLSITEBIN=/opt/perl/bin INSTALLSITESCRIPT=/opt/perl/bin INSTALLSITEMAN1DIR=/opt/perl/man/man1 INSTALLSITEMAN3DIR=/opt/perl/man/man3 INSTALLSCRIPT=/opt/perl/bin
make %{?_smp_mflags}


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
/opt/perl/bin/*
/opt/perl/lib/site_perl/5.26.0/*
/opt/perl/man/man1/*
/opt/perl/man/man3/*

