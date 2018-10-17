#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Test2-Suite
#    Version:           0.000115
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Test2\:\:Suite
#

Name:           opt-perl-Test2-Suite
Version:        0.000115
Release:        1%{?dist}
Summary:        Distribution with a rich set of tools built upon the Test2 framework.
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test2-Suite/
BuildRoot:      /tmp/cpantorpm/Test2-Suite-0.000115-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/E/EX/EXODIST/Test2-Suite-0.000115.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Test2::AsyncSubtest) = 0.000115
Provides:       opt-perl(Test2::AsyncSubtest::Event::Attach) = 0.000115
Provides:       opt-perl(Test2::AsyncSubtest::Event::Detach) = 0.000115
Provides:       opt-perl(Test2::AsyncSubtest::Formatter) = 0.000115
Provides:       opt-perl(Test2::AsyncSubtest::Hub) = 0.000115
Provides:       opt-perl(Test2::Bundle) = 0.000115
Provides:       opt-perl(Test2::Bundle::Extended) = 0.000115
Provides:       opt-perl(Test2::Bundle::More) = 0.000115
Provides:       opt-perl(Test2::Bundle::Simple) = 0.000115
Provides:       opt-perl(Test2::Compare) = 0.000115
Provides:       opt-perl(Test2::Compare::Array) = 0.000115
Provides:       opt-perl(Test2::Compare::Bag) = 0.000115
Provides:       opt-perl(Test2::Compare::Base) = 0.000115
Provides:       opt-perl(Test2::Compare::Bool) = 0.000115
Provides:       opt-perl(Test2::Compare::Custom) = 0.000115
Provides:       opt-perl(Test2::Compare::DeepRef) = 0.000115
Provides:       opt-perl(Test2::Compare::Delta) = 0.000115
Provides:       opt-perl(Test2::Compare::Event) = 0.000115
Provides:       opt-perl(Test2::Compare::EventMeta) = 0.000115
Provides:       opt-perl(Test2::Compare::Float) = 0.000115
Provides:       opt-perl(Test2::Compare::Hash) = 0.000115
Provides:       opt-perl(Test2::Compare::Meta) = 0.000115
Provides:       opt-perl(Test2::Compare::Negatable) = 0.000115
Provides:       opt-perl(Test2::Compare::Number) = 0.000115
Provides:       opt-perl(Test2::Compare::Object) = 0.000115
Provides:       opt-perl(Test2::Compare::OrderedSubset) = 0.000115
Provides:       opt-perl(Test2::Compare::Pattern) = 0.000115
Provides:       opt-perl(Test2::Compare::Ref) = 0.000115
Provides:       opt-perl(Test2::Compare::Regex) = 0.000115
Provides:       opt-perl(Test2::Compare::Scalar) = 0.000115
Provides:       opt-perl(Test2::Compare::Set) = 0.000115
Provides:       opt-perl(Test2::Compare::String) = 0.000115
Provides:       opt-perl(Test2::Compare::Undef) = 0.000115
Provides:       opt-perl(Test2::Compare::Wildcard) = 0.000115
Provides:       opt-perl(Test2::Event::Times) = 0.000115
Provides:       opt-perl(Test2::Manual) = 0.000115
Provides:       opt-perl(Test2::Manual::Anatomy) = 0.000115
Provides:       opt-perl(Test2::Manual::Anatomy::API) = 0.000115
Provides:       opt-perl(Test2::Manual::Anatomy::Context) = 0.000115
Provides:       opt-perl(Test2::Manual::Anatomy::EndToEnd) = 0.000115
Provides:       opt-perl(Test2::Manual::Anatomy::Event) = 0.000115
Provides:       opt-perl(Test2::Manual::Anatomy::Hubs) = 0.000115
Provides:       opt-perl(Test2::Manual::Anatomy::IPC) = 0.000115
Provides:       opt-perl(Test2::Manual::Anatomy::Utilities) = 0.000115
Provides:       opt-perl(Test2::Manual::Contributing) = 0.000115
Provides:       opt-perl(Test2::Manual::Testing) = 0.000115
Provides:       opt-perl(Test2::Manual::Testing::Introduction) = 0.000115
Provides:       opt-perl(Test2::Manual::Testing::Migrating) = 0.000115
Provides:       opt-perl(Test2::Manual::Testing::Planning) = 0.000115
Provides:       opt-perl(Test2::Manual::Testing::Todo) = 0.000115
Provides:       opt-perl(Test2::Manual::Tooling) = 0.000115
Provides:       opt-perl(Test2::Manual::Tooling::FirstTool) = 0.000115
Provides:       opt-perl(Test2::Manual::Tooling::Formatter) = 0.000115
Provides:       opt-perl(Test2::Manual::Tooling::Nesting) = 0.000115
Provides:       opt-perl(Test2::Manual::Tooling::Plugin::TestExit) = 0.000115
Provides:       opt-perl(Test2::Manual::Tooling::Plugin::TestingDone) = 0.000115
Provides:       opt-perl(Test2::Manual::Tooling::Plugin::ToolCompletes) = 0.000115
Provides:       opt-perl(Test2::Manual::Tooling::Plugin::ToolStarts) = 0.000115
Provides:       opt-perl(Test2::Manual::Tooling::Subtest) = 0.000115
Provides:       opt-perl(Test2::Manual::Tooling::TestBuilder) = 0.000115
Provides:       opt-perl(Test2::Manual::Tooling::Testing) = 0.000115
Provides:       opt-perl(Test2::Mock) = 0.000115
Provides:       opt-perl(Test2::Plugin) = 0.000115
Provides:       opt-perl(Test2::Plugin::BailOnFail) = 0.000115
Provides:       opt-perl(Test2::Plugin::DieOnFail) = 0.000115
Provides:       opt-perl(Test2::Plugin::ExitSummary) = 0.000115
Provides:       opt-perl(Test2::Plugin::SRand) = 0.000115
Provides:       opt-perl(Test2::Plugin::Times) = 0.000115
Provides:       opt-perl(Test2::Plugin::UTF8) = 0.000115
Provides:       opt-perl(Test2::Require) = 0.000115
Provides:       opt-perl(Test2::Require::AuthorTesting) = 0.000115
Provides:       opt-perl(Test2::Require::EnvVar) = 0.000115
Provides:       opt-perl(Test2::Require::Fork) = 0.000115
Provides:       opt-perl(Test2::Require::Module) = 0.000115
Provides:       opt-perl(Test2::Require::Perl) = 0.000115
Provides:       opt-perl(Test2::Require::RealFork) = 0.000115
Provides:       opt-perl(Test2::Require::Threads) = 0.000115
Provides:       opt-perl(Test2::Suite) = 0.000115
Provides:       opt-perl(Test2::Todo) = 0.000115
Provides:       opt-perl(Test2::Tools) = 0.000115
Provides:       opt-perl(Test2::Tools::AsyncSubtest) = 0.000115
Provides:       opt-perl(Test2::Tools::Basic) = 0.000115
Provides:       opt-perl(Test2::Tools::Class) = 0.000115
Provides:       opt-perl(Test2::Tools::ClassicCompare) = 0.000115
Provides:       opt-perl(Test2::Tools::Compare) = 0.000115
Provides:       opt-perl(Test2::Tools::Defer) = 0.000115
Provides:       opt-perl(Test2::Tools::Encoding) = 0.000115
Provides:       opt-perl(Test2::Tools::Event) = 0.000115
Provides:       opt-perl(Test2::Tools::Exception) = 0.000115
Provides:       opt-perl(Test2::Tools::Exports) = 0.000115
Provides:       opt-perl(Test2::Tools::GenTemp) = 0.000115
Provides:       opt-perl(Test2::Tools::Grab) = 0.000115
Provides:       opt-perl(Test2::Tools::Mock) = 0.000115
Provides:       opt-perl(Test2::Tools::Ref) = 0.000115
Provides:       opt-perl(Test2::Tools::Spec) = 0.000115
Provides:       opt-perl(Test2::Tools::Subtest) = 0.000115
Provides:       opt-perl(Test2::Tools::Target) = 0.000115
Provides:       opt-perl(Test2::Tools::Tester) = 0.000115
Provides:       opt-perl(Test2::Tools::Warnings) = 0.000115
Provides:       opt-perl(Test2::Util::Grabber) = 0.000115
Provides:       opt-perl(Test2::Util::Ref) = 0.000115
Provides:       opt-perl(Test2::Util::Stash) = 0.000115
Provides:       opt-perl(Test2::Util::Sub) = 0.000115
Provides:       opt-perl(Test2::Util::Table) = 0.000115
Provides:       opt-perl(Test2::Util::Table::Cell) = 0.000115
Provides:       opt-perl(Test2::Util::Table::LineBreak) = 0.000115
Provides:       opt-perl(Test2::Util::Term) = 0.000115
Provides:       opt-perl(Test2::Util::Times) = 0.000115
Provides:       opt-perl(Test2::V0) = 0.000115
Provides:       opt-perl(Test2::Workflow) = 0.000115
Provides:       opt-perl(Test2::Workflow::BlockBase) = 0.000115
Provides:       opt-perl(Test2::Workflow::Build) = 0.000115
Provides:       opt-perl(Test2::Workflow::Runner) = 0.000115
Provides:       opt-perl(Test2::Workflow::Task) = 0.000115
Provides:       opt-perl(Test2::Workflow::Task::Action) = 0.000115
Provides:       opt-perl(Test2::Workflow::Task::Group) = 0.000115
Requires:       opt-perl
Requires:       opt-perl(B)
Requires:       opt-perl(Carp)
Requires:       opt-perl(Data::Dumper)
Requires:       opt-perl(Exporter)
Requires:       opt-perl(Scalar::Util)
Requires:       opt-perl(Scope::Guard)
Requires:       opt-perl(Time::HiRes)
Requires:       opt-perl(overload)
Requires:       opt-perl(utf8)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(B)
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(Data::Dumper)
BuildRequires:  opt-perl(Exporter)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(Scalar::Util)
BuildRequires:  opt-perl(Scope::Guard)
BuildRequires:  opt-perl(Time::HiRes)
BuildRequires:  opt-perl(overload)
BuildRequires:  opt-perl(utf8)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Rich set of tools, plugins, bundles, etc built upon the L<Test2> testing
library. If you are interested in writing tests, this is the distribution
for you.

%prep

%setup  -n Test2-Suite-0.000115
chmod -R u+w %{_builddir}/Test2-Suite-%{version}

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
* Thu Oct 04 2018 Rocks 0.000115-1
- Generated using cpantorpm

