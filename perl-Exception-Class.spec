#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Exception
%define		pnam	Class
Summary:	Exception::Class - declare real exception classes in Perl
Summary(pl.UTF-8):	Exception::Class - deklarowanie prawdziwych klas wyjątków w Perlu
Name:		perl-Exception-Class
Version:	1.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Exception/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	362d428cae5dee785a9ed9ac91103a32
URL:		http://search.cpan.org/dist/Exception-Class/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Data-Inheritable >= 0.02
BuildRequires:	perl-Devel-StackTrace >= 1.17
BuildRequires:	perl(Test::More) >= 0.46
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exception::Class allows you to declare exceptions in your modules
in a manner similar to how exceptions are declared in Java.

%description -l pl.UTF-8
Exception::Class pozwala na deklarowanie w modułach wyjątków
w sposób podobny do stosowanego w Javie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE
%{perl_vendorlib}/Exception
%{_mandir}/man3/*
