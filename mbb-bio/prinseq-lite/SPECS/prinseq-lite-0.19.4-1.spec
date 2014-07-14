# This is a  spec file for prinseq-lite
# The following rpm packages are required:
# perl-ExtUtils-Depends-0.302-1.el6.rf.noarch.rpm
# perl-ExtUtils-PkgConfig-1.12-1.el6.rf.noarch.rpm
# tslib-1.0-1.el6.rf.x86_64.rpm
# libvncserver-0.9.7-4.el6.x86_64.rpm
# directfb-1.2.4-1.el6.rf.x86_64.rpm
# perl-common-sense-3.0-1.el6.rf.x86_64.rpm
# xorg-x11-proto-devel-7.6-13.el6.noarch.rpm
# pkgconfig-0.23-9.1.el6.x86_64.rpm
# pixman-devel-0.18.4-1.el6_0.1.x86_64.rpm
# perl-JSON using yum
# perl( Statistics-PCA) via cpan
# perl (Mathc::Cephes) via cpan


### define _topdir	 	/home/rpmbuild/rpms/prinseq-lite
%define name		prinseq-lite
%define release		1
%define version 	0.19.4
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	prinseq-lite is a preprocessing and information of sequence data.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.gz
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://prinseq.sourceforge.net/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPL-3|http://sourceforge.net/projects/prinseq/files/	
AutoReq:	yes

%description
prinseq-lite can be used to filter, reformat, or trim your genomic and
metagenomic sequence data. It generates summary statistics of your sequences in
graphical and tabular format. It is easily configurable and provides a
user-friendly interface. The standalone lite version is written in Perl and does
not require any non-core Perl modules. The lite version is primarily designed
for data preprocessing and does not generate summary statistics in graphical
form.

%prep
%setup -q

%build
chmod 755 prinseq-lite.pl
chmod 755 prinseq-graphs.pl
mv prinseq-lite.pl prinseq-lite
mv prinseq-graphs.pl prinseq-graphs

%install
mkdir -p %{buildroot}%{installroot}
cp -r * %{buildroot}%{installroot}

%files
%defattr(755,root,root)
%{installroot}
