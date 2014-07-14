
%define name		BEAST
### define _topdir	 	/home/rpmbuild/rpms/BEAST
%define release		1
%define version 	v1.7.5
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 

BuildRoot:		%{buildroot}
Summary: 		BEAST
License: 		Lesser GPL|https://code.google.com/p/beast-mcmc
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		BEASTv1.7.5.tgz
Patch0:         %{name}%{version}.patch0
Patch1:         %{name}%{version}.patch1
Patch2:         %{name}%{version}.patch2
Patch3:         %{name}%{version}.patch3
Patch4:         %{name}%{version}.patch4
Patch5:         %{name}%{version}.patch5
Patch6:         %{name}%{version}.patch6
Packager:	Glen Newton <glen.newton@agr.gc.ca>
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes
URL:                    http://beast.bio.ed.ac.uk

%description
BEAST is a cross-platform program for Bayesian MCMC analysis of molecular sequences. It is entirely orientated towards rooted, time-measured phylogenies inferred using strict or relaxed molecular clock models. It can be used as a method of reconstructing phylogenies but is also a framework for testing evolutionary hypotheses without conditioning on a single tree topology. BEAST uses MCMC to average over tree space, so that each tree is weighted proportional to its posterior probability. We include a simple to use user-interface program for setting up standard analyses and a suit of programs for analysing the results. 

%prep
%setup -qn BEASTv1.7.5
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1

%build

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
cp -r *  $RPM_BUILD_ROOT%{installroot}

%files
%defattr(0755,root,root) 
%{installroot}
