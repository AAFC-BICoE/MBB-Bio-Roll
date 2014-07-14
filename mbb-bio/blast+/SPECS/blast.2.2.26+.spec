
%define name		ncbi-blast
%define release		cl1
%define version 	2.2.26+
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}+

BuildRoot:	%{buildroot}
Summary: 		BLAST+ is a new suite of BLAST tools that utilizes the NCBI C++ Toolkit
License: 		Public Domain
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
#Source: 		%{name}-%{version}-x64-linux.tar.bz2
Source0: 		%{name}-%{version}-x64-linux-1.tar.bz2
Source1: 		%{name}-%{version}-x64-linux-2.tar.bz2
Source2: 		%{name}-%{version}-x64-linux-3.tar.bz2
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes
URL:			ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/

%description
The new BLAST command-line applications, compared to the current BLAST tools, demonstrate substantial speed improvements for long queries as well as chromosome length database sequences. We have also improved the user interface of the command-line applications.

%prep

%setup  -q -a 0
%setup -D -T -a 1
%setup -D -T -a 2


%build
# nothing to do; using precompiled executables


%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -R * $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
