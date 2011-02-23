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
Version:	1.32
Release:	1
License:	Artistic 2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Exception/DROLSKY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	83788ad5a2c5e946877e4ec362e19622
URL:		http://search.cpan.org/dist/Exception-Class/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.31
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Data-Inheritable >= 0.02
BuildRequires:	perl-Devel-StackTrace >= 1.20
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	perl($isa)

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
%dir %{perl_vendorlib}/Exception
%{perl_vendorlib}/Exception/Class.pm
%{perl_vendorlib}/Exception/Class
%{_mandir}/man3/Exception::Class*.3pm*
