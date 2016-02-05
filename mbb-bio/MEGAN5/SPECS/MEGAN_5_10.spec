### %define _topdir           /home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/MEGAN5
%define name              MEGAN
%define release           10
%define version           5
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
MEGAN ("MEtaGenome ANalyzer") is a computer program that allows optimized analysis of large metagenomic datasets.

Metagenomics is the analysis of the genomic sequences from a usually uncultured environmental sample. A large term goal of most metagenomics is to inventory and measure the extent and the role of microbial biodiversity in the ecosystem due to discoveries that the diversity of microbial organisms and viral agents in the environment is far greater than previously estimated. Tools that allow the investigation of very large data sets from environmental samples using shotgun sequencing techniques in particular, such as MEGAN, are designed to sample and investigate the unknown biodiversity of environmental samples where more precise techniques with smaller, better known samples, cannot be used.

Fragments of DNA from an metagenomics sample, such as ocean waters or soil, are compared against databases of known DNA sequences using BLAST or another sequence comparison tool to assemble the segments into discrete comparable sequences. MEGAN is then used to compare the resulting sequences with gene sequences from GenBank in NCBI. The program was used to investigate the DNA of a mammoth recovered from the Siberian permafrost and Sargasso Sea data set.

%prep
cp ../SOURCES/AAFC_license.txt  ../SOURCES/MEGAN_unix_5_10_5.sh .  
#%setup -n %{name}-%{version}

%build
printf "o\n1\n/home/rpmbuild/work/MBB-Bio-Roll/mbb-bio/MEGAN5/BUILD\ny\n1,2\nn\n5\n8000\nn" | sh MEGAN_unix_5_10_5.sh -c 

%install
mkdir -p $RPM_BUILD_ROOT%{installroot}
cp -r class  $RPM_BUILD_ROOT%{installroot}/
cp -r jars  $RPM_BUILD_ROOT%{installroot}/
cp -r tools  $RPM_BUILD_ROOT%{installroot}/
cp MEGAN  $RPM_BUILD_ROOT%{installroot}/
cp MEGAN.vmoptions  $RPM_BUILD_ROOT%{installroot}/
cp manual.pdf  $RPM_BUILD_ROOT%{installroot}/
cp AAFC_license.txt $RPM_BUILD_ROOT%{installroot}/
cp -r .install4j $RPM_BUILD_ROOT%{installroot}/
echo -e "MEGAN can take many options. Here I will only list a few essential ones to make it run. Please refer to the manual for any advanced usage.\nYou need to load the license on first run. You can do this by {MEGAN -L %{installroot}/AAFC_license.txt}.\nYou can run the command-line mode on a server by typing {xvfb-run --auto-servernum --server-num=1 MEGAN -g} (Note this is different from the manual which contains a typo).\nI've noticed that when running the above command MEGAN seems to forget about previously loaded licenses sometimes. To guarantee that it will work you can load the license again with the command you want to run. For example {xvfb-run --auto-servernum --server-num=1 MEGAN -L %{installroot}/AAFC_license.txt -g}.\nThe default mamimum memory allowed for MEGAN is set to be 8G. You can allow for more memory to make MEGAN run faster. You need to change the settings in MEGAN.vmoptions to do so. Please refer to the manual for more details.\n " > $RPM_BUILD_ROOT%{installroot}/00README.MBB
cd $RPM_BUILD_ROOT%{installroot}/
mkdir bin
mv MEGAN bin
mv .install4j bin
mv class bin
mv jars bin
mv tools bin

%files
%defattr(644,root,root,755)
%{installroot}
%defattr(755,root,root,755)
%{installroot}/bin
%attr(757,root,root) %{installroot}/MEGAN.vmoptions
