#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-XML-LibXML
#    Version:           2.0132
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only XML\:\:LibXML
#

Name:           opt-perl-XML-LibXML
Version:        2.0132
Release:        1%{?dist}
Summary:        Interface to Gnome libxml2 xml parsing and DOM library
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML-LibXML/
BuildRoot:      /tmp/cpantorpm/XML-LibXML-2.0132-inst
BuildArch:      %{_arch}
Source0:        http://search.cpan.org/authors/id/authors/id/S/SH/SHLOMIF/XML-LibXML-2.0132.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(XML::LibXML) = 2.0132
Provides:       opt-perl(XML::LibXML::Attr) = 2.0132
Provides:       opt-perl(XML::LibXML::AttributeHash) = 2.0132
Provides:       opt-perl(XML::LibXML::Boolean) = 2.0132
Provides:       opt-perl(XML::LibXML::CDATASection) = 2.0132
Provides:       opt-perl(XML::LibXML::Comment) = 2.0132
Provides:       opt-perl(XML::LibXML::Common) = 2.0132
Provides:       opt-perl(XML::LibXML::Devel) = 2.0132
Provides:       opt-perl(XML::LibXML::Document) = 2.0132
Provides:       opt-perl(XML::LibXML::DocumentFragment) = 2.0132
Provides:       opt-perl(XML::LibXML::Dtd) = 2.0132
Provides:       opt-perl(XML::LibXML::Element) = 2.0132
Provides:       opt-perl(XML::LibXML::ErrNo) = 2.0132
Provides:       opt-perl(XML::LibXML::Error) = 2.0132
Provides:       opt-perl(XML::LibXML::InputCallback) = 2.0132
Provides:       opt-perl(XML::LibXML::Literal) = 2.0132
Provides:       opt-perl(XML::LibXML::NamedNodeMap) = 2.0132
Provides:       opt-perl(XML::LibXML::Namespace) = 2.0132
Provides:       opt-perl(XML::LibXML::Node) = 2.0132
Provides:       opt-perl(XML::LibXML::NodeList) = 2.0132
Provides:       opt-perl(XML::LibXML::Number) = 2.0132
Provides:       opt-perl(XML::LibXML::PI) = 2.0132
Provides:       opt-perl(XML::LibXML::Pattern) = 2.0132
Provides:       opt-perl(XML::LibXML::Reader) = 2.0132
Provides:       opt-perl(XML::LibXML::RegExp) = 2.0132
Provides:       opt-perl(XML::LibXML::RelaxNG) = 2.0132
Provides:       opt-perl(XML::LibXML::SAX) = 2.0132
Provides:       opt-perl(XML::LibXML::SAX::AttributeNode) = 2.0132
Provides:       opt-perl(XML::LibXML::SAX::Builder) = 2.0132
Provides:       opt-perl(XML::LibXML::SAX::Generator) = 2.0132
Provides:       opt-perl(XML::LibXML::SAX::Parser) = 2.0132
Provides:       opt-perl(XML::LibXML::Schema) = 2.0132
Provides:       opt-perl(XML::LibXML::Text) = 2.0132
Provides:       opt-perl(XML::LibXML::XPathContext) = 2.0132
Provides:       opt-perl(XML::LibXML::XPathExpression) = 2.0132
Provides:       opt-perl(XML::LibXML::_SAXParser) = 2.0132
Requires:       opt-perl
Requires:       opt-perl(Test::More)
Requires:       opt-perl(XML::SAX::Base)
Requires:       opt-perl(XML::SAX::Exception)
Requires:       opt-perl(base)
Requires:       opt-perl(parent)
Requires:       opt-perl(strict)
Requires:       opt-perl(vars)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(Test::More)
BuildRequires:  opt-perl(XML::SAX::Base)
BuildRequires:  opt-perl(XML::SAX::Exception)
BuildRequires:  opt-perl(base)
BuildRequires:  opt-perl(parent)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(vars)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A perl module

%prep

%setup  -n XML-LibXML-2.0132
chmod -R u+w %{_builddir}/XML-LibXML-%{version}

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
* Thu Oct 04 2018 Rocks 2.0132-1
- Generated using cpantorpm

