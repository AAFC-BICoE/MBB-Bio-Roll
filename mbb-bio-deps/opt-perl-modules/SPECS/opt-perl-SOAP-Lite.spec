#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-SOAP-Lite
#    Version:           1.27
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only SOAP\:\:Lite
#

Name:           opt-perl-SOAP-Lite
Version:        1.27
Release:        1%{?dist}
Summary:        Perl's Web Services Toolkit
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/SOAP-Lite/
BuildRoot:      /tmp/cpantorpm/SOAP-Lite-1.27-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/P/PH/PHRED/SOAP-Lite-1.27.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Apache::SOAP) = 1.27
Provides:       opt-perl(SOAP) = 1.27
Provides:       opt-perl(SOAP::Client) = 1.27
Provides:       opt-perl(SOAP::Cloneable) = 1.27
Provides:       opt-perl(SOAP::Constants) = 1.27
Provides:       opt-perl(SOAP::Custom::XML::Data) = 1.27
Provides:       opt-perl(SOAP::Custom::XML::Deserializer) = 1.27
Provides:       opt-perl(SOAP::Data) = 1.27
Provides:       opt-perl(SOAP::Deserializer) = 1.27
Provides:       opt-perl(SOAP::Fault) = 1.27
Provides:       opt-perl(SOAP::Header) = 1.27
Provides:       opt-perl(SOAP::Lite) = 1.27
Provides:       opt-perl(SOAP::Lite::COM) = 1.27
Provides:       opt-perl(SOAP::Lite::Deserializer::XMLSchema1999) = 1.27
Provides:       opt-perl(SOAP::Lite::Deserializer::XMLSchema2001) = 1.27
Provides:       opt-perl(SOAP::Lite::Deserializer::XMLSchemaSOAP1_1) = 1.27
Provides:       opt-perl(SOAP::Lite::Deserializer::XMLSchemaSOAP1_2) = 1.27
Provides:       opt-perl(SOAP::Lite::Packager) = 1.27
Provides:       opt-perl(SOAP::Lite::Packager::DIME) = 1.27
Provides:       opt-perl(SOAP::Lite::Packager::MIME) = 1.27
Provides:       opt-perl(SOAP::Lite::Utils) = 1.27
Provides:       opt-perl(SOAP::Packager) = 1.27
Provides:       opt-perl(SOAP::Packager::DIME) = 1.27
Provides:       opt-perl(SOAP::Packager::MIME) = 1.27
Provides:       opt-perl(SOAP::Parser) = 1.27
Provides:       opt-perl(SOAP::SOM) = 1.27
Provides:       opt-perl(SOAP::Schema) = 1.27
Provides:       opt-perl(SOAP::Schema::Deserializer) = 1.27
Provides:       opt-perl(SOAP::Schema::WSDL) = 1.27
Provides:       opt-perl(SOAP::Serializer) = 1.27
Provides:       opt-perl(SOAP::Server) = 1.27
Provides:       opt-perl(SOAP::Server::Object) = 1.27
Provides:       opt-perl(SOAP::Server::Parameters) = 1.27
Provides:       opt-perl(SOAP::Test) = 1.27
Provides:       opt-perl(SOAP::Test::Server) = 1.27
Provides:       opt-perl(SOAP::Trace) = 1.27
Provides:       opt-perl(SOAP::Transport) = 1.27
Provides:       opt-perl(SOAP::Transport::HTTP) = 1.27
Provides:       opt-perl(SOAP::Transport::HTTP::Apache) = 1.27
Provides:       opt-perl(SOAP::Transport::HTTP::CGI) = 1.27
Provides:       opt-perl(SOAP::Transport::HTTP::Client) = 1.27
Provides:       opt-perl(SOAP::Transport::HTTP::Daemon) = 1.27
Provides:       opt-perl(SOAP::Transport::HTTP::FCGI) = 1.27
Provides:       opt-perl(SOAP::Transport::HTTP::Server) = 1.27
Provides:       opt-perl(SOAP::Transport::IO) = 1.27
Provides:       opt-perl(SOAP::Transport::IO::Server) = 1.27
Provides:       opt-perl(SOAP::Transport::LOCAL) = 1.27
Provides:       opt-perl(SOAP::Transport::LOCAL::Client) = 1.27
Provides:       opt-perl(SOAP::Transport::LOOPBACK) = 1.27
Provides:       opt-perl(SOAP::Transport::LOOPBACK::Client) = 1.27
Provides:       opt-perl(SOAP::Transport::MAILTO) = 1.27
Provides:       opt-perl(SOAP::Transport::MAILTO::Client) = 1.27
Provides:       opt-perl(SOAP::Transport::POP3) = 1.27
Provides:       opt-perl(SOAP::Transport::POP3::Server) = 1.27
Provides:       opt-perl(SOAP::Transport::TCP) = 0.715
Provides:       opt-perl(SOAP::Transport::TCP::Client) = 0.715
Provides:       opt-perl(SOAP::Transport::TCP::Server) = 0.715
Provides:       opt-perl(SOAP::Utils) = 1.27
Provides:       opt-perl(SOAP::XMLSchema1999::Serializer) = 1.27
Provides:       opt-perl(SOAP::XMLSchema2001::Serializer) = 1.27
Provides:       opt-perl(SOAP::XMLSchema::Serializer) = 1.27
Provides:       opt-perl(SOAP::XMLSchemaApacheSOAP::Deserializer) = 1.27
Requires:       opt-perl
Requires:       opt-perl(Class::Inspector)
Requires:       opt-perl(Compress::Zlib)
Requires:       opt-perl(IO::Socket::SSL)
Requires:       opt-perl(LWP::Protocol::https)
Requires:       opt-perl(LWP::UserAgent)
Requires:       opt-perl(MIME::Base64)
Requires:       opt-perl(Scalar::Util)
Requires:       opt-perl(Task::Weaken)
Requires:       opt-perl(URI)
Requires:       opt-perl(constant)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Class::Inspector)
BuildRequires:  opt-perl(Compress::Zlib)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(IO::Socket::SSL)
BuildRequires:  opt-perl(LWP::Protocol::https)
BuildRequires:  opt-perl(LWP::UserAgent)
BuildRequires:  opt-perl(MIME::Base64)
BuildRequires:  opt-perl(Scalar::Util)
BuildRequires:  opt-perl(Task::Weaken)
BuildRequires:  opt-perl(URI)
BuildRequires:  opt-perl(constant)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
SOAP::Lite is a collection of Perl modules which provides a simple and
lightweight interface to the Simple Object Access Protocol (SOAP) both on
client and server side.

%prep

%setup  -n SOAP-Lite-1.27
chmod -R u+w %{_builddir}/SOAP-Lite-%{version}

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
* Thu Oct 04 2018 Rocks 1.27-1
- Generated using cpantorpm

