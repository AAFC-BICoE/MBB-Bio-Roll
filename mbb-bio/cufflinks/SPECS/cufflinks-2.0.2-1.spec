# This is a sample spec file for wget
# TODO: Add documentation 
#
### define _topdir	 	/home/rpmbuild/rpms/cufflinks 
%define name		cufflinks
%define release		1
%define version 	2.0.2
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define insSet		x86_64
%define debug_package	%{nil} 


BuildRoot:		%{buildroot}
Summary: 		cufflinks 
License: 		Boost Software License 
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.Linux_%{insSet}.tar.gz 
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
Cufflinks assembles transcripts, estimates their abundances, and tests for differential expression and regulation in RNA-Seq samples. It accepts aligned RNA-Seq reads and assembles the alignments into a parsimonious set of transcripts. Cufflinks then estimates the relative abundances of these transcripts based on how many reads support each one, taking into account biases in library preparation protocols. 


%prep
%setup -q -n %{name}-%{version}.Linux_%{insSet}

%build
#already compiled

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp cuffcompare  cuffdiff  cufflinks  cuffmerge  gffread  gtf_to_sam  $RPM_BUILD_ROOT%{installroot}


%files
%defattr(755,root,root)
%{installroot}
