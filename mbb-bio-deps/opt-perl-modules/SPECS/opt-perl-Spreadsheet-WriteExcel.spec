#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Spreadsheet-WriteExcel
#    Version:           2.40
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Spreadsheet\:\:WriteExcel
#

Name:           opt-perl-Spreadsheet-WriteExcel
Version:        2.40
Release:        1%{?dist}
Summary:        Write to a cross platform Excel binary file
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Spreadsheet-WriteExcel/
BuildRoot:      /tmp/cpantorpm/Spreadsheet-WriteExcel-2.40-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/J/JM/JMCNAMARA/Spreadsheet-WriteExcel-2.40.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Spreadsheet::WriteExcel) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::BIFFwriter) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Big) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Chart) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Chart::Area) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Chart::Bar) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Chart::Column) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Chart::External) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Chart::Line) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Chart::Pie) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Chart::Scatter) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Chart::Stock) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Examples) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Format) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Formula) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::OLEwriter) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Properties) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Utility) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Workbook) = 2.40
Provides:       opt-perl(Spreadsheet::WriteExcel::Worksheet) = 2.40
Requires:       opt-perl
Requires:       opt-perl(File::Temp)
Requires:       opt-perl(Parse::RecDescent)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(File::Temp)
BuildRequires:  opt-perl(Parse::RecDescent)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Spreadsheet::WriteExcel Perl module can be used to create a
cross-platform Excel binary file. Multiple worksheets can be added to a
workbook and formatting can be applied to cells. Text, numbers, formulas,
hyperlinks, images and charts can be written to the cells.

%prep

%setup  -n Spreadsheet-WriteExcel-2.40
chmod -R u+w %{_builddir}/Spreadsheet-WriteExcel-%{version}

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
* Thu Oct 04 2018 Rocks 2.40-1
- Generated using cpantorpm

