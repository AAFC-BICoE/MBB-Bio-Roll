#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Data-Stag
#    Version:           0.14
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Data\:\:Stag
#

Name:           opt-perl-Data-Stag
Version:        0.14
Release:        1%{?dist}
Summary:        Structured Tags
License:        Unknown license: unknown
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Stag/
BuildRoot:      /tmp/cpantorpm/Data-Stag-0.14-inst
BuildArch:      %{_arch}
Source0:        http://search.cpan.org/authors/id/authors/id/C/CM/CMUNGALL/Data-Stag-0.14.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Data::Stag) = 0.14
Provides:       opt-perl(Data::Stag::Arr2HTML) = 0.14
Provides:       opt-perl(Data::Stag::Base) = 0.14
Provides:       opt-perl(Data::Stag::BaseGenerator) = 0.14
Provides:       opt-perl(Data::Stag::BaseHandler) = 0.14
Provides:       opt-perl(Data::Stag::ChainHandler) = 0.14
Provides:       opt-perl(Data::Stag::DTDWriter) = 0.14
Provides:       opt-perl(Data::Stag::GraphHandler) = 0.14
Provides:       opt-perl(Data::Stag::HashDB) = 0.14
Provides:       opt-perl(Data::Stag::ITextParser) = 0.14
Provides:       opt-perl(Data::Stag::ITextWriter) = 0.14
Provides:       opt-perl(Data::Stag::IndentParser) = 0.14
Provides:       opt-perl(Data::Stag::IndentWriter) = 0.14
Provides:       opt-perl(Data::Stag::JSONWriter) = 0.14
Provides:       opt-perl(Data::Stag::PerlWriter) = 0.14
Provides:       opt-perl(Data::Stag::PodParser) = 0.14
Provides:       opt-perl(Data::Stag::SAX2Stag) = 0.14
Provides:       opt-perl(Data::Stag::Simple) = 0.14
Provides:       opt-perl(Data::Stag::StagDB) = 0.14
Provides:       opt-perl(Data::Stag::StagI) = 0.14
Provides:       opt-perl(Data::Stag::StagImpl) = 0.14
Provides:       opt-perl(Data::Stag::SxprParser) = 0.14
Provides:       opt-perl(Data::Stag::SxprWriter) = 0.14
Provides:       opt-perl(Data::Stag::Util) = 0.14
Provides:       opt-perl(Data::Stag::Writer) = 0.14
Provides:       opt-perl(Data::Stag::XMLParser) = 0.14
Provides:       opt-perl(Data::Stag::XMLWriter) = 0.14
Provides:       opt-perl(Data::Stag::XSLHandler) = 0.14
Provides:       opt-perl(Data::Stag::XSLTHandler) = 0.14
Provides:       opt-perl(Data::Stag::null) = 0.14
Requires:       opt-perl
Requires:       opt-perl(IO::String)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(IO::String)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A perl module

%prep

%setup  -n Data-Stag-0.14
chmod -R u+w %{_builddir}/Data-Stag-%{version}

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
/opt/perl/bin/*
/opt/perl/lib/site_perl/5.26.0/*
/opt/perl/man/man1/*
/opt/perl/man/man3/*

%changelog
* Thu Oct 04 2018 Rocks 0.14-1
- Generated using cpantorpm

