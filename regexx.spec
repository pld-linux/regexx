Summary:	Regexx
Name:		regexx
Version:	0.97
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://download.sourceforge.net/regexx/%{name}-%{version}.tar.gz
Patch0:		%{name}-sys-pcre.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Regexx is a complete Regular Expressions C++ solution. It
implements easy expression execution, global searching,
replace with atom substitution, customized replaces,
easy match and atom strings retrieving. It's also included
in the library functions to split strings with strings or
regular expressions.

%package devel
Summary:	Regexx - development files
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Regexx - development files.

%package static
Summary:	Static regexx library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static regexx library.

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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.hh

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
