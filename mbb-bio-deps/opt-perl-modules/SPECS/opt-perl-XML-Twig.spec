#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-XML-Twig
#    Version:           3.52
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only XML\:\:Twig
#

Name:           opt-perl-XML-Twig
Version:        3.52
Release:        1%{?dist}
Summary:        XML, The Perl Way
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML-Twig/
BuildRoot:      /tmp/cpantorpm/XML-Twig-3.52-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/M/MI/MIROD/XML-Twig-3.52.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(XML::Twig) = 3.52
Provides:       opt-perl(XML::Twig::Elt) = 3.52
Provides:       opt-perl(XML::Twig::Entity) = 3.52
Provides:       opt-perl(XML::Twig::Entity_list) = 3.52
Provides:       opt-perl(XML::Twig::Notation) = 3.52
Provides:       opt-perl(XML::Twig::Notation_list) = 3.52
Provides:       opt-perl(XML::Twig::XPath) = 3.52
Provides:       opt-perl(XML::Twig::XPath::Attribute) = 3.52
Provides:       opt-perl(XML::Twig::XPath::Elt) = 3.52
Provides:       opt-perl(XML::Twig::XPath::Namespace) = 3.52
Requires:       opt-perl
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides a way to process XML documents. It is build on top of
XML::Parser.

%prep

%setup  -n XML-Twig-3.52
chmod -R u+w %{_builddir}/XML-Twig-%{version}

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
* Thu Oct 04 2018 Rocks 3.52-1
- Generated using cpantorpm

