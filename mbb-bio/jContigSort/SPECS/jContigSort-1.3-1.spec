# This is a  spec file for jContigSort

### define _topdir	 	/home/rpmbuild/rpms/jContigSort
%define name		jContigSort
%define release		1
%define version 	bin_1_3
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	jContigSort is an easy and rapid ordering contigs software.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}_%{version}.zip
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:            http://sourceforge.net/p/jcontigsort/home/jContigSort/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        BSD
AutoReq:	yes

%description
jContigSort is an easy and rapid ordering contigs software. jContigSort can be
used to order contigs based on a  reference genome. It generates summary
statistics of your contigs sequences log files. It is easily configurable and
provides a user-friendly interface.

%prep
%setup -q -c -n jContigSort

%build
#jars already built 

%install
mkdir -p %{buildroot}%{installroot}
cp -r * %{buildroot}%{installroot}

%files
%defattr(644,root,root,755)
%{installroot}

