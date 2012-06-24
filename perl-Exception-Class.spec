%include	/usr/lib/rpm/macros.perl
%define		pdir	Exception
%define		pnam	Class
Summary:	Exception::Class Perl module
Summary(cs):	Modul Exception::Class pro Perl
Summary(da):	Perlmodul Exception::Class
Summary(de):	Exception::Class Perl Modul
Summary(es):	M�dulo de Perl Exception::Class
Summary(fr):	Module Perl Exception::Class
Summary(it):	Modulo di Perl Exception::Class
Summary(ja):	Exception::Class Perl �⥸�塼��
Summary(ko):	Exception::Class �� ����
Summary(no):	Perlmodul Exception::Class
Summary(pl):	Modu� Perla Exception::Class
Summary(pt):	M�dulo de Perl Exception::Class
Summary(pt_BR):	M�dulo Perl Exception::Class
Summary(ru):	������ ��� Perl Exception::Class
Summary(sv):	Exception::Class Perlmodul
Summary(uk):	������ ��� Perl Exception::Class
Summary(zh_CN):	Exception::Class Perl ģ��
Name:		perl-Exception-Class
Version:	1.01
Release:	3
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005
BuildRequires:	perl-Class-Data-Inheritable >= 0.02
BuildRequires:	perl-Devel-StackTrace >= 0.9
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
#%{__make} test

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
