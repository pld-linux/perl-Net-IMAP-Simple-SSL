#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	IMAP-Simple-SSL
Summary:	Net::IMAP::Simple::SSL - SSL support for Net::IMAP::Simple
Summary(pl):	Net::IMAP::Simple::SSL - wsparcie SSL dla Net::IMAP::Simple
Name:		perl-Net-IMAP-Simple-SSL
Version:	1.3
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	86f5e996ff9adadbc849aadc351eca81
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(IO::Socket::SSL)
BuildRequires:	perl(Net::IMAP::Simple) >= 0.95
BuildRequires:	perl(Test::More)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a subclass of Net::IMAP::SImple that includes SSL
support. The interface is identical.

%description -l pl
Ten modu³ jest podklas± Net::IMAP::Simple dodaj±c± wsparcie dla
protoko³u SSL. Interfejs w obu klasach jest identyczny.

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
%{perl_vendorlib}/Net/IMAP/Simple/SSL.pm
%{_mandir}/man3/*
