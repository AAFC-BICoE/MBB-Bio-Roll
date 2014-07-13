#
### define _topdir	 	/home/rpmbuild/rpms/num-utils 
%define name		num-utils 
%define release		1
%define version 	0.5
%define installroot 	/opt/compute/%{name}
%define buildroot       %{_topdir}/%{name}-%{version}-root

BuildRoot:	%{buildroot}
Summary: 	num-utils 
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
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
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        Unknown
AutoReq:	yes
#Provides:	perl(the) 

%description
The num-utils, short for numeric utilities are a set of programs designed
to work together from the unix shell to do numeric operations on input.
They are basically the numeric equivilent of common unix text utilities
and aim to help complete the unix shell vocabulary.


%prep
%setup -q 

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
mkdir -p $RPM_BUILD_ROOT%{installroot} 
cp -r average bound interval normalize numgrep numprocess numsum random range round template $RPM_BUILD_ROOT%{installroot}
chmod -x $RPM_BUILD_ROOT%{installroot}/average
#cp -r bound interval normalize numgrep numprocess numsum random range round template $RPM_BUILD_ROOT%{installroot}

%files
#installed files are executables 
%defattr(755,root,root)
%{installroot}/bound
%{installroot}/interval
%{installroot}/normalize
%{installroot}/numgrep
%{installroot}/numprocess
%{installroot}/numsum
%{installroot}/random
%{installroot}/range
%{installroot}/round
%{installroot}/template
%{installroot}/average 

# make average executable in post section
%post 

chmod +x %{installroot}/average

