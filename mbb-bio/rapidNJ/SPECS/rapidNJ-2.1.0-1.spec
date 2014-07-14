# 
### define _topdir	 	/home/rpmbuild/rpms/rapidNJ
%define srcName		rapidnj
%define name		rapidNJ
%define release		1
%define version 	2.1.0 
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}


BuildRoot:		%{buildroot}
Summary: 		rapidNJ 
License: 		GPL 
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{srcName}-src-%{version}.zip
Prefix: 		/opt/bio
Group: 			Development/Tools
AutoReq:		yes

%description
RapidNJ is an algorithmic engineered implementation of canonical
neighbour-joining. It uses an efficient search heuristic to speed-up the core
computations of the neighbour-joining method that enables RapidNJ to outperform
other state-of-the-art neighbour-joining implementations. 

%prep
%setup -qn %{name}

%build
make 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp bin/* $RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
