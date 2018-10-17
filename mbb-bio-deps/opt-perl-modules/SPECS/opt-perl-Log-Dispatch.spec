#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Log-Dispatch
#    Version:           2.68
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Log\:\:Dispatch
#

Name:           opt-perl-Log-Dispatch
Version:        2.68
Release:        1%{?dist}
Summary:        Dispatches messages to one or more outputs
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Log-Dispatch/
BuildRoot:      /tmp/cpantorpm/Log-Dispatch-2.68-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/D/DR/DROLSKY/Log-Dispatch-2.68.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Log::Dispatch) = 2.68
Provides:       opt-perl(Log::Dispatch::ApacheLog) = 2.68
Provides:       opt-perl(Log::Dispatch::Base) = 2.68
Provides:       opt-perl(Log::Dispatch::Code) = 2.68
Provides:       opt-perl(Log::Dispatch::Email) = 2.68
Provides:       opt-perl(Log::Dispatch::Email::MIMELite) = 2.68
Provides:       opt-perl(Log::Dispatch::Email::MailSend) = 2.68
Provides:       opt-perl(Log::Dispatch::Email::MailSender) = 2.68
Provides:       opt-perl(Log::Dispatch::Email::MailSendmail) = 2.68
Provides:       opt-perl(Log::Dispatch::File) = 2.68
Provides:       opt-perl(Log::Dispatch::File::Locked) = 2.68
Provides:       opt-perl(Log::Dispatch::Handle) = 2.68
Provides:       opt-perl(Log::Dispatch::Null) = 2.68
Provides:       opt-perl(Log::Dispatch::Output) = 2.68
Provides:       opt-perl(Log::Dispatch::Screen) = 2.68
Provides:       opt-perl(Log::Dispatch::Syslog) = 2.68
Provides:       opt-perl(Log::Dispatch::Types) = 2.68
Provides:       opt-perl(Log::Dispatch::Vars) = 2.68
Requires:       opt-perl
Requires:       opt-perl(Carp)
Requires:       opt-perl(Devel::GlobalDestruction)
Requires:       opt-perl(Encode)
Requires:       opt-perl(Exporter)
Requires:       opt-perl(Fcntl)
Requires:       opt-perl(IO::Handle)
Requires:       opt-perl(Module::Runtime)
Requires:       opt-perl(Params::ValidationCompiler)
Requires:       opt-perl(Scalar::Util)
Requires:       opt-perl(Specio::Declare)
Requires:       opt-perl(Specio::Exporter)
Requires:       opt-perl(Specio::Library::Builtins)
Requires:       opt-perl(Specio::Library::Numeric)
Requires:       opt-perl(Specio::Library::String)
Requires:       opt-perl(Try::Tiny)
Requires:       opt-perl(base)
Requires:       opt-perl(namespace::autoclean)
Requires:       opt-perl(parent)
Requires:       opt-perl(strict)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(Devel::GlobalDestruction)
BuildRequires:  opt-perl(Encode)
BuildRequires:  opt-perl(Exporter)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(Fcntl)
BuildRequires:  opt-perl(IO::Handle)
BuildRequires:  opt-perl(Module::Runtime)
BuildRequires:  opt-perl(Params::ValidationCompiler)
BuildRequires:  opt-perl(Scalar::Util)
BuildRequires:  opt-perl(Specio::Declare)
BuildRequires:  opt-perl(Specio::Exporter)
BuildRequires:  opt-perl(Specio::Library::Builtins)
BuildRequires:  opt-perl(Specio::Library::Numeric)
BuildRequires:  opt-perl(Specio::Library::String)
BuildRequires:  opt-perl(Try::Tiny)
BuildRequires:  opt-perl(base)
BuildRequires:  opt-perl(namespace::autoclean)
BuildRequires:  opt-perl(parent)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module manages a set of Log::Dispatch::* output objects that can be
logged to via a unified interface.

%prep

%setup  -n Log-Dispatch-2.68
chmod -R u+w %{_builddir}/Log-Dispatch-%{version}

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
* Thu Oct 04 2018 Rocks 2.68-1
- Generated using cpantorpm

