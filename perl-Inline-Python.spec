#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pnam	Python
Summary:	Inline::Python Perl module
Summary(cs):	Modul Inline::Python pro Perl
Summary(da):	Perlmodul Inline::Python
Summary(de):	Inline::Python Perl Modul
Summary(es):	M�dulo de Perl Inline::Python
Summary(fr):	Module Perl Inline::Python
Summary(it):	Modulo di Perl Inline::Python
Summary(ja):	Inline::Python Perl �⥸�塼��
Summary(ko):	Inline::Python �� ����
Summary(nb):	Perlmodul Inline::Python
Summary(pl):	Modu� Perla Inline::Python
Summary(pt):	M�dulo de Perl Inline::Python
Summary(pt_BR):	M�dulo Perl Inline::Python
Summary(ru):	������ ��� Perl Inline::Python
Summary(sv):	Inline::Python Perlmodul
Summary(uk):	������ ��� Perl Inline::Python
Summary(zh_CN):	Inline::Python Perl ģ��
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

%description -l pl
Modu� Inline::Python - pozwalaj�cy na pisanie procedur i klas Perla w
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
