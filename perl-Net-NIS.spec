%define upstream_name	 Net-NIS
%define upstream_version 0.43

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	NIS interface to Perl 5	
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is a snapshot release of the NIS interface to Perl 5.  There are
three parts to the interface: the raw component (Net::NIS), the object-
oriented component (Net::NIS::Table), and the tied interface (Net::NIS).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make OPTIMIZE="%{optflags}"
# (sb) known to fail:
#  http://nntp.x.perl.org/group/perl.cpan.testers/58036 (and more)
#make test

%install
rm -rf %{buildroot} 
%makeinstall_std 

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorarch}/Net
%{perl_vendorarch}/auto/Net
