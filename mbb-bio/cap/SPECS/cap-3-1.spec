# This is a  spec file for CAP3

%define name		cap
%define release		1
%define version 	3
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	CAP3 is a DNA sequence assembly program to assemble a set of contiguous sequences (contigs).
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}%{version}.linux.x86_64.tar
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://doua.prabi.fr/software/cap3
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        Free for non-commercial use
AutoReq:	yes

%description
CAP3 is a DNA sequence assembly program to assemble a set of contiguous
sequences (contigs).

%prep
%setup -q -n CAP3

%build

%install
mkdir -p %{buildroot}%{installroot}
cp -r * %{buildroot}%{installroot}

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/cap3
%{installroot}/formcon

