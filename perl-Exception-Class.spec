%include	/usr/lib/rpm/macros.perl
%define	pdir	Exception
%define	pnam	Class
Summary:	%{pdir}::%{pnam} perl module
Summary(pl):	Modu³ perla %{pdir}::%{pnam}
Name:		perl-%{pdir}-%{pnam}
Version:	1.01
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005
BuildRequires:	perl(Class::Data::Inheritable) >= 0.02
BuildRequires:	perl(Devel::StackTrace) >= 0.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exception::Class allows you to declare exceptions in your modules
in a manner similar to how exceptions are declared in Java.

%description -l pl
Exception::Class pozwala na deklarowanie w modu³ach wyj±tków
w sposób podobny do stosowanego w Javie.


%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes LICENSE
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
