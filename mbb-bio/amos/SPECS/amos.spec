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
Patch0:         getopt.patch
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>
URL:            http://sourceforge.net/apps/mediawiki/amos/index.php?title=AMOS
Prefix: 	%{installroot}
Group: 		BioInformatics/Assembler
License:        Artistic License
AutoReq:	yes

Requires:	opt-perl
Requires:	MUMmer
Requires:	wgs
Requires:	blat

Requires:	opt-perl(Cwd)
Requires:	opt-perl(DBI)
Requires:	opt-perl(Exporter)
Requires:	opt-perl(Fcntl)
Requires:	opt-perl(File::Basename)
Requires:	opt-perl(File::Spec)
Requires:	opt-perl(FileHandle)
Requires:	opt-perl(Getopt::Long)
Requires:	opt-perl(IO::File)
Requires:	opt-perl(IO::Handle)
Requires:	opt-perl(POSIX)
Requires:	opt-perl(Statistics::Descriptive)
Requires:	opt-perl(Sys::Hostname)
Requires:	opt-perl(XML::Parser)
Requires:	opt-perl(lib)
Requires:	opt-perl(strict)
Requires:	opt-perl(vars)
Requires:	opt-perl(warnings)

%global __requires_exclude ^perl

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
%patch0 -p1

%build
./configure --prefix=%{installroot} --enable-all --with-x --with-qmake-qt4=/usr/bin/qmake-qt4  PERL="/usr/bin/env perl" PYTHON="/usr/bin/env python" NUCMER=/opt/bio/MUMmer/bin/nucmer DELTAFILTER=/opt/bio/MUMmer/bin/delta-filter SHOWCOORDS=/opt/bio/MUMmer/bin/show-coords BLAT=/opt/bio/blat/bin/blat

# LIBSTATISTICS_DESCRIPTIVE_PERL
# LIBXML_PARSER_PERL
# LIBDBI_PERL
# --libdir=%{installroot}/lib

make -pipe --jobs=`nproc`
make check

%install
mkdir -p %{buildroot}%{installroot}
make install DESTDIR=%{buildroot}

%files
%defattr(0644,root,root,0755)
%dir %{installroot}
%{installroot}/include
%{installroot}/lib
%{installroot}/share
%defattr(0755,root,root,0755)
%{installroot}/bin
