#
# This SPEC file was automatically generated using the cpantorpm
# script.
#
#    Package:           opt-perl-Graph
#    Version:           0.9704
#    cpantorpm version: 1.08
#    Date:              Thu Oct 04 2018
#    Command:
# /opt/perl/bin/cpantorpm --add-require opt-perl --install-base /opt/perl --prefix opt-perl- --packager Rocks --spec-only Graph
#

Name:           opt-perl-Graph
Version:        0.9704
Release:        1%{?dist}
Summary:        unknown
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Graph/
BuildRoot:      /tmp/cpantorpm/Graph-0.9704-inst
BuildArch:      noarch
Source0:        http://search.cpan.org/authors/id/authors/id/J/JH/JHI/Graph-0.9704.tar.gz

#
# Unfortunately, the automatic provides and requires do NOT always work (it
# was broken on the very first platform I worked on).  We'll get the list
# of provides and requires manually (using the RPM tools if they work, or
# by parsing the files otherwise) and manually specify them in this SPEC file.
#

AutoReqProv:    no
AutoReq:        no
AutoProv:       no

Provides:       opt-perl(Graph) = 0.9704
Provides:       opt-perl(Graph::AdjacencyMap) = 0.9704
Provides:       opt-perl(Graph::AdjacencyMap::Heavy) = 0.9704
Provides:       opt-perl(Graph::AdjacencyMap::Light) = 0.9704
Provides:       opt-perl(Graph::AdjacencyMap::Vertex) = 0.9704
Provides:       opt-perl(Graph::AdjacencyMatrix) = 0.9704
Provides:       opt-perl(Graph::Attribute) = 0.9704
Provides:       opt-perl(Graph::BitMatrix) = 0.9704
Provides:       opt-perl(Graph::Directed) = 0.9704
Provides:       opt-perl(Graph::MSTHeapElem) = 0.9704
Provides:       opt-perl(Graph::Matrix) = 0.9704
Provides:       opt-perl(Graph::SPTHeapElem) = 0.9704
Provides:       opt-perl(Graph::TransitiveClosure) = 0.9704
Provides:       opt-perl(Graph::TransitiveClosure::Matrix) = 0.9704
Provides:       opt-perl(Graph::Traversal) = 0.9704
Provides:       opt-perl(Graph::Traversal::BFS) = 0.9704
Provides:       opt-perl(Graph::Traversal::DFS) = 0.9704
Provides:       opt-perl(Graph::Undirected) = 0.9704
Provides:       opt-perl(Graph::UnionFind) = 0.9704
Provides:       opt-perl(Heap071::Elem) = 0.9704
Provides:       opt-perl(Heap071::Fibonacci) = 0.9704
Requires:       opt-perl
Requires:       opt-perl(List::Util)
Requires:       opt-perl(Math::Complex)
Requires:       opt-perl(Safe)
Requires:       opt-perl(Scalar::Util)
Requires:       opt-perl(Test::More)
BuildRequires:  opt-perl
BuildRequires:  opt-perl(ExtUtils::MakeMaker)
BuildRequires:  opt-perl(List::Util)
BuildRequires:  opt-perl(Math::Complex)
BuildRequires:  opt-perl(Safe)
BuildRequires:  opt-perl(Scalar::Util)
BuildRequires:  opt-perl(Test::More)
Requires:       opt-perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A perl module

%prep

%setup  -n Graph-0.9704
chmod -R u+w %{_builddir}/Graph-%{version}

if [ -f pm_to_blib ]; then rm -f pm_to_blib; fi

%build

%{__perl} Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS" INSTALLDIRS=site SITEPREFIX=/opt/perl INSTALLSITEARCH=/opt/perl/lib/site_perl/5.26.0/x86_64-linux-thread-multi INSTALLSITELIB=/opt/perl/lib/site_perl/5.26.0 INSTALLSITEBIN=/opt/perl/bin INSTALLSITESCRIPT=/opt/perl/bin INSTALLSITEMAN1DIR=/opt/perl/man/man1 INSTALLSITEMAN3DIR=/opt/perl/man/man3 INSTALLSCRIPT=/opt/perl/bin
make %{?_smp_mflags}

#
# This is included here instead of in the 'check' section because
# older versions of rpmbuild (such as the one distributed with RHEL5)
# do not do 'check' by default.
#

if [ -z "$RPMBUILD_NOTESTS" ]; then
   make test
fi

%install

rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%clean

rm -rf $RPM_BUILD_ROOT

%files

%defattr(-,root,root,-)
/opt/perl/lib/site_perl/5.26.0/*
/opt/perl/man/man3/*

%changelog
* Thu Oct 04 2018 Rocks 0.9704-1
- Generated using cpantorpm
