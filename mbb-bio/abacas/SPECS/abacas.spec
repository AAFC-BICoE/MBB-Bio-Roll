%define name		abacas
%define release		1
%define version 	1.3.1
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}
BuildRoot:	%{buildroot}
Summary:	ABACAS is intended to rapidly contiguate (align, order, orientate), visualize and design primers to close gaps on assembled contigs based on a reference sequence. 
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}.%{version}.pl
Patch0:		%{name}-%{version}-%{release}.patch0
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://abacas.sourceforge.net/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPLv2
Requires: 	opt-perl(Getopt::Std)
Requires:	opt-perl(POSIX) 
Requires:	opt-perl(strict) 
Requires:	opt-perl(warnings)

%description
ABACAS is intended to rapidly contiguate (align, order, orientate), visualize
and design primers to close gaps on assembled contigs based on a reference
sequence.  
ABACAS uses MUMmer to find alignment positions and identify syntenies of
assembled contigs against the reference. The output is then processed to
generate a pseudomolecule taking overlapping contigs and gaps in to account.
ABACAS generates a comparision file that can be used to visualize ordered and
oriented contigs in ACT. Synteny is represented by red bars where colour
intensity decreases with lower values of percent identity between comparable
blocks. Information on contigs such as the orientation, percent identity,
coverage and overlap with other contigs can also be visualized by loading the
outputted feature file on ACT. 

%prep
%setup -q -T -c -n abacas
cp ../../SOURCES/abacas.1.3.1.pl .
%patch -P 0 -p1

%build
mv abacas.1.3.1.pl abacas
chmod 755 abacas

%install
mkdir -p %{buildroot}%{_bindir}
cp abacas %{buildroot}%{_bindir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%defattr(755,root,root,755)
%{_bindir}
