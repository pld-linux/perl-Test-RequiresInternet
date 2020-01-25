#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	RequiresInternet
Summary:	Test::RequiresInternet - Easily test network connectivity
Summary(pl.UTF-8):	Test::RequiresInternet - łatwe sprawdzanie połączenia z siecią
Name:		perl-Test-RequiresInternet
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0ba9f1cff4cf90ed2618c2eddfd525d8
URL:		https://metacpan.org/release/Test-RequiresInternet/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is intended to easily test network connectivity before
functional tests begin to non-local Internet resources. It does not
require any modules beyond those supplied in core Perl.

%description -l pl.UTF-8
Ten moduł służy do łatwego sprawdzania połączenia z siecią przed
testami funkcjonalnymi sięgającymi do zasobów internetowych. Moduł
nie wymaga żadnych modułów nie dostarczanych wraz z dystrybucją Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/RequiresInternet.pm
%{_mandir}/man3/Test::RequiresInternet.3pm*
