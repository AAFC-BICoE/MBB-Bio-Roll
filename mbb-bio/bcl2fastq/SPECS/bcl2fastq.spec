### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/bcl2fastq
%define name bcl2fastq
%define version 2.17
%define release 1
%define installroot       /opt/bio/%{name}

summary: The main task of bcl2fastq is to convert the base calls in the per-cycle BCL files to the per-read FASTQ format. Usually, this task involves a simple conversion for each base.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: bcl2fastq2-v2.17.1.14.tar.gz
Group: Development/Tools
License: MIT
Vendor: Joe Brown <joe.brown@pnnl.gov>
Packager: Alex MacLean <alex.maclean@agr.gc.ca>
Url: https://github.com/brwnj/bcl2fastq
AutoReq: yes
AutoProv: yes

%description
The main task of bcl2fastq is to convert the base calls in the per-cycle BCL files to the
per-read FASTQ format. Usually, this task involves a simple conversion for each base.

%prep
%setup -q -n bcl2fastq

%build
mkdir ../{build,install}
cd ../build
../bcl2fastq/src/configure --prefix=/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/bcl2fastq/BUILD/install
make

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cd ../build
make install
cp -r ../install/* $RPM_BUILD_ROOT%{installroot}

%files 
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/lib
