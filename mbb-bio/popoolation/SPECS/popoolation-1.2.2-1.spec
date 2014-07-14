
%define name		popoolation 
### define _topdir	 	/home/rpmbuild/rpms/popoolation
%define release		1
%define version 	1.2.2
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 


BuildRoot:		%{buildroot}
Summary: 		PoPoolation is a collection of tools to facilitate population genetic studies of next generation sequencing data from pooled individuals
License: 		BSD
URL:			https://code.google.com/p/popoolation/
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}_%{version}.zip
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
Currently next generation sequencing (NGS) technologies are mainly used to sequence individuals. However, the high coverage required and the resulting costs may be prohibitive for population scale studies. Sequencing pools of individuals instead may often be more cost effective and more accurate than sequencing individuals. PoPoolation is a pipeline for analysing pooled next generation sequencing data. PoPoolation builds upon open source tools (bwa, samtools) and uses standard file formats (gtf, sam, pileup) to ensure a wide compatibility. Currently PoPoolation allows to calculate Tajima’s Pi, Watterson’s Theta and Tajima’s D for reference sequences using a sliding window approach. Alternatively these population genetic estimators may be calculated for a set of genes (provided as gtf). One of the main challenges in population genomics is to identify regions of intererest on a genome wide scale. We believe that PoPoolation will greatly aid this task by allowing a fast and user friendly analysis of NGS data from DNA pools. 

%prep
%setup -qn %{name}_%{version}

%build
#poopolation is a collection of perl scrips 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r *  $RPM_BUILD_ROOT%{installroot}


%files
#scripts and folders both need 755
%defattr(755,root,root)
%{installroot}
