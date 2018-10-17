#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Text-Format
#    Version:           0.61
#    cpantorpm version: 1.08
#    Date:              Wed Oct 17 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Text\:\:Format
#

Name:           opt-perl-Text-Format
Version:        0.61
Release:        1%{?dist}
Summary:        Various subroutines to format text.
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Text-Format/
BuildRoot:      /tmp/cpantorpm/Text-Format-0.61-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/S/SH/SHLOMIF/Text-Format-0.61.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Text::Format) = 0.61
Requires:       opt-perl
Requires:       opt-perl(Carp)
Requires:       opt-perl(strict)
Requires:       opt-perl(warnings)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(Carp)
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(strict)
BuildRequires:  opt-perl(warnings)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The format routine will format under all circumstances even if the width
isn't enough to contain the longest words. Text::Wrap will die under
these circumstances, although I am told this is fixed. If columns is set to
a small number and words are longer than that and the leading 'whitespace'
than there will be a single word on each line. This will let you make a
simple word list which could be indented or right aligned. There is a
chance for croaking if you try to subvert the module. If you don't pass in
text then the internal text is worked on, though not modified.

%prep

%setup  -n Text-Format-0.61
chmod -R u+w %{_builddir}/Text-Format-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Build.PL optimize="$RPM_OPT_FLAGS" --installdirs site --install_path arch=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi --install_path lib=/opt/perl/lib/site_perl/5.26.0 --install_path script=/opt/perl/bin --install_path bin=/opt/perl/bin --install_path libdoc=/opt/perl/man/man3 --install_path bindoc=/opt/perl/man/man1
./Build

#
# This is included here instead of in the 'check' section because
# older versions of rpmbuild (such as the one distributed with RHEL5)
# do not do 'check' by default.
#

if [ -z "$RPMBUILD_NOTESTS" ]; then
   ./Build test
fi

%install

rm -rf $RPM_BUILD_ROOT
./Build pure_install destdir=$RPM_BUILD_ROOT create_packlist=0
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
* Wed Oct 17 2018 Rocks 0.61-1
- Generated using cpantorpm

