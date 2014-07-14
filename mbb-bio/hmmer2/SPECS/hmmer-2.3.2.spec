# This is a sample spec file for wget

### define _topdir	 	/home/rpmbuild/rpms/hmmer2
%define name			hmmer2
%define release		cl1
%define version 	3.2
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 		hmmer
License: 		GPL-3|http://selab.janelia.org/software/hmmer3/3.1b1/hmmer-3.1b1.tar.gz	Specified in the LICENSE and COPYRIGHT text files in the package
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
HMMER - Biosequence analysis using profile hidden Markov models

%prep
%setup -q

%build
./configure
make prefix=%{installroot}

%install
make install prefix=$RPM_BUILD_ROOT%{installroot}
#find $RPM_BUILD_ROOT%{installroot} -type f -exec sed -i 's|/root/rpms/amos/amos-3.1.0-root/|/|g' {} \;

%files
%defattr(755,root,root)
%{installroot}
