#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pname	Python
Summary:	Inline::Python Perl module
Summary(cs):	Modul Inline::Python pro Perl
Summary(da):	Perlmodul Inline::Python
Summary(de):	Inline::Python Perl Modul
Summary(es):	M�dulo de Perl Inline::Python
Summary(fr):	Module Perl Inline::Python
Summary(it):	Modulo di Perl Inline::Python
Summary(ja):	Inline::Python Perl �⥸�塼��
Summary(ko):	Inline::Python �� ����
Summary(no):	Perlmodul Inline::Python
Summary(pl):	Modu� Perla Inline::Python
Summary(pt):	M�dulo de Perl Inline::Python
Summary(pt_BR):	M�dulo Perl Inline::Python
Summary(ru):	������ ��� Perl Inline::Python
Summary(sv):	Inline::Python Perlmodul
Summary(uk):	������ ��� Perl Inline::Python
Summary(zh_CN):	Inline::Python Perl ģ��
Name:		perl-Inline-Python
Version:	0.20
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline >= 0.42
BuildRequires:	python-devel
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::Python - Write Perl subs and classes in Python.

%description -l pl
Modu� Inline::Python - pozwalaj�cy na pisanie procedur i klas Perla w
Pythonie.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
perl Makefile.PL </dev/null
%{__make} OPTIMIZE="%{rpmcflags}"
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TESTED ToDo
%{perl_sitearch}/Inline/Python.pm
%dir %{perl_sitearch}/auto/Inline/Python
%{perl_sitearch}/auto/Inline/Python/Python.bs
%attr(755,root,root) %{perl_sitearch}/auto/Inline/Python/Python.so
%{_mandir}/man3/*
