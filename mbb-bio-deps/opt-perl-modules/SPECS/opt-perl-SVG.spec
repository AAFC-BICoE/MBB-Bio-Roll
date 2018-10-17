#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-SVG
#    Version:           2.84
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only SVG
#

Name:           opt-perl-SVG
Version:        2.84
Release:        1%{?dist}
Summary:        Perl extension for generating Scalable Vector Graphics (SVG) documents.
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/SVG/
BuildRoot:      /tmp/cpantorpm/SVG-2.84-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/M/MA/MANWAR/SVG-2.84.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(SVG) = 2.84
Provides:       opt-perl(SVG::DOM) = 2.84
Provides:       opt-perl(SVG::Element) = 2.84
Provides:       opt-perl(SVG::Extension) = 2.84
Provides:       opt-perl(SVG::XML) = 2.84
Requires:       opt-perl
Requires:       opt-perl(Exporter)
Requires:       opt-perl(Scalar::Util)
Requires:       opt-perl(constant)
Requires:       opt-perl(parent)
Requires:       opt-perl(strict)
Requires:       opt-perl(vars)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Exporter)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(File::Spec)
BuildRequires:  opt-perl(Scalar::Util)
BuildRequires:  opt-perl(constant)
BuildRequires:  opt-perl(parent)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(vars)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
SVG is a 100% Perl module which generates a nested data structure
containing the DOM representation of an SVG (Scalable Vector Graphics)
image. Using SVG, you can generate SVG objects, embed other SVG instances
into it, access the DOM object, create and access javascript, and generate
SMIL animation content.

%prep

%setup  -n SVG-2.84
chmod -R u+w %{_builddir}/SVG-%{version}

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
* Thu Oct 04 2018 Rocks 2.84-1
- Generated using cpantorpm

