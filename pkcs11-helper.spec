
Name: pkcs11-helper
Version: 1.05
Release: %mkrel 1
Summary: A library that simplifies the interaction with PKCS#11
License: GPL
Group: System/Libraries
URL: http://www.opensc-project.org
Source: http://www.opensc-project.org/files/pkcs11-helper/%{name}-%{version}.tar.bz2
BuildRequires: pkgconfig
BuildRequires: openssl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
pkcs11-helper is a library that simplifies the interaction with PKCS#11
providers for end-user applications.

#-------------------------------------------------------------

%define libname %mklibname pcks11-helper 1

%package -n %{libname}
Summary: Dynamic libraries from %name
Group: System/Libraries

%description -n %{libname}
Dynamic libraries from %name.

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_docdir}/pkcs11-helper
%{_libdir}/*.so.*

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
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
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
rm -rf %buildroot

%makeinstall_std

%clean
rm -rf %buildroot

