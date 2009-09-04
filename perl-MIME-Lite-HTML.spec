%define upstream_name    MIME-Lite-HTML
%define upstream_version 1.23

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:    Provide routine to transform HTML to MIME
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MIME/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(Email::Date::Format)
BuildRequires: perl(HTML::LinkExtor)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(MIME::Lite)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI::URL)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is a Perl mail client interface for sending message that
support HTML format and build them for you.. This module provide routine to
transform a HTML page in MIME::Lite mail. So you need this module to use
MIME-Lite-HTML possibilities

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/MIME

