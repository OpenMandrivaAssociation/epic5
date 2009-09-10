Name:		epic5
Version:	0.9.0
Release:	%mkrel 2
Epoch:		0
Summary:	(E)nhanced (P)rogrammable (I)RC-II (C)lient
Group:		Networking/IRC
License:	BSD
URL:		http://www.epicsol.org/
Source0:	http://ftp.epicsol.org/pub/epic/EPIC5-BETA/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.epicsol.org/pub/epic/help/epic-help-current.tar.bz2
# Amnesiac 1.5b/rc1 release updated on Aug 30 2008 @ 04:00
Source2:	http://amnesiac.ircii.org/ac-snap.tgz
#BuildRequires:  dante-devel
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
