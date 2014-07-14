### define _topdir	 	/home/rpmbuild/rpms/mothur
%define name		mothur
%define Name		Mothur
%define release		1
%define version 	1.30.2
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/mothur

BuildRoot:		%{buildroot}
Summary: 		The mothur metagenomics analysis package
License: 		Open Source
URL:			http://www.mothur.org/wiki/Download_mothur
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{Name}.%{version}.zip
Patch:			%{Name}.%{version}.patch
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
The goal of mothur is to have a single resource to analyze molecular data that is used by microbial ecologists. Many of these tools are available elsewhere as individual programs and as scripts, which tend to be slow or as web utilities, which limit your ability to analyze your data. mothur offers the ability to go from raw sequences to the generation of visualization tools to describe α and β diversity.

%package MPI
Summary: mothur
Group: Development/Tools
%description MPI
The mothur metagenomics analysis package compiled with MPI support.

%prep
%setup -q -n Mothur.1.30.2
rm -rf ../__MACOSX/
%patch -p 1

%build
# build with MPI support
make MOTHUR_FILES=\"\\\"/opt/bio/mothur\\\"\" USEMPI=yes

# copy executables
mv mothur mothurMPI
mv uchime uchimeMPI

# clean
make clean

# build regular version
make MOTHUR_FILES=\"\\\"/opt/bio/mothur\\\"\"

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
pwd
cp mothur uchime mothurMPI uchimeMPI *.pat $RPM_BUILD_ROOT%{installroot}

%files
%defattr(644,root,root,755)

%{installroot}/*.pat
%files MPI
%defattr(755,root,root,755)
%{installroot}/*MPI
%{installroot}/*.pat
%{installroot}/mothur
%{installroot}/uchime
