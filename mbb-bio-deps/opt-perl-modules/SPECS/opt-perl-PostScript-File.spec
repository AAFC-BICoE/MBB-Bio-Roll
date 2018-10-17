#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-PostScript-File
#    Version:           2.23
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only PostScript\:\:File
#

Name:           opt-perl-PostScript-File
Version:        2.23
Release:        1%{?dist}
Summary:        Class for creating Adobe PostScript files
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/PostScript-File/
BuildRoot:      /tmp/cpantorpm/PostScript-File-2.23-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/C/CJ/CJM/PostScript-File-2.23.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(PostScript::File) = 2.23
Provides:       opt-perl(PostScript::File::Functions) = 2.23
Provides:       opt-perl(PostScript::File::Metrics) = 2.11
Provides:       opt-perl(PostScript::File::Metrics::Loader) = 2.20
Provides:       opt-perl(PostScript::File::Metrics::cp1252::Courier) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::cp1252::Courier::Bold) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::cp1252::Courier::BoldOblique) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::cp1252::Courier::Oblique) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::cp1252::Helvetica) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::cp1252::Helvetica::Bold) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::cp1252::Helvetica::BoldOblique) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::cp1252::Helvetica::Oblique) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::cp1252::Times::Bold) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::cp1252::Times::BoldItalic) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::cp1252::Times::Italic) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::cp1252::Times::Roman) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::iso_8859_1::Courier) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::iso_8859_1::Courier::Bold) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::iso_8859_1::Courier::BoldOblique) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::iso_8859_1::Courier::Oblique) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::iso_8859_1::Helvetica) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::iso_8859_1::Helvetica::Bold) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::iso_8859_1::Helvetica::BoldOblique) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::iso_8859_1::Helvetica::Oblique) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::iso_8859_1::Times::Bold) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::iso_8859_1::Times::BoldItalic) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::iso_8859_1::Times::Italic) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::iso_8859_1::Times::Roman) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::std::Courier) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::std::Courier::Bold) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::std::Courier::BoldOblique) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::std::Courier::Oblique) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::std::Helvetica) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::std::Helvetica::Bold) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::std::Helvetica::BoldOblique) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::std::Helvetica::Oblique) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::std::Times::Bold) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::std::Times::BoldItalic) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::std::Times::Italic) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::std::Times::Roman) = 2.01
Provides:       opt-perl(PostScript::File::Metrics::sym::Symbol) = 2.01
Requires:       opt-perl
Requires:       opt-perl(Carp)
Requires:       opt-perl(File::Spec)
Requires:       opt-perl(Scalar::Util)
Requires:       opt-perl(Sys::Hostname)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(File::Spec)
BuildRequires:  opt-perl(Scalar::Util)
BuildRequires:  opt-perl(Sys::Hostname)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
PostScript::File is a class that writes PostScript files following Adobe's
Document Structuring Conventions (DSC). You should be familiar with the DSC
if you're using this class directly; consult the PostScript Language
Document Structuring Conventions Specification linked to in L</"SEE
ALSO">.

%prep

%setup  -n PostScript-File-2.23
chmod -R u+w %{_builddir}/PostScript-File-%{version}

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
* Thu Oct 04 2018 Rocks 2.23-1
- Generated using cpantorpm

