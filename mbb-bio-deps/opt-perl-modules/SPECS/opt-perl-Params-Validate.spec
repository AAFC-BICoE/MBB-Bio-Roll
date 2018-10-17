#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Params-Validate
#    Version:           1.29
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Params\:\:Validate
#

Name:           opt-perl-Params-Validate
Version:        1.29
Release:        1%{?dist}
Summary:        Validate method/function parameters
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Params-Validate/
BuildRoot:      /tmp/cpantorpm/Params-Validate-1.29-inst
BuildArch:      %{_arch}
Source0:        http://search.cpan.org/authors/id/authors/id/D/DR/DROLSKY/Params-Validate-1.29.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Params::Validate) = 1.29
Provides:       opt-perl(Params::Validate::Constants) = 1.29
Provides:       opt-perl(Params::Validate::PP) = 1.29
Provides:       opt-perl(Params::Validate::XS) = 1.29
Requires:       opt-perl
Requires:       opt-perl(Carp)
Requires:       opt-perl(Exporter)
Requires:       opt-perl(Module::Implementation)
Requires:       opt-perl(XSLoader)
Requires:       opt-perl(strict)
Requires:       opt-perl(vars)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(Exporter)
BuildRequires:  opt-perl(ExtUtils::CBuilder)
BuildRequires:  opt-perl(Module::Implementation)
BuildRequires:  opt-perl(XSLoader)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(vars)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
< I would recommend you consider using L<Params::ValidationCompiler
instead. That module, despite being pure Perl, is significantly faster
than this one, at the cost of having to adopt a type system such as
L<Specio>, L<Type::Tiny>, or the one shipped with L<Moose> >>.

%prep

%setup  -n Params-Validate-1.29
chmod -R u+w %{_builddir}/Params-Validate-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Build.PL optimize="$RPM_OPT_FLAGS" --installdirs site --install_path arch=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi --install_path lib=/opt/perl/lib/site_perl/5.26.0 --install_path script=/opt/perl/bin --install_path bin=/opt/perl/bin --install_path libdoc=/opt/perl/man/man3 --install_path bindoc=/opt/perl/man/man1
./Build

#
# This is included here instead of in the 'check' section because
# older versions of rpmbuild (such as the one distributed with RHEL5)
# do not do 'check' by default.
#

if [ -z "$RPMBUILD_NOTESTS" ]; then
   ./Build test
fi

%install

rm -rf $RPM_BUILD_ROOT
./Build pure_install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%clean

rm -rf $RPM_BUILD_ROOT

%files

%defattr(-,root,root,-)
/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi/*
/opt/perl/man/man3/*

%changelog
* Thu Oct 04 2018 Rocks 1.29-1
- Generated using cpantorpm

