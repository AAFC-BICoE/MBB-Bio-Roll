# This is a  spec file for velvet
%define debug_package %{nil}

%define name		mcl
%define release		14
%define version 	137
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	The Markov Cluster Algorithm, aka the MCL algorithm.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Packager:	Glen Newton glen.newton@agr.gc.ca
Source: 	mcl-14-137.tar.gz
URL:            http://micans.org/mcl/
Prefix: 	/opt/bio
Group: 		Applications/BioInformatics
License:        GPL-3
AutoReq:	yes

%description
This program implements mcl, a cluster algorithm for graphs. A single parameter controls the granularity of the output clustering, namely the -I inflation option described further below. In standard usage of the program this parameter is the only one that may require changing. By default it is set to 2.0 and this is a good way to start. If you want to explore cluster structure in graphs with MCL, vary this parameter to obtain clusterings at different levels of granularity. A good set of starting values is 1.4, 2, 4, and 6. 
Citation: Enright A.J., Van Dongen S., Ouzounis C.A. An efficient algorithm for large-scale detection of protein families. Nucleic Acids Research 30(7):1575-1584 (2002).

%prep
%setup -q -n mcl-14-137


%build
./configure  --prefix=%{installroot}
make --jobs=`nproc`


%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install prefix=$RPM_BUILD_ROOT%{installroot}
cd $RPM_BUILD_ROOT%{installroot}/bin; file * | grep "not stripped"|grep -Eo '^[^ ]+'|sed "s/://"|xargs strip


%files
%defattr(755,root,root,755)
%{installroot}
%defattr(644,root,root,755)


