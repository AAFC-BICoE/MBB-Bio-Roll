### %define _topdir     /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/Curses
%define name            Curses
%define release		1         
%define version         1.34  
%define installroot     /opt/bio/%{name}

Summary:   Terminal screen handling and optimization
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    %{name}-%{version}.tar.gz
License:   GPL 1
Packager:  Alex MacLean <alex.maclean@agr.gc.ca>
Group:     Development/Libraries
Prefix:    /opt/bio
Vendor:    Bryan Henderson <bryanh@giraffe-data.com>
Url:       http://search.cpan.org/CPAN/authors/id/G/GI/GIRAFFED/Curses-1.34.tar.gz
Autoreq:   yes
Autoprov:  yes

%description
Curses is the interface between Perl and your system's curses(3) library.

%prep
%setup -q -n Curses-1.34

%build
mkdir ../curses
/opt/perl/bin/perl Makefile.PL PREFIX=/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/Curses/BUILD/curses
make
make test

%install
make install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cd ..
cp -r curses/lib curses/man $RPM_BUILD_ROOT%{installroot}/

%clean

%files
%defattr(755,root,root,755)
%{installroot}
