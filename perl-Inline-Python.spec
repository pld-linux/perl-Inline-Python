%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pname	Python
Summary:	Inline::Python perl module
Summary(pl):	Modu³ perla Inline::Python
Name:		perl-Inline-Python
Version:	0.20
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline >= 0.42
BuildRequires:	python-devel
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL </dev/null
%{__make}

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
