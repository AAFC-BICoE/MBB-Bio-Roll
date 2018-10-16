
### define _topdir	 	/home/rpmbuild/rpms/cdhit
%define name		cd-hit
%define release		1	
%define version 	4.6.8
%define buildroot 	%{_topdir}/%{name}-%{version}%{date}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		cd-hit
License: 		GPLv2
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.tar.gz
Patch0:			env-perl.patch
Prefix: 		%{installroot}
Group: 			Development/Tools
AutoReq:		yes

Requires:		opt-perl

Requires:	opt-perl(Image::Magick)
Requires:	opt-perl(Storable)
Requires:	opt-perl(Text::NSP::Measures::2D::Fisher::right)
Requires:	opt-perl(strict)

%global __requires_exclude ^perl

%description
CD-HIT is a program for clustering DNA/protein sequence database at high
identity with tolerance.

%prep
%setup -q -n cdhit-%{version}
%patch0 -p1

%build
make openmp=yes -j `nproc`

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/bin
make install PREFIX=$RPM_BUILD_ROOT%{installroot}/bin

%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc README
%doc license.txt
%doc ChangeLog
%defattr(755,root,root,755)
%{installroot}/bin
