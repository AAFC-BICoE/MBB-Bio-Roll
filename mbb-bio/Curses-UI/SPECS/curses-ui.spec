### %define _topdir     /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/Curses-UI
%define name            Curses-UI
%define release		1         
%define version         0.9609  
%define installroot     /opt/bio/%{name}

Summary:   A curses based OO user interface framework
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    %{name}-%{version}.tar.gz
License:   GPL 1
Packager:  Alex MacLean <alex.maclean@agr.gc.ca>
Group:     Development/Tools
Prefix:    /opt/bio
Vendor:    Shawn Boyette <mdxi@cpan.org>
Url:       http://search.cpan.org/CPAN/authors/id/M/MD/MDXI/Curses-UI-0.9609.tar.gz
Autoreq:   yes
Autoprov:  yes

%description
A UI framework based on the curses library.

%prep
%setup -q -n Curses-UI-0.9609

%build
mkdir curses-ui
/opt/perl/bin/perl Makefile.PL PREFIX=/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/Curses-UI/BUILD/curses-ui
make
make test

%install
make install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cd ..
cp -r curses-ui/lib curses-ui/man $RPM_BUILD_ROOT%{installroot}/

%clean

%files
%defattr(755,root,root,755)
%{installroot}
