
### define _topdir	 	/home/rpmbuild/rpms/cdhit
%define name		cd-hit
%define release		1	
%define version 	4.6.6
%define date		2016-0711
%define buildroot %{_topdir}/%{name}-%{version}%{date}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 		cd-hit
License: 		GPLv2
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}-%{date}.tar.gz
Patch:			opt-perl.patch
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
CD-HIT is a program for clustering DNA/protein sequence database at high
identity with tolerance.

%prep
%setup -q -n %{name}-v%{version}-%{date}
%patch -p1

%build
make openmp=yes -j `nproc`

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install PREFIX=$RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root,755)
%{installroot}
