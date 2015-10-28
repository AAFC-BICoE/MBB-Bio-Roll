### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/ruffus
%define name ruffus
%define version 2.6
%define release 3
%define installroot       /opt/bio/lib/%{name}

Summary: Ruffus is a Computation Pipeline library for python. It is open-sourced, powerful and user-friendly, and widely used in science and bioinformatics.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: master.zip
Group: Development/Libraries
Prefix: /opt/bio/lib
License: MIT
Vendor: Leo Goodstadt <ruffus_lib@llew.org.uk>
Packager:  Xie Qiu <xie.qiu@agr.gc.ca>
Url: http://www.ruffus.org.uk/
AutoReq:   yes

%description
The Ruffus module is a lightweight way to add support for running computational pipelines.

Computational pipelines are often conceptually quite simple, especially if we breakdown the process into simple stages, or separate tasks.

Each stage or task in a computational pipeline is represented by a python function Each python function can be called in parallel to run multiple jobs.

Ruffus was originally designed for use in bioinformatics to analyse multiple genome data sets.


%prep
%setup -q -n ruffus-master

%build
python setup.py build

%install
python setup.py install --prefix=%{installroot} --root=$RPM_BUILD_ROOT 

%files 
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
#%{installroot}/bin
%{installroot}/lib
