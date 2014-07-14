# This is a sample spec file for wget

### define _topdir	 	/home/rpmbuild/rpms/SOAPdenovo
%define name		SOAPdenovo2
%define release		3
%define version 	r240
%define vc_version	r240
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
License: 		GPL v3
Summary: 		SOAPdenovo2
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-src-%{vc_version}.tgz
Prefix: 		/opt/bio
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
%setup -qn %{name}-src-%{vc_version}

%build
make
# cd sparsePregraph
# make
# make 127mer=1
# cd ../standardPregraph
# make
# make 127mer=1

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp SOAPdenovo-63mer  $RPM_BUILD_ROOT%{installroot}/SOAPdenovo2-63mer
cp SOAPdenovo-127mer $RPM_BUILD_ROOT%{installroot}/SOAPdenovo2-127mer
cp LICENSE $RPM_BUILD_ROOT%{installroot}/LICENSE
cp VERSION $RPM_BUILD_ROOT%{installroot}/VERSION
cp MANUAL $RPM_BUILD_ROOT%{installroot}/MANUAL
#cp sparsePregraph/pregraph_sparse_63mer.v1.0.3 $RPM_BUILD_ROOT%{installroot}
#cp sparsePregraph/pregraph_sparse_127mer.v1.0.3 $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}/SOAPdenovo2-63mer
%{installroot}/SOAPdenovo2-127mer
%defattr(644,root,root)
%{installroot}/LICENSE
%{installroot}/VERSION
%{installroot}/MANUAL


# %files sparse
# %defattr(755,root,root)
# %{installroot}/pregraph_sparse_63mer.v1.0.3
# %{installroot}/pregraph_sparse_127mer.v1.0.3
