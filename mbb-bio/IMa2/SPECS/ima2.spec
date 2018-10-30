%define name		ima2
%define release		1
%define version 	8.27.12
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		IMa2 is a progam that extends the method of Hey and Nielsen (2007) to two or more populations. 
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz 
Prefix: 		%{installroot}
URL:			https://bio.cst.temple.edu/~hey/software/
Group: 			Bioinformatics/Population Genetics
AutoReq:		yes

%description
The program implements a method for generating posterior probabilities for complex demographic population genetic models. IMa2 works similarly to the older IMa program, with some important additions. IMa2 can handle data and implement a model for multiple populations (for numbers of sampled populations between one and ten) – not just two populations (as was the case with the original IM and IMa programs). The method for multiple populations is described in two papers (Hey in press-b, a)

%prep
%setup -q

%build
./configure --prefix=%{installroot}
make -j`nproc` 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%defattr(755,root,root,755)
%{_bindir}/IMa2
