%define major 1

Name: pkcs11-helper
Version: 1.10
Release: 1
Summary: A library that simplifies the interaction with PKCS#11
License: GPL
Group: System/Libraries
URL: http://www.opensc-project.org
Source0: http://www.opensc-project.org/files/pkcs11-helper/%{name}-%{version}.tar.bz2
BuildRequires: pkgconfig
BuildRequires: openssl-devel

%description
pkcs11-helper is a library that simplifies the interaction with PKCS#11
providers for end-user applications.

#-------------------------------------------------------------

%define libname %mklibname pcks11-helper %{major}

%package -n %{libname}
Summary: Dynamic libraries from %name
Group: System/Libraries

%description -n %{libname}
Dynamic libraries from %name.

%files -n %{libname}
%{_docdir}/pkcs11-helper
%{_libdir}/*.so.%{major}*

#-------------------------------------------------------------

%define develname %mklibname -d %{name}

%package -n %{develname}
Summary: Header files and static libraries from %name
Group: Development/C
Requires: %{libname} = %{version}
Provides: pkcs11-helper-devel
Provides: libpkcs11-helper-devel = %version

%description -n %{develname}
Libraries and includes files for developing programs based on %name.

%files -n %{develname}
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
