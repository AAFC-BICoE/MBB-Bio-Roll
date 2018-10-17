#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Text-NSP
#    Version:           1.31
#    cpantorpm version: 1.08
#    Date:              Tue Oct 16 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Text\:\:NSP
#

Name:           opt-perl-Text-NSP
Version:        1.31
Release:        1%{?dist}
Summary:        Extract collocations and Ngrams from text
License:        OSI-Approved
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Text-NSP/
BuildRoot:      /tmp/cpantorpm/Text-NSP-1.31-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/T/TP/TPEDERSE/Text-NSP-1.31.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Text::NSP) = 1.31
Provides:       opt-perl(Text::NSP::Measures) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::CHI) = 1.03
Provides:       opt-perl(Text::NSP::Measures::2D::CHI::phi) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::CHI::tscore) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::CHI::x2) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::Dice) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::Dice::dice) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::Dice::jaccard) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::Fisher) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::Fisher2) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::Fisher2::left) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::Fisher2::right) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::Fisher2::twotailed) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::Fisher::left) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::Fisher::right) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::Fisher::twotailed) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::MI) = 1.03
Provides:       opt-perl(Text::NSP::Measures::2D::MI::ll) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::MI::pmi) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::MI::ps) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::MI::tmi) = 0.97
Provides:       opt-perl(Text::NSP::Measures::2D::odds) = 0.97
Provides:       opt-perl(Text::NSP::Measures::3D) = 0.97
Provides:       opt-perl(Text::NSP::Measures::3D::MI) = 1.03
Provides:       opt-perl(Text::NSP::Measures::3D::MI::ll) = 0.97
Provides:       opt-perl(Text::NSP::Measures::3D::MI::pmi) = 0.97
Provides:       opt-perl(Text::NSP::Measures::3D::MI::ps) = 0.97
Provides:       opt-perl(Text::NSP::Measures::3D::MI::tmi) = 0.97
Provides:       opt-perl(Text::NSP::Measures::4D) = 0.97
Provides:       opt-perl(Text::NSP::Measures::4D::MI) = 1.03
Provides:       opt-perl(Text::NSP::Measures::4D::MI::ll) = 0.97
Requires:       opt-perl
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Ngram Statistics Package (NSP) is a collection of perl modules that aid
in analyzing Ngrams in text files. We define an Ngram as a sequence of 'n'
tokens that occur within a window of at least 'n' tokens in the text; what
constitutes a "token" can be defined by the user.

%prep

%setup  -n Text-NSP-1.31
chmod -R u+w %{_builddir}/Text-NSP-%{version}

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
* Tue Oct 16 2018 Rocks 1.31-1
- Generated using cpantorpm

