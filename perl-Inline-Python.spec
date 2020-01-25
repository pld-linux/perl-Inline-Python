#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Inline
%define		pnam	Python
Summary:	Inline::Python - Write Perl subs and classes in Python
Summary(pl.UTF-8):	Inline::Python - pisanie procedur i klas Perla w Pythonie
Name:		perl-Inline-Python
Version:	0.29
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Inline/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94cf975dc488f723d2727d82de92d5ea
Patch0:		%{name}-Makefile_PL_lib64.patch
URL:		http://search.cpan.org/dist/Inline-Python/
BuildRequires:	perl-Inline >= 0.42
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	python-devel
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Inline::Python module allows you to put Python source code
directly "inline" in a Perl script or module. It sets up an in-process
Python interpreter, runs your code, and then examines Python's symbol
table for things to bind to Perl. The process of interrogating the
Python interpreter for globals only occurs the first time you run your
Python code. The namespace is cached, and subsequent calls use the
cached version.

%description -l pl.UTF-8
Moduł Inline::Python pozwala na umieszczanie kodu źródłowego w
Pythonie bezpośrednio w skryptach lub modułach perlowych. Tworzy
interpreter Pythona wewnątrz procesu, uruchamia kod, a następnie
sprawdza tabelę symboli Pythona, aby dowiązać jej elementy do Perla.
Proces sprawdzania zmiannych globalnych w interpreterze Pythona
zachodzi tylko przy pierwszym uruchomieniu kodu pythonowego.
Przestrzeń nazw jest zapamiętywana, a kolejne wywołania używają tej
zapamiętanej wersji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TESTED ToDo
%{perl_vendorarch}/Inline/Python.pm
%dir %{perl_vendorarch}/auto/Inline/Python
%attr(755,root,root) %{perl_vendorarch}/auto/Inline/Python/Python.so
%{_mandir}/man3/*
