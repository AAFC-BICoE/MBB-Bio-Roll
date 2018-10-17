#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Type-Tiny
#    Version:           1.004002
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Type\:\:Tiny
#

Name:           opt-perl-Type-Tiny
Version:        1.004002
Release:        1%{?dist}
Summary:        tiny, yet Moo(se)-compatible type constraint
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Type-Tiny/
BuildRoot:      /tmp/cpantorpm/Type-Tiny-1.004002-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/T/TO/TOBYINK/Type-Tiny-1.004002.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Devel::TypeTiny::Perl56Compat) = 1.004002
Provides:       opt-perl(Devel::TypeTiny::Perl58Compat) = 1.004002
Provides:       opt-perl(Error::TypeTiny) = 1.004002
Provides:       opt-perl(Error::TypeTiny::Assertion) = 1.004002
Provides:       opt-perl(Error::TypeTiny::Compilation) = 1.004002
Provides:       opt-perl(Error::TypeTiny::WrongNumberOfParameters) = 1.004002
Provides:       opt-perl(Eval::TypeTiny) = 1.004002
Provides:       opt-perl(Reply::Plugin::TypeTiny) = 1.004002
Provides:       opt-perl(Test::TypeTiny) = 1.004002
Provides:       opt-perl(Type::Coercion) = 1.004002
Provides:       opt-perl(Type::Coercion::FromMoose) = 1.004002
Provides:       opt-perl(Type::Coercion::Union) = 1.004002
Provides:       opt-perl(Type::Library) = 1.004002
Provides:       opt-perl(Type::Params) = 1.004002
Provides:       opt-perl(Type::Parser) = 1.004002
Provides:       opt-perl(Type::Registry) = 1.004002
Provides:       opt-perl(Type::Tiny) = 1.004002
Provides:       opt-perl(Type::Tiny::Class) = 1.004002
Provides:       opt-perl(Type::Tiny::Duck) = 1.004002
Provides:       opt-perl(Type::Tiny::Enum) = 1.004002
Provides:       opt-perl(Type::Tiny::Intersection) = 1.004002
Provides:       opt-perl(Type::Tiny::Role) = 1.004002
Provides:       opt-perl(Type::Tiny::Union) = 1.004002
Provides:       opt-perl(Type::Utils) = 1.004002
Provides:       opt-perl(Types::Common::Numeric) = 1.004002
Provides:       opt-perl(Types::Common::String) = 1.004002
Provides:       opt-perl(Types::Standard) = 1.004002
Provides:       opt-perl(Types::Standard::ArrayRef) = 1.004002
Provides:       opt-perl(Types::Standard::CycleTuple) = 1.004002
Provides:       opt-perl(Types::Standard::Dict) = 1.004002
Provides:       opt-perl(Types::Standard::HashRef) = 1.004002
Provides:       opt-perl(Types::Standard::Map) = 1.004002
Provides:       opt-perl(Types::Standard::ScalarRef) = 1.004002
Provides:       opt-perl(Types::Standard::StrMatch) = 1.004002
Provides:       opt-perl(Types::Standard::Tied) = 1.004002
Provides:       opt-perl(Types::Standard::Tuple) = 1.004002
Provides:       opt-perl(Types::TypeTiny) = 1.004002
Requires:       opt-perl
BuildRequires:  opt-perl
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
L<Type::Tiny> is a tiny class for creating Moose-like type constraint
objects which are compatible with Moo, Moose and Mouse.

%prep

%setup  -n Type-Tiny-1.004002
chmod -R u+w %{_builddir}/Type-Tiny-%{version}

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
* Thu Oct 04 2018 Rocks 1.004002-1
- Generated using cpantorpm

