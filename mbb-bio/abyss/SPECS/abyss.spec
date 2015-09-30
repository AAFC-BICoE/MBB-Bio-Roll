# This is a  spec file for abyss

%define name		abyss
%define release		1
%define version 	1.9.0
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary:        ABySS is a de novo, parallel, paired-end sequence assembler that is designed for short reads.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.bz2
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://www.bcgsc.ca/platform/bioinfo/software/abyss
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPLv3 for non-commercial usage
AutoReq:	yes

%description 
ABySS is a de novo, parallel, paired-end sequence assembler that is designed for
short reads. The single-processor version is useful for assembling genomes up to
100 Mbases in size. The parallel version is implemented using MPI and is capable
of assembling larger genomes. 

%prep
%setup -q

%build
#./configure --disable-popcnt --enable-maxk=256 --with-boost=/usr/include/boost
./configure --disable-popcnt --enable-maxk=256 --with-boost=/opt/bio/boost/include
make --jobs=`nproc`

%install
mkdir -p %{buildroot}%{installroot}
#mkdir -p %{buildroot}/usr/share/man/man1

make install prefix=%{buildroot}%{installroot}
#rm -r %{buildroot}%{installroot}/share
#mkdir -p %{buildroot}%{installroot}/../share/man/man1
cd doc; cp ABYSS.1 abyss-pe.1 abyss-tofastq.1 %{buildroot}%{installroot}/share/man/man1; cd ..
cd %{buildroot}%{installroot}/bin; file * | grep "not stripped"|grep -Eo '^[^ ]+'|sed "s/://"|xargs strip; cd ..

gzip %{buildroot}%{installroot}/share/man/man1/*

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%doc
%{installroot}/share/man/man1/ABYSS.1.gz
%{installroot}/share/man/man1/abyss-pe.1.gz
%{installroot}/share/man/man1/abyss-tofastq.1.gz
%defattr(644,root,root,755)
%{installroot}/share/man/man1/ABYSS.1.gz
%{installroot}/share/man/man1/abyss-pe.1.gz
%{installroot}/share/man/man1/abyss-tofastq.1.gz
