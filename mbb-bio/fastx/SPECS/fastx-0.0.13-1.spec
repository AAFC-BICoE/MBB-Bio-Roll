# This is a sample spec file for wget
# TODO: Add documentation 
#
### define _topdir	 	/home/rpmbuild/rpms/fastx
%define name		fastx
%define release		1
%define version 	0.0.13.2
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}


BuildRoot:		%{buildroot}
Summary: 		cufflinks 
License: 		AGPLv3
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}_toolkit-%{version}.tar.bz2 
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes
URL:			http://hannonlab.cshl.edu/fastx_toolkit/download.html

%description
Cufflinks assembles transcripts, estimates their abundances, and tests for differential expression and regulation in RNA-Seq samples. It accepts aligned RNA-Seq reads and assembles the alignments into a parsimonious set of transcripts. Cufflinks then estimates the relative abundances of these transcripts based on how many reads support each one, taking into account biases in library preparation protocols. 


%prep
%setup -qn %{name}_toolkit-%{version}  

%build
export PKG_CONFIG_PATH=/opt/bio/fastx/libgtextutils/lib/pkgconfig/
./configure --prefix=%{installroot}/%{name} 
make 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install prefix=$RPM_BUILD_ROOT%{installroot}


%files
%defattr(755,root,root)
%{installroot}
