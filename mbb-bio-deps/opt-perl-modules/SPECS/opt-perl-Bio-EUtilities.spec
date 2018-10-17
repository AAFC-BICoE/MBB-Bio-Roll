#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Bio-EUtilities
#    Version:           1.75
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Bio\:\:Tools\:\:EUtilities
#

Name:           opt-perl-Bio-EUtilities
Version:        1.75
Release:        1%{?dist}
Summary:        Webagent which interacts with and retrieves data from NCBI's eUtils.
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Bio-EUtilities/
BuildRoot:      /tmp/cpantorpm/Bio-EUtilities-1.75-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/C/CJ/CJFIELDS/Bio-EUtilities-1.75.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Bio::DB::EUtilities) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::EUtilDataI) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::EUtilParameters) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::History) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::HistoryI) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::Info) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::Info::FieldInfo) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::Info::LinkInfo) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::Link) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::Link::LinkSet) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::Link::UrlLink) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::Query) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::Query::GlobalQuery) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::Summary) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::Summary::DocSum) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::Summary::Item) = 1.75
Provides:       opt-perl(Bio::Tools::EUtilities::Summary::ItemContainerI) = 1.75
Requires:       opt-perl
Requires:       opt-perl(Bio::ASN1::EntrezGene)
Requires:       opt-perl(Bio::DB::GenericWebAgent)
Requires:       opt-perl(Bio::ParameterBaseI)
Requires:       opt-perl(Bio::Root::IO)
Requires:       opt-perl(Bio::Root::Root)
Requires:       opt-perl(Bio::Root::RootI)
Requires:       opt-perl(Bio::Root::Version)
Requires:       opt-perl(Bio::SeqIO)
Requires:       opt-perl(Cwd)
Requires:       opt-perl(Data::Dumper)
Requires:       opt-perl(File::Spec)
Requires:       opt-perl(Getopt::Long)
Requires:       opt-perl(HTTP::Request)
Requires:       opt-perl(LWP::UserAgent)
Requires:       opt-perl(Text::CSV)
Requires:       opt-perl(Text::Wrap)
Requires:       opt-perl(URI)
Requires:       opt-perl(XML::Simple)
Requires:       opt-perl(base)
Requires:       opt-perl(strict)
Requires:       opt-perl(utf8)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Bio::ASN1::EntrezGene)
BuildRequires:  opt-perl(Bio::DB::GenericWebAgent)
BuildRequires:  opt-perl(Bio::ParameterBaseI)
BuildRequires:  opt-perl(Bio::Root::IO)
BuildRequires:  opt-perl(Bio::Root::Root)
BuildRequires:  opt-perl(Bio::Root::RootI)
BuildRequires:  opt-perl(Bio::Root::Version)
BuildRequires:  opt-perl(Bio::SeqIO)
BuildRequires:  opt-perl(Cwd)
BuildRequires:  opt-perl(Data::Dumper)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(File::Spec)
BuildRequires:  opt-perl(Getopt::Long)
BuildRequires:  opt-perl(HTTP::Request)
BuildRequires:  opt-perl(LWP::UserAgent)
BuildRequires:  opt-perl(Text::CSV)
BuildRequires:  opt-perl(Text::Wrap)
BuildRequires:  opt-perl(URI)
BuildRequires:  opt-perl(XML::Simple)
BuildRequires:  opt-perl(base)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(utf8)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A perl module

%prep

%setup  -n Bio-EUtilities-1.75
chmod -R u+w %{_builddir}/Bio-EUtilities-%{version}

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
* Thu Oct 04 2018 Rocks 1.75-1
- Generated using cpantorpm

