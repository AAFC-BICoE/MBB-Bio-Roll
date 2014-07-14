# This is a  spec file for maqview

### define _topdir	 	/home/rpmbuild/rpms/maqview
%define name		maqview
%define release		2
%define version 	0.2.5
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	Maqview is graphical read alignment viewer.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
Patch0:		%{name}-%{version}-%{release}.patch0
Patch1:         %{name}-%{version}-%{release}.patch1
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://maq.sourceforge.net/maqview.shtml
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GNU GPL
AutoReq:	yes

%description
Maqview is graphical read alignment viewer. It is specifically designed for the
Maq alignment file and allows you to see the mismatches, base qualities and
mapping qualities. Maqview is nothing fancy as Consed or GAP, but just a simple
viewer for you to see what happens in a particular region.
In comparison to tgap-maq, the text-based read alignment viewer writen by James
Bonfield, Maqview is faster and takes up much less memory and disk space in
indexing. This is possibly because tgap aims to be a general-purpose viewer but
Maqview fully makes use of the fact that a Maq alignment file has already been
sorted. Maqview is also efficient in viewing and provides a command-line tool to
quickly retrieve any region in a Maq alignment file.

%prep
%setup -q -n maqview
%patch -P 0 -p1
%patch -P 1 -p1

%build
./autogen.sh
./configure CPPFLAGS="-I/usr/include/GL" LDFLAGS="-L/usr/lib64"
make

%install
mkdir -p %{buildroot}%{installroot}
cp maqindex MaqIndex.pm maqindex_socket.pl maqindex_socks maqview zrio %{buildroot}%{installroot}
chmod -x %{buildroot}%{installroot}/maqindex_socket.pl

%files
%defattr(755,root,root)
%{installroot}
%defattr(644,root,root)
%{installroot}/MaqIndex.pm

# make maqindex_socket.pl executable in post section
%post 
chmod +x %{installroot}/maqindex_socket.pl
