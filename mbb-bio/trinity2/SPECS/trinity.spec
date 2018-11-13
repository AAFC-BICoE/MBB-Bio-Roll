%define name		trinity2
%define src_name	trinityrnaseq
%define release		1
%define version 	2.8.4
%define	buildroot   %{_topdir}/%{name}-%{version}-root
%define installroot /opt/bio/%{name}
%define _prefix     %{installroot}

BuildRoot:	%{buildroot}
Summary: 	RNA-Seq De novo Assembly
License:    Open Source, MIT-like
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{src_name}-%{version}.tar.gz
Packager:	Glen Newton <glen.newton@grc.gc.ca>
URL:        http://trinityrnaseq.github.io/
Prefix: 	%{_prefix}
Group: 		BioInformatics/Assembler
AutoReq:	yes

Patch0:     makeversion.patch
Patch1:     env-perl.patch


%global         __requires_exclude ^perl
%global         __provides_exclude ^perl
Provides: 	opt-perl(CanvasXpress::Line)
Provides: 	opt-perl(Bio::AlignIO
Provides: 	opt-perl(Bio::Assembly::IO
Provides: 	opt-perl(Bio::Coordinate::Pair
Provides: 	opt-perl(Bio::DB::GFF::Util::Rearrange
Provides: 	opt-perl(Bio::DB::SeqFeature::Store)
Provides: 	opt-perl(Bio::Location::Simple)
Provides: 	opt-perl(Bio::Root::Version)
Provides: 	opt-perl(Bio::SearchIO)
Provides: 	opt-perl(Bio::SeqFeature::Generic)
Provides: 	opt-perl(Bio::SeqIO)
Provides: 	opt-perl(Bio::Tools::CodonTable)
Provides: 	opt-perl(Bio::Tools::GuessSeqFormat)
Provides: 	opt-perl(Bio::TreeIO)

%description
Trinity, developed at the Broad Institute and the Hebrew University of Jerusalem, represents a novel method for the efficient and robust de novo reconstruction of transcriptomes from RNA-seq data. Trinity combines three independent software modules: Inchworm, Chrysalis, and Butterfly, applied sequentially to process large volumes of RNA-seq reads. Trinity partitions the sequence data into many individual de Bruijn graphs, each representing the transcriptional complexity at at a given gene or locus, and then processes each graph independently to extract full-length splicing isoforms and to tease apart transcripts derived from paralogous genes.

%prep
echo "prep..."
%setup -qn %{src_name}-Trinity-v%{version}
%patch0 -p 1
%patch1 -p 1

%build
echo "build..."
make 

make plugins

%install
echo "install..."
# remove some files and directories that should not be packaged...
rm -fr bioconda_recipe/ Docker/ trinity_ext_sample_data/ trinityrnaseq.wiki/ __pull_trinity_ext_sample_data.sh

mkdir -p %{buildroot}%{installroot}
cp -r * %{buildroot}%{installroot}

%files
%defattr(644,root,root,755)
%dir %{_prefix}
%doc LICENSE LICENSE.txt README
%defattr(755,root,root,755)
%{_prefix}

# make all files in the bin directory executable in post section
# ensure text file are not executable
# create /bin/Trinity2 workaround
%post 
chmod +x %{installroot}/Trinity %{installroot}/util/support_scripts %{installroot}/util/misc
chmod -x %{installroot}/LICENSE %{installroot}/LICENSE.txt %{installroot}/Makefile %{installroot}/notes %{installroot}/README %{installroot}/README.md 
mkdir -p %{installroot}/bin
echo '#/bin/bash' > %{installroot}/bin/Trinity2
echo 'pushd `dirname $0` > /dev/null' >> %{installroot}/bin/Trinity2
echo 'SCRIPTPATH=`pwd -P`' >> %{installroot}/bin/Trinity2
echo 'popd > /dev/null' >> %{installroot}/bin/Trinity2
echo '$SCRIPTPATH/../Trinity $@' >> %{installroot}/bin/Trinity2
chmod +x %{installroot}/bin/Trinity2

%postun
# the package leaves some extraneous file around. clean them up.
rm -fr  %{installroot}/
