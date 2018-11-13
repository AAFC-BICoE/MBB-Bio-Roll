### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/SeqPrep
%define name		SeqPrep
%define version		1.2
%define release		1
%define installroot	/opt/bio/%{name}
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define _prefix		%{installroot}

summary:		SeqPrep is a program to merge paried end Illumina reads that are overlapping into a single longer read.
Name:			%{name}
Version:		%{version}
Release:		%{release}
Prefix:			%{_prefix}
BuildRoot:		%{buildroot}
Source0:		v%{version}.tar.gz
Patch0:			patchfile.patch
Group:			Development/Tools
License:		MIT 
Vendor:			Free Software Foundation, Inc. <http://fsf.org/>
Packager:		Katherine Beaulieu <katherine.beaulieu@canada.ca>
Url:			https://github.com/jstjohn/SeqPrep
AutoReq:		yes
AutoProv:		yes

%description
SeqPrep is a program to merge paired end Illumina reads that are overlapping into a single longer read.

%prep
%setup -q -n %{name}-%{version}

%patch -P 0
%build
make PREFIX=%{_prefix} -j`nproc`

%install
mkdir -p %{buildroot}%{installroot}
mkdir -p %{buildroot}%{_docdir}

make install HOME=%{buildroot}%{installroot}
cp README.md %{buildroot}%{_docdir}

%files 
%defattr(644,root,root,755)
%dir %{_prefix}
%docdir %{_docdir}
%{_docdir}
%defattr(755,root,root,755)
%{_prefix}/SeqPrep

