# This is a  spec file for amos

### define _topdir	 	/home/rpmbuild/rpms/amos
%define name		amos
%define release		3
%define version 	3.1.0
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	The AMOS consortium is committed to the development of open-source whole genome assembly software.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}-%{release}.configure.patch0
Patch1:         %{name}-%{version}-%{release}.AMOS.patch1
Patch2:         %{name}-%{version}-%{release}.Bambus_Bundler.patch2
Patch3:         %{name}-%{version}-%{release}.Bambus_Output.patch3
Patch4:         %{name}-%{version}-%{release}.Bambus_Untangler.patch4
Patch5:         %{name}-%{version}-%{release}.Bank.patch5
Patch6:         %{name}-%{version}-%{release}.Casm.patch6
Patch7:         %{name}-%{version}-%{release}.CelMsg.patch7
Patch8:         %{name}-%{version}-%{release}.Common.patch8
Patch9:         %{name}-%{version}-%{release}.Compare.patch9
Patch10:         %{name}-%{version}-%{release}.Contig.patch10
Patch11:         %{name}-%{version}-%{release}.Converters.patch11
Patch12:         %{name}-%{version}-%{release}.CtgTrim.patch12
Patch13:         %{name}-%{version}-%{release}.Experimental.patch13
Patch14:         %{name}-%{version}-%{release}.Graph.patch14
Patch15:         %{name}-%{version}-%{release}.hawkeye.patch15
Patch16:         %{name}-%{version}-%{release}.Message.patch16
Patch17:         %{name}-%{version}-%{release}.PerlModules.patch17
Patch18:         %{name}-%{version}-%{release}.Pipeline.patch18
Patch19:         %{name}-%{version}-%{release}.PythonModules.patch19
Patch20:         %{name}-%{version}-%{release}.Sim.patch20
Patch21:         %{name}-%{version}-%{release}.Slice.patch21
Patch22:         %{name}-%{version}-%{release}.Tigger.patch22
Patch23:         %{name}-%{version}-%{release}.Utils.patch23
Patch24:         %{name}-%{version}-%{release}.Validation.patch24
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://sourceforge.net/apps/mediawiki/amos/index.php?title=AMOS
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        Artistic License
AutoReq:	yes

%description
The AMOS consortium is committed to the development of open-source whole genome
assembly software. The project acronym (AMOS) represents our primary goal - to
produce A Modular, Open-Source whole genome assembler. Open-source so that
everyone is welcome to contribute and help build outstanding assembly tools, and
modular in nature so that new contributions can be easily inserted into an
existing assembly pipeline. This modular design will foster the development of
new assembly algorithms and allow the AMOS project to continually grow and
improve in hopes of eventually becoming a widely accepted and deployed assembly
infrastructure. In this sense, AMOS is both a design philosophy and a software
system.
Because of its modular nature, AMOS cannot be described in one paragraph since
it is a composite of many different systems. See the Pipeline section for quick
descriptions of each pipeline, or the Documentation section on where to find
comprehensive documentation.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%patch -P 17 -p1
%patch -P 18 -p1
%patch -P 19 -p1
%patch -P 20 -p1
%patch -P 21 -p1
%patch -P 22 -p1
%patch -P 23 -p1
%patch -P 24 -p1

%build
./configure  --prefix=%{installroot} --with-Boost-dir=/opt/bio/boost --enable-all --with-x --with-qmake-qt4=/usr/bin/qmake-qt4  PERL="/usr/bin/env perl" PYTHON="/usr/bin/env python" NUCMER=/opt/bio/MUMmer/bin/nucmer DELTAFILTER=/opt/bio/MUMmer/bin/delta-filter SHOWCOORDS=/opt/bio/MUMmer/bin/show-coords BLAT=/opt/bio/blat/bin/blat

# LIBSTATISTICS_DESCRIPTIVE_PERL
# LIBXML_PARSER_PERL
# LIBDBI_PERL
# --libdir=%{installroot}/lib

make 
make check

%install
mkdir -p %{buildroot}%{installroot}
make install prefix=%{buildroot}%{installroot}
chmod -x %{buildroot}%{installroot}/bin/*
rm -r %{buildroot}%{installroot}/include
rm %{buildroot}%{installroot}/lib/AMOS/*.a
rm -r %{buildroot}%{installroot}/share

%files
%defattr(755,root,root)
%{installroot}

# make all files in the bin directory executable in post section
%post 
chmod +x %{installroot}/bin/*
