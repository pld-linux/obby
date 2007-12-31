Summary:	obby library
Summary(pl.UTF-8):	Biblioteka obby
Name:		obby
Version:	0.4.5
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://releases.0x539.de/obby/%{name}-%{version}.tar.gz
# Source0-md5:	bc1e0d2bf7115fe53a54cb4d2d0776b7
URL:		http://gobby.0x539.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-devel
BuildRequires:	gmp-c++-devel
BuildRequires:	libtool
BuildRequires:	net6-devel >= 1.3.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
obby library.

%description -l pl.UTF-8
Biblioteka obby

%package devel
Summary:	Header files for obby
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki obby
Summary(pt_BR.UTF-8):	Arquivos do pacote obby para desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	avahi-devel
Requires:	gmp-c++-devel
Requires:	net6-devel >= 1.2.1

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
    --with-howl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_mandir}/man3}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/%{name}*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
