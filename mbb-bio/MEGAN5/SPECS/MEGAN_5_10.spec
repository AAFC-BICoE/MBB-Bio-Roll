### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/MEGAN5
%define name              MEGAN
%define release           10
%define version           5
#%define buildroot         %{_topdir}/%{name}-%{version}-root
%define installroot       /opt/bio/%{name}


Summary:   MEGAN5 is a program that allows optimized analysis of large metagenomic datasets.
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source:    MEGAN_unix_5_10_5.sh 
License:   Free academic use but not open source
Packager:  Xie Qiu <xie.qiu@agr.gc.ca>
Group:     Development/Tools
#BuildRoot: %{buildroot}
Prefix:    /opt/bio
Vendor:    D.H. Huston, S.C. Schuster, S. Mitra, D.C. Richter, P.Rupek, J.-J Ruscheweyh, R. Tappu, N. Weber
Url:       http://ab.inf.uni-tuebingen.de/software/megan5/
AutoReq:   yes

%description
djahdjkhajkdhjadhjad

%prep
#echo "pppp"
cp ../SOURCES/shellargs.txt ../SOURCES/MEGAN_unix_5_10_5.sh .  
#%setup -n %{name}-%{version}

%build
cat shellargs.txt | sh MEGAN_unix_5_10_5.sh -c

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r jars/  License.txt manual.pdf tools  $RPM_BUILD_ROOT%{installroot}/

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/tools
%{installroot}/jars/

