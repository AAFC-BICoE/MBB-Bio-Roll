%define name		opt-curl
%define src_name	curl
%define release		2
%define version		7.29.0
%define buildroot 	%{_topdir}/%{name}-%{version}-root
%define installroot 	/opt/bio/lib/%{src_name}
%define _prefix		%{installroot}
%define _mandir		%{installroot}/share/man
%define _defaultdocdir	%{installroot}/share/docs

BuildRoot:	%{buildroot}
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{src_name}-%{version}.tar.gz
Prefix: 	%{installroot}

Summary: A utility for getting files from remote servers (FTP, HTTP, and others)
License: MIT
Group: Applications/Internet
Provides: opt-webclient
URL: http://curl.haxx.se/
BuildRequires: groff
BuildRequires: krb5-devel
BuildRequires: libidn-devel
# Not building with support for ssh or nss
#BuildRequires: libssh2-devel
#BuildRequires: nss-devel
BuildRequires: openldap-devel
BuildRequires: openssh-clients
BuildRequires: openssh-server
BuildRequires: pkgconfig
BuildRequires: stunnel
BuildRequires: zlib-devel

Requires: opt-libcurl = %{version}-%{release}

# require at least the version of libssh2 that we were built against,
# to ensure that we have the necessary symbols available (#525002, #642796)
#%global libssh2_version %(pkg-config --modversion libssh2 2>/dev/null || echo 0)

%description
curl is a command line tool for transferring data with URL syntax, supporting
FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, IMAP,
SMTP, POP3 and RTSP.  curl supports SSL certificates, HTTP POST, HTTP PUT, FTP
uploading, HTTP form based upload, proxies, cookies, user+password
authentication (Basic, Digest, NTLM, Negotiate, kerberos...), file transfer
resume, proxy tunneling and a busload of other useful tricks. 

%package -n opt-libcurl
Summary: A library for getting files from web servers
Group: Development/Libraries

%description -n opt-libcurl
libcurl is a free and easy-to-use client-side URL transfer library, supporting
FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, IMAP,
SMTP, POP3 and RTSP. libcurl supports SSL certificates, HTTP POST, HTTP PUT,
FTP uploading, HTTP form based upload, proxies, cookies, user+password
authentication (Basic, Digest, NTLM, Negotiate, Kerberos4), file transfer
resume, http proxy tunneling and more.

%package -n opt-libcurl-devel
Summary: Files needed for building applications with libcurl
Group: Development/Libraries
Requires: opt-libcurl = %{version}-%{release}
Provides: opt-curl-devel = %{version}-%{release}

%description -n opt-libcurl-devel
The libcurl-devel package includes header files and libraries necessary for
developing programs which use the libcurl library. It contains the API
documentation of the library, too.

%prep
#echo %{_prefix}
#echo %{_mandir}
#echo %{_libdir}
#exit 1
%setup -q -n %{src_name}-%{version}

%build
[ -x /usr/kerberos/bin/krb5-config ] && KRB5_PREFIX="=/usr/kerberos"

%configure \
    --enable-hidden-symbols \
    --enable-ipv6 \
    --enable-ldaps \
    --enable-manual \
    --enable-threaded-resolver \
    --with-ca-bundle=%{_sysconfdir}/pki/tls/certs/ca-bundle.crt \
    --with-gssapi${KRB5_PREFIX} \
    --with-libidn  

# Remove bogus rpath
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install

rm -f %{_libdir}/libcurl.la

install -d ${RPM_BUILD_ROOT}%{_datadir}/aclocal
install -m 644 docs/libcurl/libcurl.m4 ${RPM_BUILD_ROOT}%{_datadir}/aclocal

# drop man page for a script we do not distribute
rm -f ${RPM_BUILD_ROOT}%{installroot}%{_mandir}/man1/mk-ca-bundle.1

# Make libcurl-devel multilib-ready (bug #488922)
%if 0%{?__isa_bits} == 64
%define _curlbuild_h curlbuild-64.h
%else
%define _curlbuild_h curlbuild-32.h
%endif
cp ${RPM_BUILD_ROOT}%{_includedir}/curl/curlbuild.h \
   ${RPM_BUILD_ROOT}%{_includedir}/curl/%{_curlbuild_h}


%files
%defattr(-,root,root,-)
%doc CHANGES 
%doc README* 
%doc COPYING
%doc docs/BUGS 
%doc docs/FAQ 
%doc docs/FEATURES
%doc docs/MANUAL 
%doc docs/RESOURCES
%doc docs/TheArtOfHttpScripting 
%doc docs/TODO
%{_bindir}/curl
%{_mandir}/man1/curl.1*

%files -n opt-libcurl
%defattr(-,root,root,-)
%{_libdir}/libcurl.so.*

%files -n opt-libcurl-devel
%defattr(-,root,root,-)
%doc docs/examples/*.c 
%doc docs/examples/Makefile.example 
%doc docs/INTERNALS
%doc docs/CONTRIBUTE 
%doc docs/libcurl/ABI
%{_bindir}/curl-config*
%{_includedir}/curl
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/curl-config.1*
%{_libdir}/libcurl.*
%{_datadir}/aclocal/libcurl.m4
