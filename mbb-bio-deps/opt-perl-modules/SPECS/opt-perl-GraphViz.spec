#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-GraphViz
#    Version:           2.24
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only GraphViz
#

Name:           opt-perl-GraphViz
Version:        2.24
Release:        1%{?dist}
Summary:        Interface to AT&T's GraphViz. Deprecated. See GraphViz2
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/GraphViz/
BuildRoot:      /tmp/cpantorpm/GraphViz-2.24-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/R/RS/RSAVAGE/GraphViz-2.24.tgz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(DB) = 2.24
Provides:       opt-perl(Devel::GraphVizProf) = 2.24
Provides:       opt-perl(GraphViz) = 2.24
Provides:       opt-perl(GraphViz::Data::Grapher) = 2.24
Provides:       opt-perl(GraphViz::No) = 2.24
Provides:       opt-perl(GraphViz::Parse::RecDescent) = 2.24
Provides:       opt-perl(GraphViz::Parse::Yacc) = 2.24
Provides:       opt-perl(GraphViz::Parse::Yapp) = 2.24
Provides:       opt-perl(GraphViz::Regex) = 2.24
Provides:       opt-perl(GraphViz::Small) = 2.24
Provides:       opt-perl(GraphViz::XML) = 2.24
Requires:       opt-perl
Requires:       opt-perl(Config)
Requires:       opt-perl(lib)
Requires:       opt-perl(strict)
Requires:       opt-perl(vars)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Config)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(lib)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(vars)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides an interface to layout and image generation of
directed and undirected graphs in a variety of formats (PostScript, PNG,
etc.) using the "dot", "neato", "twopi", "circo" and "fdp" programs from
the Graphviz project (http://www.graphviz.org/ or
http://www.research.att.com/sw/tools/graphviz/).

%prep

%setup  -n GraphViz-2.24
chmod -R u+w %{_builddir}/GraphViz-%{version}

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
* Thu Oct 04 2018 Rocks 2.24-1
- Generated using cpantorpm

