%define name		mafft
%define release		1
%define version 	7.407
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{name}
%define _prefix		%{installroot}

BuildRoot:		%{buildroot}
Summary: 		Multiple alignment program for amino acid or nucleotide sequences
License: 		Public Domain /w restrictions (http://mafft.cbrc.jp/alignment/software/license66.txt)
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}-with-extensions-src.tgz
Patch0:			env-perl.patch
Prefix: 		%{_prefix}
URL:			http://mafft.cbrc.jp/alignment/software/
Group: 			Bioinformatics/Alignment
AutoReq:		yes

%global __requires_exclude ^perl
Requires:		opt-perl(Cwd)
Requires:		opt-perl(File::Path)
Requires:		opt-perl(Getopt::Long)
Requires:		opt-perl(LWP::Protocol::http)
Requires:		opt-perl(LWP::Simple)
Requires:		opt-perl(LWP::UserAgent)
Requires:		opt-perl(strict)


%description
MAFFT is a multiple sequence alignment program for unix-like operating systems.  It offers a range of multiple alignment methods, L-INS-i (accurate; for alignment of <~200 sequences), FFT-NS-2 (fast; for alignment of<~10,000 sequences), etc.

%prep
%setup -q -n %{name}-%{version}-with-extensions
%patch0 -p 1

%build
cd core
make   -pipe --jobs=`nproc` PREFIX=%{_prefix}
cd ..
cd extensions
make  -pipe --jobs=`nproc` PREFIX=%{_prefix}
cd ..

%install
mkdir -p %{buildroot}%{_prefix}
cd core
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
cd ..
pushd %{buildroot}%{_bindir}
rm mafft-distance; ln -s ../libexec/mafft/mafft-distance 
rm mafft-profile; ln -s ../libexec/mafft/mafft-profile 
popd

pushd extensions
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc license
%doc readme
%{_datadir}
%defattr(755,root,root,755)
%{_libexecdir}
%{_bindir}
