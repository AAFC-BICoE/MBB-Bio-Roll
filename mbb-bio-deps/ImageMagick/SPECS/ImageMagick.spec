%define name		opt-ImageMagick
%define src_name	ImageMagick
%define release		1
%define version 	7.0.8.14
%define src_version 	7.0.8-14
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/%{src_name}
%define	_prefix		%{installroot}
%define _libdir		%{_prefix}/lib

BuildRoot:	%{buildroot}
Summary: 	Image processing library and utilities.
License:    	GPL
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{src_name}-v%{version}.tar.gz
Prefix: 	%{_prefix}
Group: 		Development/Tools
URL:		https://github.com/ImageMagick/ImageMagick
AutoReqProv:	yes
Packager:	Iyad Kandalaft <iyad.kandalaft@canada.ca>

BuildRequires:	opt-perl
Requires:	opt-perl

%global __provides_exclude ^perl
%global __requires_exclude ^perl

Provides:	opt-perl(Image::Magick)	= %{version}
Provides:	opt-perl(Image::Magick::Q16HDRI) = %{version}

Requires:	opt-perl(AutoLoader)
Requires:	opt-perl(Carp)
Requires:	opt-perl(DynaLoader)
Requires:	opt-perl(Exporter)
Requires:	opt-perl(Image::Magick::Q16HDRI)
Requires:	opt-perl(parent)
Requires:	opt-perl(strict)
Requires:	opt-perl(vars)

%description
Use ImageMagick® to create, edit, compose, or convert bitmap images. It can read and write images in a variety of formats (over 200) including PNG, JPEG, GIF, HEIC, TIFF, DPX, EXR, WebP, Postscript, PDF, and SVG. Use ImageMagick to resize, flip, mirror, rotate, distort, shear and transform images, adjust image colors, apply various special effects, or draw text, lines, polygons, ellipses and Bézier curves.

%prep
%setup -q -n %{src_name}-%{src_version}

%build
#./configure --prefix=%{_prefix} --enable-shared --disable-static --with-x --with-threads --with-gslib --with-rsvg --with-perl=/opt/perl/bin/perl --with-perl-options="CC='%__cc -L$PWD/magick/.libs' LDDLFLAGS='-shared -Wl,-rpath -Wl,%{_libdir} -L$PWD/PerlMagick/../MagickCore/.libs'"
./configure --prefix=%{_prefix} --enable-shared --disable-static --with-x --with-threads --with-gslib --with-rsvg --with-perl
make -j

%install
make install DESTDIR=%{buildroot}
# Building perl module indepdently because automated build fails to set RPATH correctly
cd PerlMagick
%{__perl} Makefile.PL
make install DESTDIR=%{buildroot} LD_RUN_PATH=%{_libdir}
chmod +w %{buildroot}/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi/auto/Image/Magick/*/*.so

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%{_includedir}
%{_datadir}
%config %{_prefix}/etc
%{perl_sitearch}/auto/Image/Magick
%{perl_sitearch}/Image/Magick.pm
%{perl_sitearch}/Image/Magick/*.pm
%defattr(755,root,root,755)
%{_bindir}
%{_libdir}
