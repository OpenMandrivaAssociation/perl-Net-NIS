%define module	Net-NIS
%define name	perl-%{module}
%define version 0.34
%define release %mkrel 5

Summary:	NIS interface to Perl 5	
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-root

%description
This is a snapshot release of the NIS interface to Perl 5.  There are
three parts to the interface: the raw component (Net::NIS), the object-
oriented component (Net::NIS::Table), and the tied interface (Net::NIS).

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
make OPTIMIZE="$RPM_OPT_FLAGS" 
# (sb) known to fail:
#  http://nntp.x.perl.org/group/perl.cpan.testers/58036 (and more)
#make test

%install
rm -rf $RPM_BUILD_ROOT 
%makeinstall_std 

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_mandir}/man3/*
%{perl_vendorarch}/Net
%{perl_vendorarch}/Net/NIS
%{perl_vendorarch}/auto/Net/NIS

