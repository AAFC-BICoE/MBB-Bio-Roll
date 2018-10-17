#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Spreadsheet-ParseExcel
#    Version:           0.65
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Spreadsheet\:\:ParseExcel
#

Name:           opt-perl-Spreadsheet-ParseExcel
Version:        0.65
Release:        1%{?dist}
Summary:        Read information from an Excel file.
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Spreadsheet-ParseExcel/
BuildRoot:      /tmp/cpantorpm/Spreadsheet-ParseExcel-0.65-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/D/DO/DOUGW/Spreadsheet-ParseExcel-0.65.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Spreadsheet::ParseExcel) = 0.65
Provides:       opt-perl(Spreadsheet::ParseExcel::Cell) = 0.65
Provides:       opt-perl(Spreadsheet::ParseExcel::Dump) = 0.65
Provides:       opt-perl(Spreadsheet::ParseExcel::FmtDefault) = 0.65
Provides:       opt-perl(Spreadsheet::ParseExcel::FmtJapan) = 0.65
Provides:       opt-perl(Spreadsheet::ParseExcel::FmtJapan2) = 0.65
Provides:       opt-perl(Spreadsheet::ParseExcel::FmtUnicode) = 0.65
Provides:       opt-perl(Spreadsheet::ParseExcel::Font) = 0.65
Provides:       opt-perl(Spreadsheet::ParseExcel::Format) = 0.65
Provides:       opt-perl(Spreadsheet::ParseExcel::SaveParser) = 0.65
Provides:       opt-perl(Spreadsheet::ParseExcel::SaveParser::Workbook) = 0.65
Provides:       opt-perl(Spreadsheet::ParseExcel::SaveParser::Worksheet) = 0.65
Provides:       opt-perl(Spreadsheet::ParseExcel::Utility) = 0.65
Provides:       opt-perl(Spreadsheet::ParseExcel::Workbook) = 0.65
Provides:       opt-perl(Spreadsheet::ParseExcel::Worksheet) = 0.65
Requires:       opt-perl
Requires:       opt-perl(Crypt::RC4)
Requires:       opt-perl(Digest::Perl::MD5)
Requires:       opt-perl(IO::File)
Requires:       opt-perl(IO::Scalar)
Requires:       opt-perl(Scalar::Util)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Crypt::RC4)
BuildRequires:  opt-perl(Digest::Perl::MD5)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(IO::File)
BuildRequires:  opt-perl(IO::Scalar)
BuildRequires:  opt-perl(Scalar::Util)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Spreadsheet::ParseExcel module can be used to read information from
Excel 95-2003 binary files.

%prep

%setup  -n Spreadsheet-ParseExcel-0.65
chmod -R u+w %{_builddir}/Spreadsheet-ParseExcel-%{version}

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
* Thu Oct 04 2018 Rocks 0.65-1
- Generated using cpantorpm

