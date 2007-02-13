#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Python
Summary:	Inline::Python Perl module
Summary(cs.UTF-8):	Modul Inline::Python pro Perl
Summary(da.UTF-8):	Perlmodul Inline::Python
Summary(de.UTF-8):	Inline::Python Perl Modul
Summary(es.UTF-8):	Módulo de Perl Inline::Python
Summary(fr.UTF-8):	Module Perl Inline::Python
Summary(it.UTF-8):	Modulo di Perl Inline::Python
Summary(ja.UTF-8):	Inline::Python Perl モジュール
Summary(ko.UTF-8):	Inline::Python 펄 모줄
Summary(nb.UTF-8):	Perlmodul Inline::Python
Summary(pl.UTF-8):	Moduł Perla Inline::Python
Summary(pt.UTF-8):	Módulo de Perl Inline::Python
Summary(pt_BR.UTF-8):	Módulo Perl Inline::Python
Summary(ru.UTF-8):	Модуль для Perl Inline::Python
Summary(sv.UTF-8):	Inline::Python Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Inline::Python
Summary(zh_CN.UTF-8):	Inline::Python Perl 模块
Name:		perl-Inline-Python
Version:	0.21
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eee389d273c5e0fa91126b0329213c6b
Patch0:		%{name}-Makefile_PL_lib64.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Inline >= 0.42
BuildRequires:	perl-Parse-RecDescent
BuildRequires:	python-devel
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Python - Write Perl subs and classes in Python.

%description -l pl.UTF-8
Moduł Inline::Python - pozwalający na pisanie procedur i klas Perla w
Pythonie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL </dev/null \
	INSTALLDIRS=vendor
%{__make} \
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
%{perl_vendorarch}/auto/Inline/Python/Python.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Inline/Python/Python.so
%{_mandir}/man3/*
