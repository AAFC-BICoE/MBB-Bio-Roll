# This is a  spec file for O2DBI

### define _topdir	 	/home/rpmbuild/rpms/O2DBI
%define name		O2DBI
%define release		1
%define version 	1.24
%define installroot 	/opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	O2DBI tries to make a connection between two worlds: Object Oriented Programming and Relational Databases.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}.pm
Packager:	Zaky Adam <zaky.adam@grc.gc.ca>
URL:          	http://www.techfak.uni-bielefeld.de/~joern/dev/perl/o2dbi/o2dbi.html
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        Public Domain
AutoReq:	yes

%description
This tool reads an object definition and generates a database schema and Perl modules for storing data in a relational database, yet accessing the data in an object oriented fashion.

%prep
%setup -q -T -c -n O2DBI-1.24
cp ../../SOURCES/O2DBI.pm . 

%build


%install
mkdir -p %{buildroot}%{installroot}
cp -r * %{buildroot}%{installroot}

%files
%defattr(755,root,root)
%{installroot}
