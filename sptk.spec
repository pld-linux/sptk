#
# Conditional build:
%bcond_without	static_libs # don't build static libraries
#
Summary:	C++ user interface toolkit for X with database and Excel support
Summary(pl.UTF-8):	Toolkit C++ dla X ze wsparciem dla bazy danych i Excela
Name:		sptk
Version:	3.5.7.05
Release:	0.1
License:	LGPL v2+ with the exceptions: http://www.sptk.net/index.php?act=license
Group:		Libraries
Source0:	http://www.sptk.net/%{name}-%{version}.tbz2
# Source0-md5:	51ac4d3db97903c8f5d72bee980d546b
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
Simple Powerful Toolkit is C++ user interface for X with database and
Excel support.

%description -l pl.UTF-8
SPTK jest toolkitem C++ dla X ze wsparciem dla bazy danych i Excela.

%package devel
Summary:	Header files for SPTK library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SPTK
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for SPTK library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SPTK.

%package static
Summary:	Static SPTK library
Summary(pl.UTF-8):	Statyczna biblioteka SPTK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SPTK library.

%description static -l pl.UTF-8
Statyczna biblioteka SPTK.

%package examples
Summary:	Examples for Simple Powerful Toolkit
Summary(pl.UTF-8):	Przykłady do SPTK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description examples
Examples for Simple Powerful Toolkit.

%description -l pl.UTF-8
Przykłady dla SPTK.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no} \
	--enable-debug=%{?debug:yes}%{!?debug:no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -Rf examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

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

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
