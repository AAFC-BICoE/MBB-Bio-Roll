### %define _topdir     /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/matplotlib
%define name            matplotlib
%define release		1         
%define version         1.5.1  
%define installroot     /opt/bio/lib/%{name}

Summary:   matplotlib is a python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    %{name}-%{version}.tar.gz
License:   PSF
Packager:  Alex MacLean <alex.maclean@agr.gc.ca>
Group:     Development/Libraries
Vendor:    Hunter, J. D.
Url:       http://matplotlib.org/index.html
AutoReq:   yes
AutoProv:  yes

%description
matplotlib is a python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. matplotlib can be used in python scripts, the python and ipython shell (ala MATLAB or Mathematica), web application servers, and six graphical user interface toolkits.

%prep
%setup -q 

%build
python setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
mkdir -p ../install/lib/python2.7/site-packages
export PYTHONPATH=$PYTHONPATH:/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/matplotlib/BUILD/install/lib/python2.7/site-packages/
python setup.py install --prefix=/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/matplotlib/BUILD/install
cp -r ../install/bin ../install/lib $RPM_BUILD_ROOT%{installroot}

%clean

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%{installroot}/lib
