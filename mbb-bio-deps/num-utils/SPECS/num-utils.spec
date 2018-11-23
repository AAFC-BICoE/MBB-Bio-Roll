%define name		opt-num-utils 
%define src_name	num-utils
%define release		1
%define version 	0.5
%define installroot 	/opt/bio/%{src_name}
%define buildroot       %{_topdir}/%{name}-%{version}-root
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary: 	num-utils 
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{src_name}-%{version}.tar.gz
patch0:		average.patch
patch1:		bound.patch
patch2:		interval.patch
patch3:		normalize.patch
patch4:		numgrep.patch
patch5:		numprocess.patch
patch6:		numsum.patch
patch7:		random.patch
patch8:		range.patch
patch9:		round.patch
patch10:	template.patch
Prefix: 	%{_prefix}
Group: 		Development/Tools
License:        GPL
AutoReq:	no
Requires:	opt-perl(Getopt::Std)
Requires: 	opt-perl(POSIX)
Requires: 	opt-perl(strict)
Requires: 	opt-perl(vars)
Requires: 	opt-perl(warnings)

%description
The num-utils, short for numeric utilities are a set of programs designed
to work together from the unix shell to do numeric operations on input.
They are basically the numeric equivilent of common unix text utilities
and aim to help complete the unix shell vocabulary.

%prep
%setup -q -n %{src_name}-%{version}

%patch -P 0 -p0
%patch -P 1 -p0
%patch -P 2 -p0
%patch -P 3 -p0
%patch -P 4 -p0
%patch -P 5 -p0
%patch -P 6 -p0
%patch -P 7 -p0
%patch -P 8 -p0
%patch -P 9 -p0
%patch -P 10 -p0

%build
## perl scripts 

%install
mkdir -p %{buildroot}%{_bindir}
cp -r average bound interval normalize numgrep numprocess numsum random range round template %{buildroot}%{_bindir}

%files
%defattr(644,root,root,755)
%doc COPYING
%doc LICENSE
%doc CHANGELOG
%defattr(755,root,root,755)
%{_bindir}/bound
%{_bindir}/interval
%{_bindir}/normalize
%{_bindir}/numgrep
%{_bindir}/numprocess
%{_bindir}/numsum
%{_bindir}/random
%{_bindir}/range
%{_bindir}/round
%{_bindir}/template
%{_bindir}/average 
