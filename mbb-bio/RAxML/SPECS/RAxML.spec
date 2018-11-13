%define name		RAxML
%define release		1
%define version 	8.2.12
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:	%{buildroot}
Summary:        Randomized Axelerated Maximum likelihood
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-v%{version}.tar.gz
URL:            http://www.exelixis-lab.org/
Prefix: 	%{_prefix}
Group: 		Development/Tools
License:        GPL
AutoReq:	yes

%description
RAxML (Randomized Axelerated Maximum Likelihood) is a program for sequential and parallel Maximum
Likelihood [1] based inference of large phylogenetic trees. It has originally been derived from fastDNAml
which in turn was derived from Joe Felsentein’s dnaml which is part of the PHYLIP [2] package.


%prep
%setup -q -n standard-%{name}-%{version}

%build
#make -f Makefile.gcc 
for i in {SSE3,AVX,SSE3.PTHREADS,AVX.PTHREADS,SSE3.MPI,AVX.MPI,SSE3.HYBRID,AVX.HYBRID}; do
	make -f Makefile.$i.gcc -j`nproc`
	rm *.o
done

%install
#make -f Makefile.gcc install prefix=$RPM_BUILD_ROOT%{installroot}
mkdir -p %{buildroot}%{_bindir}
cp ./raxmlHPC* %{buildroot}%{_bindir}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc manual/NewManual.pdf
%defattr(755,root,root,755)
%{_bindir}
