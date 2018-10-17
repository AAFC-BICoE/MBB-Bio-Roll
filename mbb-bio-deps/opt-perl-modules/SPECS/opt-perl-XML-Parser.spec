#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-XML-Parser
#    Version:           2.44
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only XML\:\:Parser
#

Name:           opt-perl-XML-Parser
Version:        2.44
Release:        1%{?dist}
Summary:        A perl module for parsing XML documents
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML-Parser/
BuildRoot:      /tmp/cpantorpm/XML-Parser-2.44-inst
BuildArch:      %{_arch}
Source0:        http://search.cpan.org/authors/id/authors/id/T/TO/TODDR/XML-Parser-2.44.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(XML::Parser) = 2.44
Provides:       opt-perl(XML::Parser::Expat) = 2.44
Provides:       opt-perl(XML::Parser::Style::Debug) = 2.44
Provides:       opt-perl(XML::Parser::Style::Objects) = 2.44
Provides:       opt-perl(XML::Parser::Style::Stream) = 2.44
Provides:       opt-perl(XML::Parser::Style::Subs) = 2.44
Provides:       opt-perl(XML::Parser::Style::Tree) = 2.44
Requires:       opt-perl
Requires:       opt-perl(LWP::UserAgent)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(LWP::UserAgent)
BuildRequires:  opt-perl(Test::More)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides ways to parse XML documents. It is built on top of
L<XML::Parser::Expat>, which is a lower level interface to James Clark's
expat library. Each call to one of the parsing methods creates a new
instance of XML::Parser::Expat which is then used to parse the document.
Expat options may be provided when the XML::Parser object is created. These
options are then passed on to the Expat object on each parse call. They can
also be given as extra arguments to the parse methods, in which case they
override options given at XML::Parser creation time.

%prep

%setup  -n XML-Parser-2.44
chmod -R u+w %{_builddir}/XML-Parser-%{version}

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
/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi/*
/opt/perl/man/man3/*

%changelog
* Thu Oct 04 2018 Rocks 2.44-1
- Generated using cpantorpm

