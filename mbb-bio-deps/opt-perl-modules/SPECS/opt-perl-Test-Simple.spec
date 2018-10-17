#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Test-Simple
#    Version:           1.302140
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Test\:\:Simple
#

Name:           opt-perl-Test-Simple
Version:        1.302140
Release:        1%{?dist}
Summary:        Basic utilities for writing tests.
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Simple/
BuildRoot:      /tmp/cpantorpm/Test-Simple-1.302140-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/E/EX/EXODIST/Test-Simple-1.302140.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Test2) = 1.302140
Provides:       opt-perl(Test2::API) = 1.302140
Provides:       opt-perl(Test2::API::Breakage) = 1.302140
Provides:       opt-perl(Test2::API::Context) = 1.302140
Provides:       opt-perl(Test2::API::Instance) = 1.302140
Provides:       opt-perl(Test2::API::Stack) = 1.302140
Provides:       opt-perl(Test2::Event) = 1.302140
Provides:       opt-perl(Test2::Event::Bail) = 1.302140
Provides:       opt-perl(Test2::Event::Diag) = 1.302140
Provides:       opt-perl(Test2::Event::Encoding) = 1.302140
Provides:       opt-perl(Test2::Event::Exception) = 1.302140
Provides:       opt-perl(Test2::Event::Fail) = 1.302140
Provides:       opt-perl(Test2::Event::Generic) = 1.302140
Provides:       opt-perl(Test2::Event::Note) = 1.302140
Provides:       opt-perl(Test2::Event::Ok) = 1.302140
Provides:       opt-perl(Test2::Event::Pass) = 1.302140
Provides:       opt-perl(Test2::Event::Plan) = 1.302140
Provides:       opt-perl(Test2::Event::Skip) = 1.302140
Provides:       opt-perl(Test2::Event::Subtest) = 1.302140
Provides:       opt-perl(Test2::Event::TAP::Version) = 1.302140
Provides:       opt-perl(Test2::Event::V2) = 1.302140
Provides:       opt-perl(Test2::Event::Waiting) = 1.302140
Provides:       opt-perl(Test2::EventFacet) = 1.302140
Provides:       opt-perl(Test2::EventFacet::About) = 1.302140
Provides:       opt-perl(Test2::EventFacet::Amnesty) = 1.302140
Provides:       opt-perl(Test2::EventFacet::Assert) = 1.302140
Provides:       opt-perl(Test2::EventFacet::Control) = 1.302140
Provides:       opt-perl(Test2::EventFacet::Error) = 1.302140
Provides:       opt-perl(Test2::EventFacet::Hub) = 1.302140
Provides:       opt-perl(Test2::EventFacet::Info) = 1.302140
Provides:       opt-perl(Test2::EventFacet::Meta) = 1.302140
Provides:       opt-perl(Test2::EventFacet::Parent) = 1.302140
Provides:       opt-perl(Test2::EventFacet::Plan) = 1.302140
Provides:       opt-perl(Test2::EventFacet::Render) = 1.302140
Provides:       opt-perl(Test2::EventFacet::Trace) = 1.302140
Provides:       opt-perl(Test2::Formatter) = 1.302140
Provides:       opt-perl(Test2::Formatter::TAP) = 1.302140
Provides:       opt-perl(Test2::Hub) = 1.302140
Provides:       opt-perl(Test2::Hub::Interceptor) = 1.302140
Provides:       opt-perl(Test2::Hub::Interceptor::Terminator) = 1.302140
Provides:       opt-perl(Test2::Hub::Subtest) = 1.302140
Provides:       opt-perl(Test2::IPC) = 1.302140
Provides:       opt-perl(Test2::IPC::Driver) = 1.302140
Provides:       opt-perl(Test2::IPC::Driver::Files) = 1.302140
Provides:       opt-perl(Test2::Tools::Tiny) = 1.302140
Provides:       opt-perl(Test2::Util) = 1.302140
Provides:       opt-perl(Test2::Util::ExternalMeta) = 1.302140
Provides:       opt-perl(Test2::Util::Facets2Legacy) = 1.302140
Provides:       opt-perl(Test2::Util::HashBase) = 1.302140
Provides:       opt-perl(Test2::Util::Trace) = 1.302140
Provides:       opt-perl(Test::Builder) = 1.302140
Provides:       opt-perl(Test::Builder::Formatter) = 1.302140
Provides:       opt-perl(Test::Builder::IO::Scalar) = 2.114
Provides:       opt-perl(Test::Builder::Module) = 1.302140
Provides:       opt-perl(Test::Builder::Tester) = 1.302140
Provides:       opt-perl(Test::Builder::Tester::Color) = 1.302140
Provides:       opt-perl(Test::Builder::Tester::Tie) = 1.302140
Provides:       opt-perl(Test::Builder::TodoDiag) = 1.302140
Provides:       opt-perl(Test::More) = 1.302140
Provides:       opt-perl(Test::Simple) = 1.302140
Provides:       opt-perl(Test::Tester) = 1.302140
Provides:       opt-perl(Test::Tester::Capture) = 1.302140
Provides:       opt-perl(Test::Tester::CaptureRunner) = 1.302140
Provides:       opt-perl(Test::Tester::Delegate) = 1.302140
Provides:       opt-perl(Test::use::ok) = 1.302140
Provides:       opt-perl(ok) = 1.302140
Requires:       opt-perl
Requires:       opt-perl(File::Spec)
Requires:       opt-perl(File::Temp)
Requires:       opt-perl(Storable)
Requires:       opt-perl(utf8)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(File::Spec)
BuildRequires:  opt-perl(File::Temp)
BuildRequires:  opt-perl(Storable)
BuildRequires:  opt-perl(utf8)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
** If you are unfamiliar with testing read L<Test::Tutorial first!> **

%prep

%setup  -n Test-Simple-1.302140
chmod -R u+w %{_builddir}/Test-Simple-%{version}

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
%perl_sitelib/*

%changelog
* Thu Oct 04 2018 Rocks 1.302140-1
- Generated using cpantorpm

