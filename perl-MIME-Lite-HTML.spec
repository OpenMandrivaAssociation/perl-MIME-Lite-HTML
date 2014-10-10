%define upstream_name    MIME-Lite-HTML
%define upstream_version 1.24

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.24
Release:	2
Summary:	Provide routine to transform HTML to MIME
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MIME/MIME-Lite-HTML-1.24.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Email::Date::Format)
BuildRequires:	perl(HTML::LinkExtor)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(MIME::Lite)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI::URL)
BuildArch:	noarch

%description
This module is a Perl mail client interface for sending message that
support HTML format and build them for you.. This module provide routine to
transform a HTML page in MIME::Lite mail. So you need this module to use
MIME-Lite-HTML possibilities

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

# %check
# %make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/MIME

%changelog
* Fri Sep 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.230.0-1mdv2010.0
+ Revision: 430505
- import perl-MIME-Lite-HTML


* Thu Sep 03 2009 cpan2dist 1.23-1mdv
- initial mdv release, generated with cpan2dist

