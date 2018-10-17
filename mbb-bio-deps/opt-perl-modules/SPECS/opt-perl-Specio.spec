#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Specio
#    Version:           0.42
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Specio
#

Name:           opt-perl-Specio
Version:        0.42
Release:        1%{?dist}
Summary:        Type constraints and coercions for Perl
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Specio/
BuildRoot:      /tmp/cpantorpm/Specio-0.42-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/D/DR/DROLSKY/Specio-0.42.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Specio) = 0.42
Provides:       opt-perl(Specio::Coercion) = 0.42
Provides:       opt-perl(Specio::Constraint::AnyCan) = 0.42
Provides:       opt-perl(Specio::Constraint::AnyDoes) = 0.42
Provides:       opt-perl(Specio::Constraint::AnyIsa) = 0.42
Provides:       opt-perl(Specio::Constraint::Enum) = 0.42
Provides:       opt-perl(Specio::Constraint::Intersection) = 0.42
Provides:       opt-perl(Specio::Constraint::ObjectCan) = 0.42
Provides:       opt-perl(Specio::Constraint::ObjectDoes) = 0.42
Provides:       opt-perl(Specio::Constraint::ObjectIsa) = 0.42
Provides:       opt-perl(Specio::Constraint::Parameterizable) = 0.42
Provides:       opt-perl(Specio::Constraint::Parameterized) = 0.42
Provides:       opt-perl(Specio::Constraint::Role::CanType) = 0.42
Provides:       opt-perl(Specio::Constraint::Role::DoesType) = 0.42
Provides:       opt-perl(Specio::Constraint::Role::Interface) = 0.42
Provides:       opt-perl(Specio::Constraint::Role::IsaType) = 0.42
Provides:       opt-perl(Specio::Constraint::Simple) = 0.42
Provides:       opt-perl(Specio::Constraint::Structurable) = 0.42
Provides:       opt-perl(Specio::Constraint::Structured) = 0.42
Provides:       opt-perl(Specio::Constraint::Union) = 0.42
Provides:       opt-perl(Specio::Declare) = 0.42
Provides:       opt-perl(Specio::DeclaredAt) = 0.42
Provides:       opt-perl(Specio::Exception) = 0.42
Provides:       opt-perl(Specio::Exporter) = 0.42
Provides:       opt-perl(Specio::Helpers) = 0.42
Provides:       opt-perl(Specio::Library::Builtins) = 0.42
Provides:       opt-perl(Specio::Library::Numeric) = 0.42
Provides:       opt-perl(Specio::Library::Perl) = 0.42
Provides:       opt-perl(Specio::Library::String) = 0.42
Provides:       opt-perl(Specio::Library::Structured) = 0.42
Provides:       opt-perl(Specio::Library::Structured::Dict) = 0.42
Provides:       opt-perl(Specio::Library::Structured::Map) = 0.42
Provides:       opt-perl(Specio::Library::Structured::Tuple) = 0.42
Provides:       opt-perl(Specio::OO) = 0.42
Provides:       opt-perl(Specio::PartialDump) = 0.42
Provides:       opt-perl(Specio::Registry) = 0.42
Provides:       opt-perl(Specio::Role::Inlinable) = 0.42
Provides:       opt-perl(Specio::Subs) = 0.42
Provides:       opt-perl(Specio::TypeChecks) = 0.42
Provides:       opt-perl(Test::Specio) = 0.42
Requires:       opt-perl
Requires:       opt-perl(B)
Requires:       opt-perl(Carp)
Requires:       opt-perl(Devel::StackTrace)
Requires:       opt-perl(Eval::Closure)
Requires:       opt-perl(Exporter)
Requires:       opt-perl(IO::File)
Requires:       opt-perl(MRO::Compat)
Requires:       opt-perl(Module::Runtime)
Requires:       opt-perl(Role::Tiny::With)
Requires:       opt-perl(Scalar::Util)
Requires:       opt-perl(Storable)
Requires:       opt-perl(Sub::Quote)
Requires:       opt-perl(Test::Fatal)
Requires:       opt-perl(Try::Tiny)
Requires:       opt-perl(overload)
Requires:       opt-perl(parent)
Requires:       opt-perl(re)
Requires:       opt-perl(strict)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(B)
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(Devel::StackTrace)
BuildRequires:  opt-perl(Eval::Closure)
BuildRequires:  opt-perl(Exporter)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(IO::File)
BuildRequires:  opt-perl(MRO::Compat)
BuildRequires:  opt-perl(Module::Runtime)
BuildRequires:  opt-perl(Role::Tiny::With)
BuildRequires:  opt-perl(Scalar::Util)
BuildRequires:  opt-perl(Storable)
BuildRequires:  opt-perl(Sub::Quote)
BuildRequires:  opt-perl(Test::Fatal)
BuildRequires:  opt-perl(Try::Tiny)
BuildRequires:  opt-perl(overload)
BuildRequires:  opt-perl(parent)
BuildRequires:  opt-perl(re)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Specio distribution provides classes for representing type
constraints and coercion, along with syntax sugar for declaring them.

%prep

%setup  -n Specio-0.42
chmod -R u+w %{_builddir}/Specio-%{version}

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
* Thu Oct 04 2018 Rocks 0.42-1
- Generated using cpantorpm

