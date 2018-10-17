#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-HTML-Parser
#    Version:           3.72
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only HTML\:\:Parser
#

Name:           opt-perl-HTML-Parser
Version:        3.72
Release:        1%{?dist}
Summary:        HTML parser class
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/HTML-Parser/
BuildRoot:      /tmp/cpantorpm/HTML-Parser-3.72-inst
BuildArch:      %{_arch}
Source0:        http://search.cpan.org/authors/id/authors/id/G/GA/GAAS/HTML-Parser-3.72.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(HTML::Entities) = 3.69
Provides:       opt-perl(HTML::Filter) = 3.72
Provides:       opt-perl(HTML::HeadParser) = 3.71
Provides:       opt-perl(HTML::LinkExtor) = 3.69
Provides:       opt-perl(HTML::Parser) = 3.72
Provides:       opt-perl(HTML::PullParser) = 3.57
Provides:       opt-perl(HTML::TokeParser) = 3.69
Requires:       opt-perl
Requires:       opt-perl(XSLoader)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(Test::More)
BuildRequires:  opt-perl(XSLoader)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Objects of the HTML::Parser class will recognize markup and separate it
from plain text (alias data content) in HTML documents. As different kinds
of markup and text are recognized, the corresponding event handlers are
invoked.

%prep

%setup  -n HTML-Parser-3.72
chmod -R u+w %{_builddir}/HTML-Parser-%{version}

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
* Thu Oct 04 2018 Rocks 3.72-1
- Generated using cpantorpm

