#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Accessor-Grouped
Version  : 0.10014
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Class-Accessor-Grouped-0.10014.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Class-Accessor-Grouped-0.10014.tar.gz
Summary  : 'Lets you build groups of accessors'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::XSAccessor)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Sub::Name)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)

%description
NAME
Class::Accessor::Grouped - Lets you build groups of accessors
SYNOPSIS
use base 'Class::Accessor::Grouped';

%package dev
Summary: dev components for the perl-Class-Accessor-Grouped package.
Group: Development
Provides: perl-Class-Accessor-Grouped-devel

%description dev
dev components for the perl-Class-Accessor-Grouped package.


%prep
%setup -q -n Class-Accessor-Grouped-0.10014

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Class/Accessor/Grouped.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Accessor::Grouped.3
