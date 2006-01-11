#
# Conditional build:
%bcond_without	static_libs # don't build static libraries
#
Summary:	C++ user interface toolkit for X with database and Excel support
Name:		sptk
Version:	3.0.11
Release:	0.1
License:	LGPL v2+ with the exceptions: http://www.sptk.net/index.php?act=license
Group:		Libraries
Source0:	http://www.sptk.net/%{name}-%{version}.tbz2
# Source0-md5:	2779cf1b1d82bcc692c68cddc63f1adb
URL:		http://www.sptk.net/
BuildRequires:	aspell-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fltk-devel
BuildRequires:	libtool
BuildRequires:	sqlite3-devel
BuildRequires:	unixODBC-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ user interface toolkit for X with database and Excel support.

%package devel
Summary:	Header files for SPTK library
Summary(pl):	Pliki nag³ówkowe biblioteki SPTK
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for SPTK library.

%description devel -l pl
Pliki nag³ówkowe biblioteki SPTK.

%package static
Summary:	Static SPTK library
Summary(pl):	Statyczna biblioteka SPTK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SPTK library.

%description static -l pl
Statyczna biblioteka SPTK.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
#%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
