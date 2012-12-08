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


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.07-4mdv2011.0
+ Revision: 667777
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.07-3mdv2011.0
+ Revision: 607177
- rebuild

* Tue Apr 06 2010 Funda Wang <fwang@mandriva.org> 1.07-2mdv2010.1
+ Revision: 531982
- rebuild for new openssl

* Tue Jan 12 2010 Emmanuel Andry <eandry@mandriva.org> 1.07-1mdv2010.1
+ Revision: 490356
- New version 1.07
- use major

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.05-3mdv2010.0
+ Revision: 426709
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.05-2mdv2009.0
+ Revision: 224971
- rebuild
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Nov 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2008.1
+ Revision: 111206
- new version

* Fri Aug 10 2007 Helio Chissini de Castro <helio@mandriva.com> 1.03-1mdv2008.0
+ Revision: 61662
- First release of this packages, now required by new qca2-plugins
- import pkcs11-helper-1.03-1mdv2008.0


