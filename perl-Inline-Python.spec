#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define		pname	Python
Summary:	Inline::Python Perl module
Summary(cs):	Modul Inline::Python pro Perl
Summary(da):	Perlmodul Inline::Python
Summary(de):	Inline::Python Perl Modul
Summary(es):	Módulo de Perl Inline::Python
Summary(fr):	Module Perl Inline::Python
Summary(it):	Modulo di Perl Inline::Python
Summary(ja):	Inline::Python Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Inline::Python ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul Inline::Python
Summary(pl):	Modu³ Perla Inline::Python
Summary(pt):	Módulo de Perl Inline::Python
Summary(pt_BR):	Módulo Perl Inline::Python
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Inline::Python
Summary(sv):	Inline::Python Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Inline::Python
Summary(zh_CN):	Inline::Python Perl Ä£¿é
Name:		perl-Inline-Python
Version:	0.20
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
# Source0-md5:	b409236f93bc7c872b20c56debf97a8d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Inline >= 0.42
BuildRequires:	python-devel
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Python - Write Perl subs and classes in Python.

%description -l pl
Modu³ Inline::Python - pozwalaj±cy na pisanie procedur i klas Perla w
Pythonie.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

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
