# NOTE: no sense to build for Th, online service has been shutdown in 2020
Summary:	Google Cloud Print Common Print Dialog Backend
Summary(pl.UTF-8):	Backend Google Cloud Print dla CPDB (wspólnych okien dialogowych drukowania)
Name:		cpdb-backend-gcp
Version:	1.1.0
Release:	0.1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/OpenPrinting/cpdb-backend-gcp/releases
Source0:	https://github.com/OpenPrinting/cpdb-backend-gcp/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	48a9c244c20d1d7b754eb29018eb5adf
URL:		https://github.com/OpenPrinting/cpdb-backend-gcp
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
# pkgconfig(cpdb-libs-backend)
BuildRequires:	cpdb-libs-devel >= 1
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	json-glib-devel >= 1.0
BuildRequires:	rest-devel >= 0.7
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	pkgconfig
Requires:	cpdb-libs >= 1
Requires:	json-glib >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Google Cloud Print Common Print Dialog
Backend. This backend manages and provides information about Google
Cloud Print printing destinations to the printing dialog.

%description -l pl.UTF-8
Ten pakiet zawiera backend Google Cloud Print dla CPDB (Common
Printing Dialog Backends - wspólnych backendów okien dialogowych
drukowania). Ten backend zarządza i dostarcza informacje o celach
drukowania przez Google Cloud Print.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%attr(755,root,root) %{_libdir}/print-backends/gcp
%{_datadir}/dbus-1/services/org.openprinting.Backend.GCP.service
%{_datadir}/print-backends/org.openprinting.Backend.GCP
