%define	major 4
%define libname %mklibname ruli %{major}
%define develname %mklibname ruli -d

Summary:	The RULI (Resolver User Layer Interface) library
Name:		ruli
Version:	0.36
Release:	6
License:	BSD
Group:		System/Libraries
URL:		https://www.nongnu.org/ruli/
Source0:	http://savannah.nongnu.org/download/ruli/ruli_%{version}.orig.tar.gz
Source2:	http://savannah.nongnu.org/download/ruli/ruli_%{version}.orig.tar.gz.sig
Patch0:		ruli-0.35-optflags.diff
Patch1:		ruli-0.36-format_not_a_string_literal_and_no_format_arguments.diff
BuildRequires:	oop-devel
BuildConflicts:	%{name}-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
RULI stands for Resolver User Layer Interface. It's a library
built on top of an asynchronous DNS stub resolver. RULI provides
an easy-to-use interface for querying DNS SRV resource records.
The goal is to promote the wide deployment of SRV-cognizant
software. RULI aims to fully support SRV-related standards. There
are bindings for PHP and Perl. IPv6 is supported. 

As side-effect, RULI also provides a general-purpose,
event-driven, asynchronous, stub DNS resolver. 

%package -n	%{libname}
Summary:	The RULI (Resolver User Layer Interface) library
Group:          System/Libraries

%description -n	%{libname}
RULI stands for Resolver User Layer Interface. It's a library
built on top of an asynchronous DNS stub resolver. RULI provides
an easy-to-use interface for querying DNS SRV resource records.
The goal is to promote the wide deployment of SRV-cognizant
software. RULI aims to fully support SRV-related standards. There
are bindings for PHP and Perl. IPv6 is supported. 

As side-effect, RULI also provides a general-purpose,
event-driven, asynchronous, stub DNS resolver. 

%package -n	%{develname}
Summary:	Static library and header files for the %{libname} library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname ruli 4 -d}

%description -n	%{develname}
RULI stands for Resolver User Layer Interface. It's a library
built on top of an asynchronous DNS stub resolver. RULI provides
an easy-to-use interface for querying DNS SRV resource records.
The goal is to promote the wide deployment of SRV-cognizant
software. RULI aims to fully support SRV-related standards. There
are bindings for PHP and Perl. IPv6 is supported. 

As side-effect, RULI also provides a general-purpose,
event-driven, asynchronous, stub DNS resolver. 

%package	tools
Summary:	Tools utilizing the RULI (Resolver User Layer Interface) library
Group:          System/Servers

%description	tools
RULI stands for Resolver User Layer Interface. It's a library
built on top of an asynchronous DNS stub resolver. RULI provides
an easy-to-use interface for querying DNS SRV resource records.
The goal is to promote the wide deployment of SRV-cognizant
software. RULI aims to fully support SRV-related standards. There
are bindings for PHP and Perl. IPv6 is supported. 

As side-effect, RULI also provides a general-purpose,
event-driven, asynchronous, stub DNS resolver. 

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build

for dir in src sample tools; do
    %make -C $dir \
	OOP_BASE_DIR=%{_prefix} \
	OOP_INCLUDE_DIR=%{_includedir} \
	OOP_LIB_DIR=%{_libdir}
done

#	DEFINE_SOLARIS="%{optflags} -fPIC"

%install
rm -rf %{buildroot}

for dir in src sample tools; do
    make -C $dir \
	INSTALL_BASE_DIR=%{buildroot}%{_prefix} \
	INSTALL_INCLUDE_DIR=%{buildroot}%{_includedir} \
	INSTALL_LIB_DIR=%{buildroot}%{_libdir} \
	INSTALL_MAN_DIR=%{buildroot}%{_mandir} \
	install
done

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README
%attr(0755,root,root) %{_libdir}/*.so.*
%attr(0644,root,root) %{_mandir}/man3/*

%files -n %{develname}
%defattr(-,root,root)
%doc TODO
%attr(0644,root,root) %{_includedir}/*.h
%attr(0755,root,root) %{_libdir}/*.so
%attr(0755,root,root) %{_libdir}/*.a

%files tools
%defattr(-,root,root)
%doc tools/README
%attr(0755,root,root) %{_bindir}/*
%attr(0644,root,root) %{_mandir}/man1/*


%changelog
* Mon Oct 05 2009 Oden Eriksson <oeriksson@mandriva.com> 0.36-5mdv2010.0
+ Revision: 454043
- P1: fix format string errors
- rebuild

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

* Wed Jul 09 2008 Oden Eriksson <oeriksson@mandriva.com> 0.36-3mdv2009.0
+ Revision: 233001
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.36-2mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.36-2mdv2008.0
+ Revision: 83648
- new devel naming


* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.36-1mdv2007.0
+ Revision: 85478
- Import ruli

* Mon May 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.36-1mdk
- 0.36

* Sat Nov 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.35-2mdk
- oops! new major...

* Sat Nov 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.35-1mdk
- 0.35
- rediffed P0

* Fri Dec 31 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.29-4mdk
- revert latest "lib64 fixes"

* Tue Dec 28 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.29-3mdk
- lib64 fixes

* Sun Dec 12 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.29-2mdk
- lib64 fixes

* Mon Aug 30 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.29-1mdk
- initial mandrake package

