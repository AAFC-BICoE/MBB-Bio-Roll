#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Curses-UI
#    Version:           0.9609
#    cpantorpm version: 1.08
#    Date:              Wed Oct 17 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Curses\:\:UI
#

Name:           opt-perl-Curses-UI
Version:        0.9609
Release:        1%{?dist}
Summary:        A curses based OO user interface framework
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Curses-UI/
BuildRoot:      /tmp/cpantorpm/Curses-UI-0.9609-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/M/MD/MDXI/Curses-UI-0.9609.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Curses::UI) = 0.9609
Provides:       opt-perl(Curses::UI::Buttonbox) = 1.10
Provides:       opt-perl(Curses::UI::Calendar) = 1.10
Provides:       opt-perl(Curses::UI::Checkbox) = 1.11
Provides:       opt-perl(Curses::UI::Color) = 0.01
Provides:       opt-perl(Curses::UI::Common) = 1.10
Provides:       opt-perl(Curses::UI::Container) = 1.11
Provides:       opt-perl(Curses::UI::ContainerWidget) = 1.10
Provides:       opt-perl(Curses::UI::Dialog::Basic) = 1.10
Provides:       opt-perl(Curses::UI::Dialog::Calendar) = 1.10
Provides:       opt-perl(Curses::UI::Dialog::Dirbrowser) = 1.0
Provides:       opt-perl(Curses::UI::Dialog::Error) = 1.10
Provides:       opt-perl(Curses::UI::Dialog::Filebrowser) = 1.10
Provides:       opt-perl(Curses::UI::Dialog::Progress) = 1.10
Provides:       opt-perl(Curses::UI::Dialog::Question) = 1.00
Provides:       opt-perl(Curses::UI::Dialog::Status) = 1.10
Provides:       opt-perl(Curses::UI::Label) = 1.11
Provides:       opt-perl(Curses::UI::Language) = 0.9609
Provides:       opt-perl(Curses::UI::Language::chinese) = 0.9609
Provides:       opt-perl(Curses::UI::Language::czech) = 0.9609
Provides:       opt-perl(Curses::UI::Language::dutch) = 0.9609
Provides:       opt-perl(Curses::UI::Language::english) = 0.9609
Provides:       opt-perl(Curses::UI::Language::french) = 0.9609
Provides:       opt-perl(Curses::UI::Language::german) = 0.9609
Provides:       opt-perl(Curses::UI::Language::italian) = 0.9609
Provides:       opt-perl(Curses::UI::Language::japanese) = 0.9609
Provides:       opt-perl(Curses::UI::Language::norwegian) = 0.9609
Provides:       opt-perl(Curses::UI::Language::polish) = 0.9609
Provides:       opt-perl(Curses::UI::Language::portuguese) = 0.9609
Provides:       opt-perl(Curses::UI::Language::russian) = 0.9609
Provides:       opt-perl(Curses::UI::Language::slovak) = 0.9609
Provides:       opt-perl(Curses::UI::Language::spanish) = 0.9609
Provides:       opt-perl(Curses::UI::Language::turkish) = 0.9609
Provides:       opt-perl(Curses::UI::Listbox) = 1.3
Provides:       opt-perl(Curses::UI::MenuListbox) = 1.10
Provides:       opt-perl(Curses::UI::Menubar) = 1.10
Provides:       opt-perl(Curses::UI::Notebook) = 1.0001
Provides:       opt-perl(Curses::UI::PasswordEntry) = 1.10
Provides:       opt-perl(Curses::UI::Popupmenu) = 1.10
Provides:       opt-perl(Curses::UI::PopupmenuListbox) = 1.0011
Provides:       opt-perl(Curses::UI::Progressbar) = 1.10
Provides:       opt-perl(Curses::UI::Radiobuttonbox) = 1.10
Provides:       opt-perl(Curses::UI::SearchEntry) = 1.10
Provides:       opt-perl(Curses::UI::Searchable) = 1.10
Provides:       opt-perl(Curses::UI::TextEditor) = 1.5
Provides:       opt-perl(Curses::UI::TextEntry) = 1.10
Provides:       opt-perl(Curses::UI::TextViewer) = 1.10
Provides:       opt-perl(Curses::UI::Widget) = 1.12
Provides:       opt-perl(Curses::UI::Window) = 1.10
Requires:       opt-perl
Requires:       opt-perl(Curses)
Requires:       opt-perl(Term::ReadKey)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Curses)
BuildRequires:  opt-perl(Term::ReadKey)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Curses::UI is an object-oriented user interface framework for Perl.

%prep

%setup  -n Curses-UI-0.9609
chmod -R u+w %{_builddir}/Curses-UI-%{version}

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
* Wed Oct 17 2018 Rocks 0.9609-1
- Generated using cpantorpm

