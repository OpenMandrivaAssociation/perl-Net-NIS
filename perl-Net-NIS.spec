%define upstream_name	 Net-NIS
%define upstream_version 0.43

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	5

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.430.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.430.0-2mdv2011.0
+ Revision: 555266
- rebuild

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.430.0-1mdv2010.0
+ Revision: 407817
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.43-5mdv2009.0
+ Revision: 258056
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.43-4mdv2009.0
+ Revision: 246159
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.43-2mdv2008.1
+ Revision: 152223
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Nov 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.43-1mdv2008.1
+ Revision: 110284
- update to new version 0.43

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-1mdv2008.1
+ Revision: 109589
- new version

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.34-6mdv2008.0
+ Revision: 25228
- rebuild


* Fri Apr 28 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.34-5mdk
- Fix SPEC according to Perl Policy
	- Source URL
	- URL
- use mkrel

* Tue Dec 27 2005 Stew Benedict <sbenedict@mandriva.com> 0.34-4mdk
- rebuild

* Thu Nov 18 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.34-3mdk
- rebuild for new perl

* Mon Dec 01 2003 Stew Benedict <sbenedict@mandrakesoft.com> 0.34-2mdk
- rebuild, reupload from correct host

* Mon Dec 01 2003 Stew Benedict <sbenedict@mandrakesoft.com> 0.34-1mdk
- first Mandrake release, optional feature for nocatauth

