# This is a sample spec file for wget

%define name		breakdancer
### define _topdir	 	/home/rpmbuild/rpms/breakdancer
%define release		1
%define version 	1.1
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 
%define timestamp	2011_02_21	


BuildRoot:		%{buildroot}
Summary: 		breakdancer
License: 		GPL3|http://breakdancer.sourceforge.net	
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz 
Patch0:			bam2cfg.pl.patch	
Patch1:			Makefile.patch
Patch2:			BreakDancerMax.pl.patch
Patch3:			BreakDancerMini.pl.patch
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes


%description
BreakDancerMax predicts five types of structural variants: insertions, deletions, inversions, inter- and intra-chromosomal translocations from next-generation short paired-end sequencing reads using read pairs that are mapped with unexpected separation distances or orientation. 

Source is customized to include breakdancermax.pl from earlier version 

%prep
%setup -q 
%patch -P 0 -p1  
%patch -P 1 -p1  
%patch -P 2 -p1  
%patch -P 3 -p1  

%build
cd cpp
make 


%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r perl $RPM_BUILD_ROOT%{installroot}/
cp cpp/breakdancer_max $RPM_BUILD_ROOT%{installroot}


%files 
%defattr(644,root,root,755)
%{installroot}
%attr(755,root,root) %{installroot}/perl/bam2cfg.pl 
%attr(755,root,root) %{installroot}/perl/BreakDancerMax.pl 
%attr(755,root,root) %{installroot}/perl/BreakDancerMini.pl 
%attr(755,root,root) %{installroot}/breakdancer_max
