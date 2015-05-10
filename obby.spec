Summary:	obby library providing synchronized document buffers
Summary(pl.UTF-8):	Biblioteka obby udostępniająca synchronizowane bufory dokumentów
Name:		obby
Version:	0.4.8
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://releases.0x539.de/obby/%{name}-%{version}.tar.gz
# Source0-md5:	5d4cd4e77f87b092e5ed21b104d8ad33
URL:		http://gobby.0x539.de/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	avahi-devel >= 0.6
BuildRequires:	gettext-tools >= 0.15
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	net6-devel >= 1.3.3
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
obby library providing synchronized document buffers.

%description -l pl.UTF-8
Biblioteka obby udostępniająca synchronizowane bufory dokumentów.

%package devel
Summary:	Header files for obby
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki obby
Summary(pt_BR.UTF-8):	Arquivos do pacote obby para desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	avahi-devel >= 0.6
Requires:	net6-devel >= 1.3.3

%description devel
Header files for obby.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki obby.

%description devel -l pt_BR.UTF-8
Arquivos de cabeçalho e bibliotecas usadas no desenvolvimento de
aplicativos que usam obby.

%package static
Summary:	Static obby library
Summary(pl.UTF-8):	Biblioteka statyczna obby
Summary(pt_BR.UTF-8):	Arquivos do pacote obby para desenvolvimento estático
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static obby library.

%description static -l pl.UTF-8
Biblioteka statyczna obby.

%description static -l pt_BR.UTF-8
Arquivos de cabeçalho e bibliotecas usadas no desenvolvimento de
aplicativos estáticos que usam obby.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--enable-ipv6 \
	--with-zeroconf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libobby-0.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libobby-0.4.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libobby.so
%{_includedir}/obby
%{_pkgconfigdir}/obby-0.4.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libobby.a
