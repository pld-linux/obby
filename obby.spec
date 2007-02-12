Summary:	obby library
Summary(pl.UTF-8):   Biblioteka obby
Name:		obby
Version:	0.3.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://releases.0x539.de/obby/%{name}-%{version}.tar.gz
# Source0-md5:	b14135018a3093395296cf091f9f824f
URL:		http://gobby.0x539.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmp-c++-devel
BuildRequires:	howl-devel
BuildRequires:	libtool
BuildRequires:	net6-devel >= 1.2.1
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
obby library.

%description -l pl.UTF-8
Biblioteka obby

%package devel
Summary:	Header files for obby
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki obby
Summary(pt_BR.UTF-8):   Arquivos do pacote obby para desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-c++-devel
Requires:	howl-devel
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
Summary(pl.UTF-8):   Biblioteka statyczna obby
Summary(pt_BR.UTF-8):   Arquivos do pacote obby para desenvolvimento estático
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
