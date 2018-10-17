#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-SVG-Graph
#    Version:           0.02
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only SVG\:\:Graph
#

Name:           opt-perl-SVG-Graph
Version:        0.02
Release:        1%{?dist}
Summary:        unknown
License:        Unknown license: unknown
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/SVG-Graph/
BuildRoot:      /tmp/cpantorpm/SVG-Graph-0.02-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/A/AL/ALLENDAY/SVG-Graph-0.02.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(SVG::Graph) = 0.02
Provides:       opt-perl(SVG::Graph::Data) = 0.02
Provides:       opt-perl(SVG::Graph::Data::Datum) = 0.02
Provides:       opt-perl(SVG::Graph::Data::Node) = 0.02
Provides:       opt-perl(SVG::Graph::Data::Tree) = 0.02
Provides:       opt-perl(SVG::Graph::File) = 0.02
Provides:       opt-perl(SVG::Graph::Frame) = 0.02
Provides:       opt-perl(SVG::Graph::Glyph) = 0.02
Provides:       opt-perl(SVG::Graph::Glyph::axis) = 0.02
Provides:       opt-perl(SVG::Graph::Glyph::bar) = 0.02
Provides:       opt-perl(SVG::Graph::Glyph::barflex) = 0.02
Provides:       opt-perl(SVG::Graph::Glyph::bezier) = 0.02
Provides:       opt-perl(SVG::Graph::Glyph::bubble) = 0.02
Provides:       opt-perl(SVG::Graph::Glyph::heatmap) = 0.02
Provides:       opt-perl(SVG::Graph::Glyph::line) = 0.02
Provides:       opt-perl(SVG::Graph::Glyph::pictogram) = 0.02
Provides:       opt-perl(SVG::Graph::Glyph::scatter) = 0.02
Provides:       opt-perl(SVG::Graph::Glyph::tree) = 0.02
Provides:       opt-perl(SVG::Graph::Glyph::wedge) = 0.02
Provides:       opt-perl(SVG::Graph::Group) = 0.02
Requires:       opt-perl
Requires:       opt-perl(Math::Derivative)
Requires:       opt-perl(Math::Spline)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(Math::Derivative)
BuildRequires:  opt-perl(Math::Spline)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
SVG::Graph is a suite of perl modules for plotting data. SVG::Graph
currently supports plots of one-, two- and three-dimensional data, as well
as N-ary rooted trees. Data may be represented as:

%prep

%setup  -n SVG-Graph-0.02
chmod -R u+w %{_builddir}/SVG-Graph-%{version}

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
* Thu Oct 04 2018 Rocks 0.02-1
- Generated using cpantorpm

