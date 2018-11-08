%define debug_package	%{nil}
%define name		mcl
%define release		1
%define version		14.137
%define src_version	14-137
%define installroot	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	The Markov Cluster Algorithm, aka the MCL algorithm.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Packager:	Glen Newton glen.newton@agr.gc.ca
Source: 	%{name}-%{src_version}.tar.gz
URL:            http://micans.org/mcl/
Prefix: 	%{_prefix}
Group: 		Bioinformatics/Clustering
License:        GPLv3
AutoReq:	yes

%global	__requires_exclude ^perl

Requires:	opt-perl(strict)

%description
This program implements mcl, a cluster algorithm for graphs. A single parameter controls the granularity of the output clustering, namely the -I inflation option described further below. In standard usage of the program this parameter is the only one that may require changing. By default it is set to 2.0 and this is a good way to start. If you want to explore cluster structure in graphs with MCL, vary this parameter to obtain clusterings at different levels of granularity. A good set of starting values is 1.4, 2, 4, and 6. 
Citation: Enright A.J., Van Dongen S., Ouzounis C.A. An efficient algorithm for large-scale detection of protein families. Nucleic Acids Research 30(7):1575-1584 (2002).

%prep
%setup -q -n %{name}-%{src_version}

%build
./configure --prefix=%{installroot}
make --jobs=`nproc`

%install
mkdir -p %{buildroot}%{installroot}
make install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc COPYING
%doc AUTHORS
%doc ChangeLog
%doc LICENSE
%{_docdir}
%{_mandir}
%defattr(755,root,root,755)
%{_bindir}
