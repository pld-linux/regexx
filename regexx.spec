Summary:	Regexx - a complete Regular Expressions C++ solution
Summary(pl):	Regexx - kompletne rozwi±zanie problemu wyra¿eñ regularnych w C++
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

%description -l pl
Regexx to kompletne rozwi±zanie problemu wyra¿eñ regularnych w C++. Ma
zaimplementowane ³atwe wykonywanie wyra¿eñ, wyszukiwanie globalne,
zamianê z podstawianiem elementów, konfigurowalne podstawienia, ³atwe
dopasowywanie i uzyskiwanie elementów ³añcuchów. Do biblioteki zosta³y
do³±czone tak¿e funkcje do dzielenia ³añcuchów na podstawie ³añcuchów
lub wyra¿eñ regularnych.

%package devel
Summary:	Regexx - development files
Summary(pl):	Regexx - pliki dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Regexx - development files.

%description devel -l pl
Regexx - pliki dla programistów.

%package static
Summary:	Static regexx library
Summary(pl):	Statyczna biblioteka regexx
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static regexx library.

%description static -l pl
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
