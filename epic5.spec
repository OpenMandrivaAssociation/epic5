Name:           epic5
Version:        0.3.4
Release:        %mkrel 3
Epoch:          0
Summary:        (E)nhanced (P)rogrammable (I)RC-II (C)lient
Group:          Networking/IRC
License:        BSD
URL:            http://www.epicsol.org/
Source0:        ftp://ftp.epicsol.org:/pub/epic/EPIC5-ALPHA/epic5-%{version}.tar.bz2 
Source1:        ftp://ftp.epicsol.org/pub/epic/help/epic-help-current.tar.bz2
Source2:        http://amnesiac.ircii.org/ac-snap.tgz
Patch0:         http://epicsol.org/~jnelson/epic5-0.3.4-patch1
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
#BuildRequires:  dante-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-devel
BuildRequires:  ruby-devel
BuildRequires:  tcl-devel
BuildRoot:         %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
EPIC4 is a new direction in ircII development. No longer is EPIC
100% backwards compatible with ircII, but instead we have chosen to
find those things where compatibility is undesirable, and fix them.
No gratuitous incompatibilities have been added, but lots of new
code has been added to make EPIC the best ircII client we could make.

EPIC4 is derived directly from EPIC3, which was itself derived from
IRC-II which is currently maintained by Matthew Green, and includes
in whole all the additions included in the "plus" clients by Jeremy
Nelson and all of the modifications in the "mod" clients by Jake Khuon.
EPIC is currently maintained by EPIC Software Labs (ESL), comprised of
a couple of dozen people.

%prep 
%setup -q -a 1 -T -b 0
%patch0 -p1
%{_bindir}/find . -type d -name CVS | %{_bindir}/xargs -t %{__rm} -r
%{__perl} -pi -e 's|/usr/local/bin/perl5|%{__perl}|' regress/crash-irc

%build
%{configure2_5x} --with-ipv6 \
                 --with-perl \
                 --with-ruby \
                 --with-ssl \
                 --without-socks \
                 --with-tcl
%{make} wserv_exe=%{_bindir}/wserv4

%install
%{__rm} -rf %{buildroot}
%{makeinstall} libexecdir=%{buildroot}%{_bindir} sharedir=%{buildroot}%{_datadir} installhelp 
%{__chmod} 755 %{buildroot}%{_datadir}/%{name}/script/epic-crypt-gpg{,-aa}

%{__tar} -xf %{SOURCE2} -C %{buildroot}%{_datadir}/%{name}/script
%{__chmod} 644 %{buildroot}%{_datadir}/%{name}/script/amn/themes/ansiless.th

%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=EPIC5
Comment=(E)nhanced (P)rogrammable (I)RC-II (C)lient
Exec=epic5
Terminal=true
Type=Application
Icon=irc_section
Categories=Network;IRCClient;
EOF

%{_bindir}/desktop-file-install --vendor="mandriva" \
  --add-category="X-MandrivaLinux-Internet-Chat" \
  --dir %{buildroot}%{_datadir}/applications %{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%post
%{update_desktop_database}
%if 0
%update_icon_cache hicolor
%endif

%postun
%{clean_desktop_database}
%if 0
%clean_icon_cache hicolor
%endif

%files
%defattr(0644,root,root,0755)
%doc BUG_FORM COPYRIGHT FILES INSTALL KNOWNBUGS README README-CRYPTO UPDATES VOTES doc/* contrib regress
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}-%{version}
%attr(0755,root,root) %{_bindir}/epic5-wserv4
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}
