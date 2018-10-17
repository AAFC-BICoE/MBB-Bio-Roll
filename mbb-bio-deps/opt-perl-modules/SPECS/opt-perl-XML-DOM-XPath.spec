#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-XML-DOM-XPath
#    Version:           0.14
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --NO-TESTS --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only XML\:\:DOM\:\:XPath
#

Name:           opt-perl-XML-DOM-XPath
Version:        0.14
Release:        1%{?dist}
Summary:        Perl extension to add XPath support to XML::DOM, using XML::XPath engine
License:        Unknown license: unknown
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML-DOM-XPath/
BuildRoot:      /tmp/cpantorpm/XML-DOM-XPath-0.14-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/M/MI/MIROD/XML-DOM-XPath-0.14.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(XML::DOM::Attr) = 0.14
Provides:       opt-perl(XML::DOM::Comment) = 0.14
Provides:       opt-perl(XML::DOM::Document) = 0.14
Provides:       opt-perl(XML::DOM::Element) = 0.14
Provides:       opt-perl(XML::DOM::Namespace) = 0.14
Provides:       opt-perl(XML::DOM::Node) = 0.14
Provides:       opt-perl(XML::DOM::ProcessingInstruction) = 0.14
Provides:       opt-perl(XML::DOM::Text) = 0.14
Provides:       opt-perl(XML::DOM::XPath) = 0.14
Requires:       opt-perl
Requires:       opt-perl(XML::DOM)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(XML::DOM)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
XML::DOM::XPath allows you to use XML::XPath methods to query a DOM. This
is often much easier than relying only on getElementsByTagName.

%prep

%setup  -n XML-DOM-XPath-0.14
chmod -R u+w %{_builddir}/XML-DOM-XPath-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS" INSTALLDIRS=site SITEPREFIX=/opt/perl INSTALLSITEARCH=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi INSTALLSITELIB=/opt/perl/lib/site_perl/5.26.0 INSTALLSITEBIN=/opt/perl/bin INSTALLSITESCRIPT=/opt/perl/bin INSTALLSITEMAN1DIR=/opt/perl/man/man1 INSTALLSITEMAN3DIR=/opt/perl/man/man3 INSTALLSCRIPT=/opt/perl/bin
make %{?_smp_mflags}


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
* Thu Oct 04 2018 Rocks 0.14-1
- Generated using cpantorpm

