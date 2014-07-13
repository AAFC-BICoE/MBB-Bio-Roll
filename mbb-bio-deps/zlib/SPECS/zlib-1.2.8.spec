# This is a sample spec file for wget

### define _topdir	 	/home/rpmbuild/rpms/%{name}
%define name			zlib
%define src_name		zlib
%define release		1
%define version 	1.2.8
%define buildroot %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	A Massively Spiffy Yet Delicately Unobtrusive Compression Library
License: 		{"licenses": [{"name": "MIT", "url": "https://svn.osgeo.org/gdal/tags/1.11.0/gdal/LICENSE.TXT"},{"name": "Others", "url": "https://svn.osgeo.org/gdal/tags/1.11.0/gdal/LICENSE.TXT"}]}
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{src_name}-%{version}.tar.gz
Prefix: 		/opt/bio
Group: 			Libraries/Compression
URL:			http://www.zlib.net/
AutoReq:		yes

%description
zlib is designed to be a free, general-purpose, legally unencumbered -- that is, not covered by any patents -- lossless data-compression library for use on virtually any computer hardware and operating system. The zlib data format is itself portable across platforms. Unlike the LZW compression method used in Unix compress(1) and in the GIF image format, the compression method currently used in zlib essentially never expands the data. (LZW can double or triple the file size in extreme cases.) zlib's memory footprint is also independent of the input data and can be reduced, if necessary, at some cost in compression. A more precise, technical discussion of both points is available on another page.
zlib was written by Jean-loup Gailly (compression) and Mark Adler (decompression). Jean-loup is also the primary author/maintainer of gzip(1), the author of the comp.compression FAQ list and the former maintainer of Info-ZIP's Zip; Mark is also the author of gzip's and UnZip's main decompression routines and was the original author of Zip. Not surprisingly, the compression algorithm used in zlib is essentially the same as that in gzip and Zip, namely, the "deflate" method that originated in PKWARE's PKZIP 2.x.



%prep
%setup -q

%build
./configure --prefix=/opt/bio/gdal
make prefix=%{installroot}

%install
make install prefix=$RPM_BUILD_ROOT%{installroot}

%files
%defattr(755,root,root,755)
%{installroot}
