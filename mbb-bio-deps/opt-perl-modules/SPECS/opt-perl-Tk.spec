#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Tk
#    Version:           804.034
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Tk
#

Name:           opt-perl-Tk
Version:        804.034
Release:        1%{?dist}
Summary:        Tk - a Graphical User Interface Toolkit
License:        Distributable
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Tk/
BuildRoot:      /tmp/cpantorpm/Tk-804.034-inst
BuildArch:      %{_arch}
Source0:        http://search.cpan.org/authors/id/authors/id/S/SR/SREZIC/Tk-804.034.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Tie::Watch) = 804.034
Provides:       opt-perl(Tk) = 804.034
Provides:       opt-perl(Tk::Adjuster) = 4.008
Provides:       opt-perl(Tk::After) = 4.008
Provides:       opt-perl(Tk::Animation) = 4.008
Provides:       opt-perl(Tk::Balloon) = 4.012
Provides:       opt-perl(Tk::Bitmap) = 4.004
Provides:       opt-perl(Tk::BrowseEntry) = 4.015
Provides:       opt-perl(Tk::Button) = 4.010
Provides:       opt-perl(Tk::Canvas) = 4.013
Provides:       opt-perl(Tk::Checkbutton) = 4.006
Provides:       opt-perl(Tk::Clipboard) = 4.009
Provides:       opt-perl(Tk::CmdLine) = 4.007
Provides:       opt-perl(Tk::ColorDialog) = 4.014
Provides:       opt-perl(Tk::ColorEditor) = 4.014
Provides:       opt-perl(Tk::ColorSelect) = 4.014
Provides:       opt-perl(Tk::Compound) = 4.004
Provides:       opt-perl(Tk::Config) = 804.034
Provides:       opt-perl(Tk::Configure) = 4.009
Provides:       opt-perl(Tk::Derived) = 4.011
Provides:       opt-perl(Tk::Dialog) = 4.005
Provides:       opt-perl(Tk::DialogBox) = 4.016
Provides:       opt-perl(Tk::DirTree) = 4.022
Provides:       opt-perl(Tk::DirTreeDialog) = 804.034
Provides:       opt-perl(Tk::Dirlist) = 4.004
Provides:       opt-perl(Tk::DragDrop) = 4.015
Provides:       opt-perl(Tk::DragDrop::Common) = 4.005
Provides:       opt-perl(Tk::DragDrop::Local) = 4.004
Provides:       opt-perl(Tk::DragDrop::Rect) = 4.012
Provides:       opt-perl(Tk::DragDrop::SunConst) = 4.004
Provides:       opt-perl(Tk::DragDrop::SunDrop) = 4.006
Provides:       opt-perl(Tk::DragDrop::SunSite) = 4.007
Provides:       opt-perl(Tk::DragDrop::XDNDDrop) = 4.007
Provides:       opt-perl(Tk::DragDrop::XDNDSite) = 4.007
Provides:       opt-perl(Tk::DropSite) = 4.008
Provides:       opt-perl(Tk::DummyEncode) = 4.007
Provides:       opt-perl(Tk::DummyEncode::X11ControlChars) = 804.034
Provides:       opt-perl(Tk::DummyEncode::iso8859_1) = 804.034
Provides:       opt-perl(Tk::English) = 4.006
Provides:       opt-perl(Tk::Entry) = 4.018
Provides:       opt-perl(Tk::ErrorDialog) = 4.008
Provides:       opt-perl(Tk::Event) = 4.035
Provides:       opt-perl(Tk::Event::IO) = 4.009
Provides:       opt-perl(Tk::FBox) = 4.021
Provides:       opt-perl(Tk::FileSelect) = 4.018
Provides:       opt-perl(Tk::FloatEntry) = 4.004
Provides:       opt-perl(Tk::Font) = 4.004
Provides:       opt-perl(Tk::Frame) = 4.010
Provides:       opt-perl(Tk::HList) = 4.015
Provides:       opt-perl(Tk::IO) = 4.006
Provides:       opt-perl(Tk::IconList) = 4.007
Provides:       opt-perl(Tk::Image) = 4.011
Provides:       opt-perl(Tk::InputO) = 4.004
Provides:       opt-perl(Tk::ItemStyle) = 4.004
Provides:       opt-perl(Tk::JPEG) = 4.003
Provides:       opt-perl(Tk::LabEntry) = 4.006
Provides:       opt-perl(Tk::LabFrame) = 4.010
Provides:       opt-perl(Tk::LabRadiobutton) = 4.004
Provides:       opt-perl(Tk::Label) = 4.006
Provides:       opt-perl(Tk::LabeledEntryLabeledRadiobutton) = 4.004
Provides:       opt-perl(Tk::Labelframe) = 4.003
Provides:       opt-perl(Tk::Listbox) = 4.015
Provides:       opt-perl(Tk::MMtry) = 4.011
Provides:       opt-perl(Tk::MMutil) = 4.026
Provides:       opt-perl(Tk::MainWindow) = 4.015
Provides:       opt-perl(Tk::MakeDepend) = 4.015
Provides:       opt-perl(Tk::Menu) = 4.023
Provides:       opt-perl(Tk::Menu::Button) = 804.034
Provides:       opt-perl(Tk::Menu::Cascade) = 804.034
Provides:       opt-perl(Tk::Menu::Checkbutton) = 804.034
Provides:       opt-perl(Tk::Menu::Item) = 4.005
Provides:       opt-perl(Tk::Menu::Radiobutton) = 804.034
Provides:       opt-perl(Tk::Menu::Separator) = 804.034
Provides:       opt-perl(Tk::Menubar) = 4.006
Provides:       opt-perl(Tk::Menubutton) = 4.005
Provides:       opt-perl(Tk::Message) = 4.006
Provides:       opt-perl(Tk::MsgBox) = 4.002
Provides:       opt-perl(Tk::Mwm) = 4.004
Provides:       opt-perl(Tk::NBFrame) = 4.004
Provides:       opt-perl(Tk::NoteBook) = 4.012
Provides:       opt-perl(Tk::Optionmenu) = 4.014
Provides:       opt-perl(Tk::PNG) = 4.004
Provides:       opt-perl(Tk::Pane) = 4.007
Provides:       opt-perl(Tk::Panedwindow) = 4.004
Provides:       opt-perl(Tk::Photo) = 4.006
Provides:       opt-perl(Tk::Pixmap) = 4.004
Provides:       opt-perl(Tk::Pretty) = 4.006
Provides:       opt-perl(Tk::ProgressBar) = 4.015
Provides:       opt-perl(Tk::ROText) = 4.011
Provides:       opt-perl(Tk::Radiobutton) = 4.006
Provides:       opt-perl(Tk::Region) = 4.006
Provides:       opt-perl(Tk::Reindex) = 4.006
Provides:       opt-perl(Tk::ReindexedROText) = 4.004
Provides:       opt-perl(Tk::ReindexedText) = 4.004
Provides:       opt-perl(Tk::Scale) = 4.004
Provides:       opt-perl(Tk::Scrollbar) = 4.010
Provides:       opt-perl(Tk::Spinbox) = 4.007
Provides:       opt-perl(Tk::Stats) = 4.004
Provides:       opt-perl(Tk::Submethods) = 4.005
Provides:       opt-perl(Tk::TList) = 4.006
Provides:       opt-perl(Tk::Table) = 4.016
Provides:       opt-perl(Tk::Text) = 4.030
Provides:       opt-perl(Tk::Text::Tag) = 4.004
Provides:       opt-perl(Tk::TextEdit) = 4.004
Provides:       opt-perl(Tk::TextList) = 4.006
Provides:       opt-perl(Tk::TextUndo) = 4.015
Provides:       opt-perl(Tk::Tiler) = 4.013
Provides:       opt-perl(Tk::TixGrid) = 4.010
Provides:       opt-perl(Tk::Toplevel) = 4.006
Provides:       opt-perl(Tk::Trace) = 4.009
Provides:       opt-perl(Tk::Tree) = 4.72
Provides:       opt-perl(Tk::Widget) = 4.036
Provides:       opt-perl(Tk::WinPhoto) = 4.005
Provides:       opt-perl(Tk::Wm) = 4.015
Provides:       opt-perl(Tk::X) = 4.005
Provides:       opt-perl(Tk::X11Font) = 4.007
Provides:       opt-perl(Tk::Xlib) = 4.004
Provides:       opt-perl(Tk::Xrm) = 4.005
Provides:       opt-perl(Tk::install) = 4.004
Provides:       opt-perl(Tk::widgets) = 4.005
Provides:       opt-perl(WidgetDemo) = 4.012
Requires:       opt-perl
Requires:       opt-perl(Encode)
Requires:       opt-perl(Test::More)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Encode)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(Test::More)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A perl module

%prep

%setup  -n Tk-804.034
chmod -R u+w %{_builddir}/Tk-%{version}

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
/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi/*
/opt/perl/man/man1/*
/opt/perl/man/man3/*

%changelog
* Thu Oct 04 2018 Rocks 804.034-1
- Generated using cpantorpm

