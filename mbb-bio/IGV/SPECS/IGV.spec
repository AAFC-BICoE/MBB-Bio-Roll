%define name		IGV
%define src_name	igv
%define release		1
%define version 	2.4.14
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name} 
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		IGV
License: 		LGPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source0: 		%{name}-v%{version}.tar.gz
Source1: 		javafx.tar.gz
Prefix: 		%{installroot}
URL:			http://www.broadinstitute.org/igv/
Group: 			Bioinformatics/Visualization
AutoReq:		yes

BuildRequires:		java-sdk >= 1:1.8.0
Requires:		java >= 1.8

%description
The Integrative Genomics Viewer (IGV) is a high-performance visualization tool for interactive exploration of large, integrated genomic datasets. It supports a wide variety of data types, including array-based and next-generation sequence data, and genomic annotations.

%prep
%setup -q -n %{src_name}-%{version} -a 1

%build
./gradlew createDist
./gradlew createToolsDist

%install
mkdir -p %{buildroot}%{installroot}

mv build/IGV-dist/{igv.sh,lib} %{buildroot}%{installroot}/
mv build/IGVTools-dist/{igvtools,igvtools_gui} %{buildroot}%{installroot}/
mv build/IGVTools-dist/lib/* %{buildroot}%{installroot}/lib/


%files
%defattr(644,root,root,755)
%dir %_prefix
%doc license.txt
%doc docs/RelNotes/*.md
%_prefix/lib
%defattr(755,root,root,755)
%_prefix/igv.sh
%_prefix/igvtools
%_prefix/igvtools_gui
