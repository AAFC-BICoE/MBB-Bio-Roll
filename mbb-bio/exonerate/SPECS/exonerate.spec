#This is a sample spec file for wget
# TODO: Add documentation 
#
### define _topdir	 	/home/rpmbuild/rpms/exonerate
%define name		exonerate
%define release		1
%define version 	2.2.0
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define debug_package 	%{nil} 
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		exonerate
License: 		GNU GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		%{installroot}
Group: 			Bioinformatics/Alignment
AutoReq:		yes

%description
 exonerate is a generic tool for pairwise sequence comparison.
 It allows you to align sequences using a many alignment models, using either exhaustive dynamic programming, or a variety of heuristics. 


%prep
%setup -q
./configure --prefix=%{installroot}

%build
#Parallel builds fail
make 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc README
%doc COPYING
%doc ChangeLog
%doc NEWS
%doc AUTHORS
%{installroot}/share
%defattr(755,root,root,755)
%{installroot}/bin
