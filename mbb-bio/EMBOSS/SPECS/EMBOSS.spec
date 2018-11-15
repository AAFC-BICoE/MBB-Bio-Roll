%define name		EMBOSS
%define release		1
%define version 	6.6.0
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

BuildRoot:		%{buildroot}
Summary: 		European Molecular Biolohy Open Software Suite
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		https://github.com/kimrutherford/EMBOSS/archive/%{name}-%{version}.tar.gz
Prefix: 		%{_prefix}
URL:			https://www.ebi.ac.uk/Tools/emboss/
Group: 			Bioinformatics
AutoReq:		yes


%description
EMBOSS is "The European Molecular Biology Open Software Suite". EMBOSS is a free Open Source software analysis package specially developed for the needs of the molecular biology (e.g. EMBnet) user community. The software automatically copes with data in a variety of formats and even allows transparent retrieval of sequence data from the web. Also, as extensive libraries are provided with the package, it is a platform to allow other scientists to develop and release software in true open source spirit. EMBOSS also integrates a range of currently available packages and tools for sequence analysis into a seamless whole. EMBOSS breaks the historical trend towards commercial software packages.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
./configure --prefix=%{_prefix}
export LD_RUN_PATH=%{_libdir}
make -j`nproc`

%install
mkdir -p %{buildroot}%{_bindir}
head -n 834 Makefile > Makefile.new
mv -f Makefile.new Makefile
make install DESTDIR=%{buildroot} 

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc LICENSE
%doc NEWS
%doc AUTHORS
%doc COPYING
%doc KNOWN_BUGS
%{_includedir}
%{_datadir}
%defattr(755,root,root,755)
%{_bindir}
%{_libdir}
