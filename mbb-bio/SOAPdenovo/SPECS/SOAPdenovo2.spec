### define _topdir	 	/home/rpmbuild/rpms/SOAPdenovo
%define name		SOAPdenovo2
%define release		1
%define version 	r241
%define vc_version	r241
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
License: 		GPL v3
Summary: 		SOAPdenovo2
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-src-%{vc_version}.tgz
Prefix: 		%{_prefix}
URL:			https://github.com/aquaskyline/SOAPdenovo2
Group: 			Development/Tools
AutoReq:		yes

%description
SOAPdenovo is a novel short-read assembly method that can build a de novo draft
assembly for the human-sized genomes. The program is specially designed to
assemble Illumina GA short reads. It creates new opportunities for building
reference sequences and carrying out accurate analyses of unexplored genomes in
a cost effective way. Now the new version is available. SOAPdenovo2, which has
the advantage of a new algorithm design that reduces memory consumption in
graph construction, resolves more repeat regions in contig assembly, increases
coverage and length in scaffold construction, improves gap closing, and
optimizes for large genome.

%prep
%setup -qn %{name}-%{vc_version}

%build
make -j`nproc`

%install
mkdir -p $RPM_BUILD_ROOT%{_prefix}
cp SOAPdenovo-63mer  $RPM_BUILD_ROOT%{_prefix}/SOAPdenovo2-63mer
cp SOAPdenovo-127mer $RPM_BUILD_ROOT%{_prefix}/SOAPdenovo2-127mer
cp LICENSE $RPM_BUILD_ROOT%{_prefix}/LICENSE
cp VERSION $RPM_BUILD_ROOT%{_prefix}/VERSION
cp README.md $RPM_BUILD_ROOT%{_prefix}/README.md

%files
%defattr(755,root,root)
%{_prefix}/SOAPdenovo2-63mer
%{_prefix}/SOAPdenovo2-127mer
%defattr(644,root,root)
%doc %{_prefix}/LICENSE
%doc %{_prefix}/VERSION
%doc %{_prefix}/README.md

