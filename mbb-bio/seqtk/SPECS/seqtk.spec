%define debug_package %{nil}

%define name		seqtk
%define release		1
%define version		4612adf23b
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define installroot	/opt/bio/%{name}
%define _prefix		%{installroot}
%define debug_package	%{nil}

BuildRoot:	%{buildroot}
Summary: 	Seqtk is a C program that converts a fastq file to a fasta file
Name: 		%{name}
Version: 	%{version}
Release: 	1
License: 	MIT|Verified by emailing creator (lh3@me.com)	
Group: 		Development/Tools
Prefix:      	%{_prefix}
URL: 		https://github.com/lh3/misc/tree/4612adf23b07366ec1c5a38d24acc53bf89a0115/seq/seqtk
Source: 	%{name}-%{version}.tar.gz
Packager:	Glen Newton <glen.newton@agr.gc.ca>

%description
Seqtk is a fast and lightweight tool for processing sequences in the FASTA or FASTQ format. It seamlessly parses both FASTA and FASTQ files which can also be optionally compressed by gzip.

%prep
%setup -q -n %{name}-%{version}

%build
make -j`nproc`

%install
mkdir -p %{buildroot}%{installroot}
cp seqtk %{buildroot}%{installroot}

%clean
rm -rf %{buildroot}


%files
%defattr(755,root,root,755)
%{_prefix}
%doc


%changelog
* Wed Apr 17 2013 glen newton <newtong@onottr624241.agr.gc.ca> - 4612adf23b-1
- Initial build.

