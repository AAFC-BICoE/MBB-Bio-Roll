# This is a  spec file for velvet

%define name		FastOrtho
%define release		1
%define version 	1
%define installroot /opt/bio/%{name}

BuildRoot:	%{buildroot}
Summary: 	FastOrtho
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Packager:	Glen Newton glen.newton@agr.gc.ca
Source: 	%{name}.zip
URL:            http://enews.patricbrc.org/fastortho/
Prefix: 	/opt/bio
Group: 		Development/Tools
License:        GPL-3
AutoReq:	yes

%description


%prep
%setup -q -n FastOrtho


%build
cd src
sed -i s/enable-auto-import/-enable-auto-import/g Makefile
make --jobs=`nproc`
strip FastOrtho


%install
mkdir -p %{buildroot}%{installroot}

cp src/FastOrtho SetFast.jar %{buildroot}%{installroot}

%files
%defattr(755,root,root,755)
%{installroot}
%defattr(644,root,root,755)


