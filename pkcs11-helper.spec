%define major 1

Summary:	A library that simplifies the interaction with PKCS#11
Name:		pkcs11-helper
Version:	1.10
Release:	7
License:	GPLv2
Group:		System/Libraries
Url:		http://www.opensc-project.org
Source0:	http://www.opensc-project.org/files/pkcs11-helper/%{name}-%{version}.tar.bz2
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
%setup -q

%build
%configure2_5x \
	--disable-debug \
	--disable-static

%make
										
%install
%makeinstall_std

