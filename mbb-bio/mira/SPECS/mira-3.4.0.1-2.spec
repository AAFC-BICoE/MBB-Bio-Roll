# This is a  spec file for mira genome assembler

### define _topdir	 	/home/rpmbuild/rpms/mira
%define name		mira
%define release		2
%define version 	3.4.0.1
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary:        MIRA 3 is  Whole Genome Shotgun and EST Sequence Assembler for Sanger, 454 and Solexa / Illumina
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.bz2
URL:            http://www.chevreux.org/projects_mira.html
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GNU GPL
AutoReq:	yes

%description
MIRA 3 is able to perform true hybrid de-novo assemblies using reads gathered
through Sanger, 454 or Solexa sequencing technologies. That is, it assembles
reads instead of a mix of (eventually shredded) shredded consensus sequence and
reads. See an example on how it looks like for Sanger and 454, but it also
works with Sanger/Solexa or 454/Solexa or Sanger/454/Solexa. The length of the
Solexa sequences is not restricted, they can be 36mers to 150mers or more.  An
often used combination of current sequencing technologies is a mix of de-novo
454 assembly and Solexa mapping assemblies: 454 to get long contigs built,
Solexa to get rid of the pesky 454 homopolymer problems. Here's the recipe I
use for sequencing a bacterium de-novo and almost perfectly for comparatively
little money:
 

%prep
%setup -q

%build
./configure --with-boost=/opt/bio/boost
make

%install
make install prefix=$RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root)
%{installroot}
