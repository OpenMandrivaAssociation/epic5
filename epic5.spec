Name:		epic5
Version:	1.1.2
Release:	%mkrel 1
Epoch:		0
Summary:	(E)nhanced (P)rogrammable (I)RC-II (C)lient
Group:		Networking/IRC
License:	BSD
URL:		http://www.epicsol.org/
Source0:	http://ftp.epicsol.org/pub/epic/EPIC5-PRODUCTION/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.epicsol.org/pub/epic/help/epic-help-current.tar.bz2
# Amnesiac 2.0.2 release updated on Jul 26 2010 @ 20:09
Source2:	http://amnesiac.ircii.org/amnesiac2.0.2cvs51.tgz
#BuildRequires:  dante-devel
BuildRequires:	libarchive-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-devel
BuildRequires:	ruby-devel
BuildRequires:	tcl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
EPIC is an irc client project. The EPIC software was forked from
ircII-2.8.2 in fall 1994. There have been 5 generations of EPIC.

EPIC's development model is to provide tools to scripters rather than
features to end users. Out of the box, EPIC behaves much the same way
ircII-2.8.2 did in 1994. To truly leverage EPIC, you will need a
script pack. This Mandriva package includes the Amnesia script pack,
see http://amnesiac.ircii.org/

%prep 
%setup -q -a 1 -T -b 0
%{_bindir}/find . -type d -name CVS | %{_bindir}/xargs -t %{__rm} -r
%{__perl} -pi -e 's|/usr/local/bin/perl5|%{__perl}|' regress/crash-irc

%build
%{configure2_5x} --with-ipv6 \
                 --with-perl \
                 --with-ruby \
                 --with-ssl \
                 --without-socks \
                 --with-tcl
make wserv_exe=%{_bindir}/wserv4

%install
%{__rm} -rf %{buildroot}
%{makeinstall} libexecdir=%{buildroot}%{_bindir} sharedir=%{buildroot}%{_datadir} installhelp 
%{__chmod} 755 %{buildroot}%{_datadir}/%{name}/script/epic-crypt-gpg{,-aa}

%{__tar} -xf %{SOURCE2} -C %{buildroot}%{_datadir}/%{name}/script
%{__chmod} 644 %{buildroot}%{_datadir}/%{name}/script/amn/themes/ansiless.th

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc BUG_FORM COPYRIGHT FILES INSTALL KNOWNBUGS README README-CRYPTO UPDATES VOTES doc/* contrib regress
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}-%{version}
%attr(0755,root,root) %{_bindir}/epic5-wserv4
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}



%changelog
* Thu Oct 13 2011 Andrey Bondrov <abondrov@mandriva.org> 0:1.1.2-1mdv2011.0
+ Revision: 704598
- New version: 1.1.2

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0:0.9.0-4mdv2011.0
+ Revision: 610381
- rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 0:0.9.0-3mdv2010.1
+ Revision: 537453
- rebuild

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0:0.9.0-2mdv2010.0
+ Revision: 437470
- rebuild

* Sat Dec 06 2008 Adam Williamson <awilliamson@mandriva.org> 0:0.9.0-1mdv2009.1
+ Revision: 311082
- finish dropping the menu entry
- rebuild for new tcl
- drop the menu entry, it's a console app
- drop parallel build, it breaks
- update the description, which was still talking about epic4
- add the amnesiac version info as a comment as you can't tell from file name
- new release 0.9.0
- spec clean

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0:0.3.5-3mdv2009.0
+ Revision: 244929
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Nov 10 2007 David Walluck <walluck@mandriva.org> 0:0.3.5-1mdv2008.1
+ Revision: 107318
- 0.3.5

* Mon Sep 10 2007 David Walluck <walluck@mandriva.org> 0:0.3.4-4mdv2008.0
+ Revision: 83969
- bump release
- ship the amnesiac snapshot for this epic version

* Mon Sep 10 2007 David Walluck <walluck@mandriva.org> 0:0.3.4-3mdv2008.0
+ Revision: 83960
- include hook bugfix from hop
- update amnesiac to 1.5r2
- do not force removal of CVS dirs
- remove Application category from desktop menu
- set vendor for desktop menu
- fix amnesiac perms to be world readable

* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 0:0.3.4-2mdv2008.0
+ Revision: 82012
- rebuild for new soname of tcl

* Thu Sep 06 2007 Nicolas Vigier <nvigier@mandriva.com> 0:0.3.4-1mdv2008.0
+ Revision: 81078
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Sun Feb 04 2007 David Walluck <walluck@mandriva.org> 0.3.2-1mdv2007.0
+ Revision: 116124
- 0.3.2

* Fri Oct 27 2006 David Walluck <walluck@mandriva.org> 0:0.3.1-3mdv2007.1
+ Revision: 72938
- include amnesiac 1.4r2

* Fri Oct 27 2006 David Walluck <walluck@mandriva.org> 0:0.3.1-2mdv2007.1
+ Revision: 72921
- fix summary, description, and menu summary

* Fri Oct 27 2006 David Walluck <walluck@mandriva.org> 0:0.3.1-1mdv2007.0
+ Revision: 72913
- Import epic5

* Thu Oct 26 2006 David Walluck <walluck@mandriva.org> 0:0.3.1-1mdv2007.1
- release

