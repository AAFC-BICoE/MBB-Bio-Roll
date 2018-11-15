%define name		t-coffee
%define src_name	T-COFFEE
%define release		1
%define version 	11.00.8cbe486
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		T-Coffee is a multiple sequence alignment package.	
License: 		GPL
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-v%{version}.tar.gz
Prefix: 		%{_prefix}
URL:			http://www.tcoffee.org/Projects/tcoffee/index.html
Group: 			Bioinformatics/Alignment
AutoReq:		yes


%description
T-Coffee is a multiple sequence alignment package. You can use T-Coffee to align sequences or to combine the output of your favorite alignment methods (Clustal, Mafft, Probcons, Muscle...) into one unique alignment (M-Coffee). 

T-Coffee can align Protein, DNA and RNA sequences. It is also able to combine sequence information with protein structural information (3D-Coffee/Expresso), profile information (PSI-Coffee) or RNA secondary structures (R-Coffee).

%prep
%setup -q -n %{src_name}_distribution_Version_%{version}

%build
cd t_coffee_source
make -j`nproc` all FCC=gfortran

%install
mkdir -p %{buildroot}%{_bindir}
cd t_coffee_source
mv t_coffee TMalign %{buildroot}%{_bindir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc license.txt
%defattr(755,root,root,755)
%{_bindir}
