%define name		breakdancer
%define release		1
%define version 	1.4.5
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 

BuildRoot:		%{buildroot}
Summary: 		breakdancer
License: 		GPL3|http://breakdancer.sourceforge.net	
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.tar.gz 
Patch0:			bogus-perl.patch
Prefix: 		%{installroot}
Group: 			Bioinformatics/Variant Calling
AutoReq:		yes

Requires:	opt-perl(FindBin)
Requires:	opt-perl(GD::Graph::histogram)
Requires:	opt-perl(Getopt::Std)
Requires:	opt-perl(Statistics::Descriptive)
Requires:	opt-perl(lib)
Requires:	opt-perl(strict)
Requires:	opt-perl(warnings)

%global __requires_exclude ^perl

%description
BreakDancerMax predicts five types of structural variants: insertions, deletions, inversions, inter- and intra-chromosomal translocations from next-generation short paired-end sequencing reads using read pairs that are mapped with unexpected separation distances or orientation. 

%prep -n 
%setup -q 
%patch -P 0 -p1  

%build
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{installroot} .
make


%install
make install DESTDIR=%{buildroot}
mkdir -p $RPM_BUILD_ROOT%{installroot}

#cp -r perl $RPM_BUILD_ROOT%{installroot}/
#cp cpp/breakdancer_max $RPM_BUILD_ROOT%{installroot}


%files 
%defattr(-,root,root,755)
%doc README
%{installroot}
