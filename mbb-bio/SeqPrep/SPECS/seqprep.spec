### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/SeqPrep
%define name SeqPrep
%define version 1.2
%define release 1
%define installroot       /opt/bio/%{name}

summary: SeqPrep is a program to merge paried end Illumina reads that are overlapping into a single longer read.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: v1.2.tar.gz
Patch0: patchfile.patch
Group: Development/Tools
License: MIT 
Vendor: Free Software Foundation, Inc. <http://fsf.org/>
Packager: Katherine Beaulieu <katherine.beaulieu@canada.ca>
Url: https://github.com/jstjohn/SeqPrep
AutoReq: yes
AutoProv: yes

%description
SeqPrep is a program to merge paired end Illumina reads that are overlapping into a single longer read.
%prep
%setup -q -n SeqPrep-1.2
cat Makefile
pwd
cp Makefile Makefile.old
rm Makefile
patch Makefile.old -i /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/SeqPrep/SOURCES/patchfile.patch -o Makefile
%build
make PREFIX=/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/SeqPrep/BUILD

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}

make PREFIX=/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/SeqPrep/BUILD install 
pwd
ls
cp SeqPrep $RPM_BUILD_ROOT/%{installroot}


%files 
%defattr(755,root,root,755)
%{installroot}

%clean

