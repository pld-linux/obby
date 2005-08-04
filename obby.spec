Summary:	obby library
Summary(pl):	Biblioteka obby
Name:		obby
Version:	0.2.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://releases.0x539.de/obby/%{name}-%{version}.tar.gz
# Source0-md5:	6bd46f9b8c7652d7bfa8413ed2c2af4b
BuildRequires: gmp-c++-devel
BuildRequires: howl-devel
BuildRequires: net6-devel >= 1.1.0
URL:		http://gobby.0x539.de/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
obby library.

%description -l pl
Biblioteka obby

%package devel
Summary:	Header files for obby
Summary(pl):	Pliki nag³ówkowe biblioteki obby
Summary(pt_BR):	Arquivos do pacote obby para desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for obby.

%description devel -l pl
Pliki nag³ówkowe biblioteki obby.

%description devel -l pt_BR
Arquivos de cabeçalho e bibliotecas usadas no desenvolvimento de
aplicativos que usam obby.

%package static
Summary:	Static obby library
Summary(pl):	Biblioteka statyczna obby
Summary(pt_BR):	Arquivos do pacote obby para desenvolvimento estático
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static obby library.

%description static -l pl
Biblioteka statyczna obby.

%description static -l pt_BR
Arquivos de cabeçalho e bibliotecas usadas no desenvolvimento de
aplicativos estáticos que usam obby.

%prep
%setup -q

%build
%configure --with-howl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_examplesdir}/%{name}-%{version},%{_mandir}/man3}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
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
