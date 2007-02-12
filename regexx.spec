Summary:	Regexx - a complete Regular Expressions C++ solution
Summary(pl.UTF-8):	Regexx - kompletne rozwiązanie problemu wyrażeń regularnych w C++
Name:		regexx
Version:	0.98.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/regexx/%{name}-%{version}.tar.gz
# Source0-md5:	a33aecd7bc0005e3a2c7fa946722b56c
Patch0:		%{name}-sys-pcre.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexx is a complete Regular Expressions C++ solution. It implements
easy expression execution, global searching, replace with atom
substitution, customized replaces, easy match and atom strings
retrieving. It's also included in the library functions to split
strings with strings or regular expressions.

%description -l pl.UTF-8
Regexx to kompletne rozwiązanie problemu wyrażeń regularnych w C++. Ma
zaimplementowane łatwe wykonywanie wyrażeń, wyszukiwanie globalne,
zamianę z podstawianiem elementów, konfigurowalne podstawienia, łatwe
dopasowywanie i uzyskiwanie elementów łańcuchów. Do biblioteki zostały
dołączone także funkcje do dzielenia łańcuchów na podstawie łańcuchów
lub wyrażeń regularnych.

%package devel
Summary:	Regexx - development files
Summary(pl.UTF-8):	Regexx - pliki dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Regexx - development files.

%description devel -l pl.UTF-8
Regexx - pliki dla programistów.

%package static
Summary:	Static regexx library
Summary(pl.UTF-8):	Statyczna biblioteka regexx
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static regexx library.

%description static -l pl.UTF-8
Statyczna biblioteka regexx.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.hh
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
