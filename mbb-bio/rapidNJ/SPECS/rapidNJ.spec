%define name		rapidNJ
%define release		1
%define version 	2.3.2 
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		rapidNJ 
License: 		GPLv2
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.tar.gz
Prefix: 		%{_prefix}
Group: 			Bioinformatics/Phylohenetics
AutoReq:		yes

%description
RapidNJ is an algorithmic engineered implementation of canonical
neighbour-joining. It uses an efficient search heuristic to speed-up the core
computations of the neighbour-joining method that enables RapidNJ to outperform
other state-of-the-art neighbour-joining implementations. 

%prep
%setup -qn %{name}

%build
make -j`nproc`

%install
mkdir -p %{buildroot}%{_bindir}
cp bin/* %{buildroot}%{_bindir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc README
%defattr(755,root,root,755)
%{_bindir}
