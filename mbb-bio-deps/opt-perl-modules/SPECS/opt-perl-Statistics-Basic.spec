#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Statistics-Basic
#    Version:           1.6611
#    cpantorpm version: 1.08
#    Date:              Wed Oct 17 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Statistics\:\:Basic
#

Name:           opt-perl-Statistics-Basic
Version:        1.6611
Release:        1%{?dist}
Summary:        unknown
License:        OSI-Approved
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Statistics-Basic/
BuildRoot:      /tmp/cpantorpm/Statistics-Basic-1.6611-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/J/JE/JETTERO/Statistics-Basic-1.6611.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Statistics::Basic) = 1.6611
Provides:       opt-perl(Statistics::Basic::ComputedVector) = 1.6611
Provides:       opt-perl(Statistics::Basic::Correlation) = 1.6611
Provides:       opt-perl(Statistics::Basic::Covariance) = 1.6611
Provides:       opt-perl(Statistics::Basic::LeastSquareFit) = 1.6611
Provides:       opt-perl(Statistics::Basic::Mean) = 1.6611
Provides:       opt-perl(Statistics::Basic::Median) = 1.6611
Provides:       opt-perl(Statistics::Basic::Mode) = 1.6611
Provides:       opt-perl(Statistics::Basic::StdDev) = 1.6611
Provides:       opt-perl(Statistics::Basic::Variance) = 1.6611
Provides:       opt-perl(Statistics::Basic::Vector) = 1.6611
Provides:       opt-perl(Statistics::Basic::_OneVectorBase) = 1.6611
Provides:       opt-perl(Statistics::Basic::_TwoVectorBase) = 1.6611
Requires:       opt-perl
Requires:       opt-perl(Scalar::Util)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(Scalar::Util)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A perl module

%prep

%setup  -n Statistics-Basic-1.6611
chmod -R u+w %{_builddir}/Statistics-Basic-%{version}

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
* Wed Oct 17 2018 Rocks 1.6611-1
- Generated using cpantorpm

