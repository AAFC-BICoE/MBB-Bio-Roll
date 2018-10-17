#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-XML-DOM
#    Version:           1.46
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only XML\:\:DOM
#

Name:           opt-perl-XML-DOM
Version:        1.46
Release:        1%{?dist}
Summary:        unknown
License:        Unknown license: unknown
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML-DOM/
BuildRoot:      /tmp/cpantorpm/XML-DOM-1.46-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/T/TJ/TJMATHER/XML-DOM-1.46.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(XML::DOM) = 1.46
Provides:       opt-perl(XML::DOM::AttDef) = 1.46
Provides:       opt-perl(XML::DOM::AttlistDecl) = 1.46
Provides:       opt-perl(XML::DOM::Attr) = 1.46
Provides:       opt-perl(XML::DOM::CDATASection) = 1.46
Provides:       opt-perl(XML::DOM::CharacterData) = 1.46
Provides:       opt-perl(XML::DOM::Comment) = 1.46
Provides:       opt-perl(XML::DOM::DOMException) = 1.46
Provides:       opt-perl(XML::DOM::DOMImplementation) = 1.46
Provides:       opt-perl(XML::DOM::Document) = 1.46
Provides:       opt-perl(XML::DOM::DocumentFragment) = 1.46
Provides:       opt-perl(XML::DOM::DocumentType) = 1.46
Provides:       opt-perl(XML::DOM::Element) = 1.46
Provides:       opt-perl(XML::DOM::ElementDecl) = 1.46
Provides:       opt-perl(XML::DOM::Entity) = 1.46
Provides:       opt-perl(XML::DOM::EntityReference) = 1.46
Provides:       opt-perl(XML::DOM::NamedNodeMap) = 1.46
Provides:       opt-perl(XML::DOM::Node) = 1.46
Provides:       opt-perl(XML::DOM::NodeList) = 1.46
Provides:       opt-perl(XML::DOM::Notation) = 1.46
Provides:       opt-perl(XML::DOM::Parser) = 1.46
Provides:       opt-perl(XML::DOM::PerlSAX) = 1.46
Provides:       opt-perl(XML::DOM::PrintToFileHandle) = 1.46
Provides:       opt-perl(XML::DOM::PrintToString) = 1.46
Provides:       opt-perl(XML::DOM::ProcessingInstruction) = 1.46
Provides:       opt-perl(XML::DOM::Text) = 1.46
Provides:       opt-perl(XML::DOM::XMLDecl) = 1.46
Provides:       opt-perl(XML::Handler::BuildDOM) = 1.46
Provides:       opt-perl(XML::Parser::Dom) = 1.46
Provides:       opt-perl(XML::XQL::Node) = 1.46
Requires:       opt-perl
Requires:       opt-perl(LWP::UserAgent)
Requires:       opt-perl(XML::RegExp)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(LWP::UserAgent)
BuildRequires:  opt-perl(XML::RegExp)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module extends the XML::Parser module by Clark Cooper. The XML::Parser
module is built on top of XML::Parser::Expat, which is a lower level
interface to James Clark's expat library.

%prep

%setup  -n XML-DOM-1.46
chmod -R u+w %{_builddir}/XML-DOM-%{version}

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
* Thu Oct 04 2018 Rocks 1.46-1
- Generated using cpantorpm

