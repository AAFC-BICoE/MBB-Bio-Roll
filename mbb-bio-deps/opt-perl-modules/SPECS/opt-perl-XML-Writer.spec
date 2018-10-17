#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-XML-Writer
#    Version:           0.625
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only XML\:\:Writer
#

Name:           opt-perl-XML-Writer
Version:        0.625
Release:        1%{?dist}
Summary:        Easily generate well-formed, namespace-aware XML.
License:        Distributable
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML-Writer/
BuildRoot:      /tmp/cpantorpm/XML-Writer-0.625-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/J/JO/JOSEPHW/XML-Writer-0.625.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(XML::Writer) = 0.625
Provides:       opt-perl(XML::Writer::Namespaces) = 0.625
Provides:       opt-perl(XML::Writer::_PrintChecker) = 0.625
Provides:       opt-perl(XML::Writer::_String) = 0.625
Requires:       opt-perl
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
XML::Writer is a helper module for Perl programs that write an XML
document. The module handles all escaping for attribute values and
character data and constructs different types of markup, such as tags,
comments, and processing instructions.

%prep

%setup  -n XML-Writer-0.625
chmod -R u+w %{_builddir}/XML-Writer-%{version}

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
* Thu Oct 04 2018 Rocks 0.625-1
- Generated using cpantorpm

