#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Font-TTF
#    Version:           1.06
#    cpantorpm version: 1.08
#    Date:              Wed Oct 17 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Font\:\:TTF
#

Name:           opt-perl-Font-TTF
Version:        1.06
Release:        1%{?dist}
Summary:        TTF font support for Perl
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Font-TTF/
BuildRoot:      /tmp/cpantorpm/Font-TTF-1.06-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/B/BH/BHALLISSY/Font-TTF-1.06.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Font::TTF) = 1.06
Provides:       opt-perl(Font::TTF::AATKern) = 1.06
Provides:       opt-perl(Font::TTF::AATutils) = 1.06
Provides:       opt-perl(Font::TTF::Anchor) = 1.06
Provides:       opt-perl(Font::TTF::Bsln) = 1.06
Provides:       opt-perl(Font::TTF::Cmap) = 1.06
Provides:       opt-perl(Font::TTF::Coverage) = 1.06
Provides:       opt-perl(Font::TTF::Cvt_) = 0.0001
Provides:       opt-perl(Font::TTF::DSIG) = 1.06
Provides:       opt-perl(Font::TTF::Delta) = 1.06
Provides:       opt-perl(Font::TTF::Dumper) = 1.06
Provides:       opt-perl(Font::TTF::EBDT) = 1.06
Provides:       opt-perl(Font::TTF::EBLC) = 1.06
Provides:       opt-perl(Font::TTF::Fdsc) = 1.06
Provides:       opt-perl(Font::TTF::Feat) = 1.06
Provides:       opt-perl(Font::TTF::Features::Cvar) = 1.06
Provides:       opt-perl(Font::TTF::Features::Size) = 1.06
Provides:       opt-perl(Font::TTF::Features::Sset) = 1.06
Provides:       opt-perl(Font::TTF::Fmtx) = 1.06
Provides:       opt-perl(Font::TTF::Font) = 0.39
Provides:       opt-perl(Font::TTF::Fpgm) = 0.0001
Provides:       opt-perl(Font::TTF::GDEF) = 1.06
Provides:       opt-perl(Font::TTF::GPOS) = 1.06
Provides:       opt-perl(Font::TTF::GSUB) = 1.06
Provides:       opt-perl(Font::TTF::Glat) = 1.06
Provides:       opt-perl(Font::TTF::Gloc) = 1.06
Provides:       opt-perl(Font::TTF::Glyf) = 1.06
Provides:       opt-perl(Font::TTF::Glyph) = 1.06
Provides:       opt-perl(Font::TTF::GrFeat) = 1.06
Provides:       opt-perl(Font::TTF::Hdmx) = 1.06
Provides:       opt-perl(Font::TTF::Head) = 1.06
Provides:       opt-perl(Font::TTF::Hhea) = 1.06
Provides:       opt-perl(Font::TTF::Hmtx) = 1.06
Provides:       opt-perl(Font::TTF::Kern) = 1.06
Provides:       opt-perl(Font::TTF::Kern::ClassArray) = 1.06
Provides:       opt-perl(Font::TTF::Kern::CompactClassArray) = 1.06
Provides:       opt-perl(Font::TTF::Kern::OrderedList) = 1.06
Provides:       opt-perl(Font::TTF::Kern::StateTable) = 1.06
Provides:       opt-perl(Font::TTF::Kern::Subtable) = 1.06
Provides:       opt-perl(Font::TTF::LTSH) = 1.06
Provides:       opt-perl(Font::TTF::Loca) = 1.06
Provides:       opt-perl(Font::TTF::Maxp) = 1.06
Provides:       opt-perl(Font::TTF::Mort) = 1.06
Provides:       opt-perl(Font::TTF::Mort::Chain) = 1.06
Provides:       opt-perl(Font::TTF::Mort::Contextual) = 1.06
Provides:       opt-perl(Font::TTF::Mort::Insertion) = 1.06
Provides:       opt-perl(Font::TTF::Mort::Ligature) = 1.06
Provides:       opt-perl(Font::TTF::Mort::Noncontextual) = 1.06
Provides:       opt-perl(Font::TTF::Mort::Rearrangement) = 1.06
Provides:       opt-perl(Font::TTF::Mort::Subtable) = 1.06
Provides:       opt-perl(Font::TTF::Name) = 1.1
Provides:       opt-perl(Font::TTF::OS_2) = 1.06
Provides:       opt-perl(Font::TTF::OTTags) = 1.06
Provides:       opt-perl(Font::TTF::OldCmap) = 1.06
Provides:       opt-perl(Font::TTF::OldMort) = 1.06
Provides:       opt-perl(Font::TTF::PCLT) = 1.06
Provides:       opt-perl(Font::TTF::PSNames) = 1.06
Provides:       opt-perl(Font::TTF::Post) = 0.01
Provides:       opt-perl(Font::TTF::Prep) = 0.0001
Provides:       opt-perl(Font::TTF::Prop) = 1.06
Provides:       opt-perl(Font::TTF::Segarr) = 0.0001
Provides:       opt-perl(Font::TTF::Silf) = 1.06
Provides:       opt-perl(Font::TTF::Sill) = 1.06
Provides:       opt-perl(Font::TTF::Table) = 0.0001
Provides:       opt-perl(Font::TTF::Ttc) = 0.0001
Provides:       opt-perl(Font::TTF::Ttopen) = 1.06
Provides:       opt-perl(Font::TTF::Utils) = 0.0001
Provides:       opt-perl(Font::TTF::Vhea) = 1.06
Provides:       opt-perl(Font::TTF::Vmtx) = 1.06
Provides:       opt-perl(Font::TTF::Win32) = 1.06
Provides:       opt-perl(Font::TTF::Woff) = 1.06
Provides:       opt-perl(Font::TTF::Woff::MetaData) = 1.06
Provides:       opt-perl(Font::TTF::Woff::PrivateData) = 1.06
Provides:       opt-perl(Font::TTF::XMLparse) = 1.06
Requires:       opt-perl
Requires:       opt-perl(IO::String)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(IO::String)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module allows you to do almost anything to a TrueType/OpenType Font
including modify and inspect nearly all tables.

%prep

%setup  -n Font-TTF-1.06
chmod -R u+w %{_builddir}/Font-TTF-%{version}

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
* Wed Oct 17 2018 Rocks 1.06-1
- Generated using cpantorpm

