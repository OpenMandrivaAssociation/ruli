%define	major 4
%define libname	%mklibname ruli %{major}

Summary:	The RULI (Resolver User Layer Interface) library
Name:		ruli
Version:	0.36
Release:	%mkrel 1
License:	BSD
Group:		System/Libraries
URL:		http://www.nongnu.org/ruli/
Source0:	http://savannah.nongnu.org/download/ruli/ruli_%{version}.orig.tar.gz
Source2:	http://savannah.nongnu.org/download/ruli/ruli_%{version}.orig.tar.gz.sig
Patch0:		ruli-0.35-optflags.diff
BuildRequires:	oop-devel
BuildConflicts:	%{name}-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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

%package -n	%{libname}-devel
Summary:	Static library and header files for the %{libname} library
Group:		Development/C
Obsoletes:	%{name}-devel lib%{name}-devel
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
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

%build

for dir in src sample tools; do
    %make -C $dir \
	OOP_BASE_DIR=%{_prefix} \
	OOP_INCLUDE_DIR=%{_includedir} \
	OOP_LIB_DIR=%{_libdir}
done

#	DEFINE_SOLARIS="%{optflags} -fPIC"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

for dir in src sample tools; do
    make -C $dir \
	INSTALL_BASE_DIR=%{buildroot}%{_prefix} \
	INSTALL_INCLUDE_DIR=%{buildroot}%{_includedir} \
	INSTALL_LIB_DIR=%{buildroot}%{_libdir} \
	INSTALL_MAN_DIR=%{buildroot}%{_mandir} \
	install
done

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README
%attr(0755,root,root) %{_libdir}/*.so.*
%attr(0644,root,root) %{_mandir}/man3/*

%files -n %{libname}-devel
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


