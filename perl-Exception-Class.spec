#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Exception
%define	pnam	Class
Summary:	Exception::Class - Declare real exception classes in Perl
Summary(pl):	Exception::Class - Zadeklaruj prawdziwe klasy wyj�tk�w w Perlu
Name:		perl-Exception-Class
Version:	1.09
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005
%if %{!?_without_tests:1}0
BuildRequires:	perl-Class-Data-Inheritable >= 0.02
BuildRequires:	perl-Devel-StackTrace >= 1.03
BuildRequires:	perl(Test::More) >= 0.46
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exception::Class allows you to declare exceptions in your modules
in a manner similar to how exceptions are declared in Java.

%description -l pl
Exception::Class pozwala na deklarowanie w modu�ach wyj�tk�w
w spos�b podobny do stosowanego w Javie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes LICENSE
%{perl_sitelib}/Exception
%{_mandir}/man3/*
