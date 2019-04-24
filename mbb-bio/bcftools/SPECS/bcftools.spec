%define name            bcftools
%define release         1
%define version         1.9
%define buildroot	%{_topdir}/%{name}-%{version}-root
%define installroot	/opt/bio/%{name}
%define _prefix		%{installroot}
%define _libdir		%{_prefix}/lib

BuildRoot:		%{buildroot}
Summary:		BCFtools is a program for variant calling and manipulating files in the Variant Call Format (VCF) and its binary counterpart BCF.	
License:		MIT
Name:			%{name}
Version:		%{version}
Release:		%{release}
Source0:		%{name}-%{version}.tar.bz2
Prefix:			%{installroot}
Group:			Bioinformatics/Variant Calling
AutoReq:		yes
Url:			http://samtools.github.io/bcftools/howtos/index.html

%global __requires_exclude ^perl

Requires:	opt-perl(Carp)
Requires:	opt-perl(Data::Dumper) 
Requires:	opt-perl(Getopt::Std)
Requires:	opt-perl(Storable)
Requires:	opt-perl(strict)
Requires:	opt-perl(warnings) 

%description
BCFtools is a program for variant calling and manipulating files in the Variant
Call Format (VCF) and its binary counterpart BCF. All commands work
transparently with both VCFs and BCFs, both uncompressed and BGZF-compressed.

%prep
%setup -qn %{name}-%{version}

%build
# Do not enable autoheader and autoconf because they require a newer m4 than
# what is provided by CentOS 7
#autoheader 
#autoconf 
./configure --enable-libgsl --enable-perl-filters --prefix=%{installroot}
make -j`nproc`

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}/
make install DESTDIR=%{buildroot} prefix=%{installroot}

%files
%defattr(644,root,root,755)
%dir %{installroot}
%doc AUTHORS
%doc NEWS 
%{_datadir}
%defattr(755,root,root,755)
%{_libexecdir}
%{_bindir}
