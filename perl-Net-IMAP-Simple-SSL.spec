#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Net
%define		pnam	IMAP-Simple-SSL
Summary:	Net::IMAP::Simple::SSL - SSL support for Net::IMAP::Simple
Summary(pl.UTF-8):	Net::IMAP::Simple::SSL - obsługa SSL dla Net::IMAP::Simple
Name:		perl-Net-IMAP-Simple-SSL
Version:	1.3
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	86f5e996ff9adadbc849aadc351eca81
URL:		http://search.cpan.org/dist/Net-IMAP-Simple-SSL/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::More)
BuildRequires:	perl-IO-Socket-SSL
BuildRequires:	perl-Net-IMAP-Simple >= 0.95
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a subclass of Net::IMAP::SImple that includes SSL
support. The interface is identical.

%description -l pl.UTF-8
Ten moduł jest podklasą Net::IMAP::Simple dodającą obsługę protokołu
SSL. Interfejs w obu klasach jest identyczny.

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
%doc Changes README
%dir %{perl_vendorlib}/Net/IMAP/Simple
%{perl_vendorlib}/Net/IMAP/Simple/SSL.pm
%{_mandir}/man3/*
