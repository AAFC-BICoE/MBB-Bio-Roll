%define name		MEGAN5
%define src_name	MEGAN
%define release		1
%define version		5.11.3
%define src_version	5_11_3
%define installroot	/opt/bio/%{name}
%define _prefix		%{installroot}
%define __jar_repack	%{nil}

Summary:	MEGAN5 is a program that allows optimized analysis of large metagenomic datasets.
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{src_name}_unix_%{src_version}.sh 
Source1:	AAFC_license.txt 
License:	Free academic use but not open source
Packager:	Xie Qiu <xie.qiu@agr.gc.ca>
Group:		Bioinformatics/Metagenomics
BuildRoot:	%{buildroot}
Prefix:		%{_prefix}
Vendor:		D.H. Huston, S.C. Schuster, S. Mitra, D.C. Richter, P.Rupek, J.-J Ruscheweyh, R. Tappu, N. Weber
Url:		http://ab.inf.uni-tuebingen.de/software/megan5/
AutoReq:	yes

%description
MEGAN ("MEtaGenome ANalyzer") is a computer program that allows optimized analysis of large metagenomic datasets.

Metagenomics is the analysis of the genomic sequences from a usually uncultured environmental sample. A large term goal of most metagenomics is to inventory and measure the extent and the role of microbial biodiversity in the ecosystem due to discoveries that the diversity of microbial organisms and viral agents in the environment is far greater than previously estimated. Tools that allow the investigation of very large data sets from environmental samples using shotgun sequencing techniques in particular, such as MEGAN, are designed to sample and investigate the unknown biodiversity of environmental samples where more precise techniques with smaller, better known samples, cannot be used.

Fragments of DNA from an metagenomics sample, such as ocean waters or soil, are compared against databases of known DNA sequences using BLAST or another sequence comparison tool to assemble the segments into discrete comparable sequences. MEGAN is then used to compare the resulting sequences with gene sequences from GenBank in NCBI. The program was used to investigate the DNA of a mammoth recovered from the Siberian permafrost and Sargasso Sea data set.

%prep
cp %{SOURCE0} .  

%build

%install
printf "o\n1\n%{buildroot}%{_prefix}\n1,2\nn\n5\n128000\nn" | sh %{src_name}_unix_%{src_version}.sh -c 
cp %{SOURCE1} %{buildroot}%{_prefix}
rm %{buildroot}%{_prefix}/.install4j/{*.log,response.varfile,install.prop}
echo -e "
MEGAN is provided for academic use only.  Please refer to the license for your specific use case.

AAFC BICoE is provided a license for academic use that you can use to run MEGAN5. You can do this by:
MEGAN -L %{installroot}/AAFC_license.txt}.

If you want to run MEGAN without a GUI, you can run the command-line mode by:
xvfb-run --auto-servernum --server-num=1 MEGAN -L %{installroot}/AAFC_license.txt -g

The default maximum memory allowed for MEGAN is set to be 128GB. You can allow for less or more memory to make MEGAN run more optimally by changing the settings in MEGAN.vmoptions to do so." > %{buildroot}%{_prefix}/README

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc %{_prefix}/License.txt
%doc %{_prefix}/manual.pdf
%{_prefix}/README
%{_prefix}/class
%{_prefix}/jars
%{_prefix}/tools
%{_prefix}/MEGAN.vmoptions
%{_prefix}/.install4j
%{_prefix}/AAFC_license.txt
%defattr(755,root,root,755)
%{_prefix}/MEGAN
