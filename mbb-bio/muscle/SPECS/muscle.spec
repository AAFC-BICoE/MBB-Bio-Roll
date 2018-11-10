%define name		muscle	
%define release		1
%define version 	3.8.1551
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		MUSCLE is one of the most widely-used methods in biology. On average, MUSCLE is cited by ten new papers every day. 
License: 		Public Domain
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.tar.gz
Prefix: 		%{_prefix}
URL:			http://www.drive5.com/muscle/
Group: 			Bioinformatics/Alignemtn
AutoReq:		yes

%description
MUSCLE is one of the best-performing multiple alignment programs according to published benchmark tests, with accuracy and speed that are consistently better than CLUSTALW. MUSCLE can align hundreds of sequences in seconds. Most users learn everything they need to know about MUSCLE in a few minutes—only a handful of command-line options are needed to perform common alignment tasks.

%prep
%setup -q -c 

%build
make -j`nproc` LDLIBS=-lm

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp muscle $RPM_BUILD_ROOT%{_bindir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%defattr(755,root,root,755)
%{_bindir}
