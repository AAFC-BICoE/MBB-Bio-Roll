#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Mail-Sender
#    Version:           0.903
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Mail\:\:Sender
#

Name:           opt-perl-Mail-Sender
Version:        0.903
Release:        1%{?dist}
Summary:        (DEPRECATED) module for sending mails with attachments through an SMTP server
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Mail-Sender/
BuildRoot:      /tmp/cpantorpm/Mail-Sender-0.903-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/C/CA/CAPOEIRAB/Mail-Sender-0.903.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Mail::Sender) = 0.903
Provides:       opt-perl(Mail::Sender::CType::Ext) = 0.903
Provides:       opt-perl(Mail::Sender::CType::Win32) = 0.903
Provides:       opt-perl(Mail::Sender::DBIO) = 0.903
Provides:       opt-perl(Mail::Sender::IO) = 0.903
Requires:       opt-perl
Requires:       opt-perl(Carp)
Requires:       opt-perl(Encode)
Requires:       opt-perl(Exporter)
Requires:       opt-perl(File::Basename)
Requires:       opt-perl(IO::Handle)
Requires:       opt-perl(IO::Socket::INET)
Requires:       opt-perl(MIME::Base64)
Requires:       opt-perl(MIME::QuotedPrint)
Requires:       opt-perl(Socket)
Requires:       opt-perl(Symbol)
Requires:       opt-perl(Tie::Handle)
Requires:       opt-perl(Time::Local)
Requires:       opt-perl(base)
Requires:       opt-perl(strict)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(Encode)
BuildRequires:  opt-perl(Exporter)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(File::Basename)
BuildRequires:  opt-perl(IO::Handle)
BuildRequires:  opt-perl(IO::Socket::INET)
BuildRequires:  opt-perl(MIME::Base64)
BuildRequires:  opt-perl(MIME::QuotedPrint)
BuildRequires:  opt-perl(Socket)
BuildRequires:  opt-perl(Symbol)
BuildRequires:  opt-perl(Tie::Handle)
BuildRequires:  opt-perl(Time::Local)
BuildRequires:  opt-perl(base)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
L<Mail::Sender> is deprecated. L<Email::Sender> is the go-to choice when
you need to send Email from Perl. Go there, be happy!

%prep

%setup  -n Mail-Sender-0.903
chmod -R u+w %{_builddir}/Mail-Sender-%{version}

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
* Thu Oct 04 2018 Rocks 0.903-1
- Generated using cpantorpm

