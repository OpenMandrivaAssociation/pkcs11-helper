%define major 1

Summary:	A library that simplifies the interaction with PKCS#11
Name:		pkcs11-helper
Version:	1.30.0
Release:	1
License:	GPLv2
Group:		System/Libraries
Url:		https://github.com/OpenSC/pkcs11-helper
Source0:	https://github.com/OpenSC/pkcs11-helper/archive/%{name}-%{name}-%{version}.tar.gz
# https://github.com/OpenSC/pkcs11-helper/pull/4
Patch0:         pkcs11-helper-rfc7512.patch
#Patch1:		pkcs11-helper-openssl3.patch
BuildRequires:	pkgconfig(openssl)

%description
pkcs11-helper is a library that simplifies the interaction with PKCS#11
providers for end-user applications.

#-------------------------------------------------------------

%define libname %mklibname pkcs11-helper %{major}

%package -n %{libname}
Summary:	Dynamic libraries from %name
Group:		System/Libraries
%rename		%{_lib}pcks11-helper1

%description -n %{libname}
Dynamic libraries from %name.

%files -n %{libname}
%{_docdir}/pkcs11-helper
%{_libdir}/libpkcs11-helper.so.%{major}*

#-------------------------------------------------------------

%define devname %mklibname -d %{name}

%package -n %{devname}
Summary:	Header files and static libraries from %name
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Libraries and includes files for developing programs based on %name.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man8/*
%{_datadir}/aclocal/*

#-------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}
autoreconf -fiv
%configure \
	--disable-debug \
	--disable-static \
	--disable-crypto-engine-nss


%build
%make_build

%install
%make_install
