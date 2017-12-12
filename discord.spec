%global         debug_package %{nil}
%global         __strip /bin/true

Name:           discord
Version:        0.0.3
Release:        1%{?dist}
Summary:        All-in-one voice and text chat for gamers

License:        Proprietary
URL:            https://discordapp.com/
Source0:        https://dl.discordapp.net/apps/linux/%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  x86_64

AutoReqProv:	No

BuildRequires:  desktop-file-utils%{_isa}
BuildRequires:  sed%{_isa}

Requires:       glibc%{_isa}
Requires:       alsa-lib%{_isa}
Requires:       GConf2%{_isa}
Requires:       libnotify%{_isa}
Requires:       nspr%{_isa} >= 4.13
Requires:       nss%{_isa} >= 3.27
Requires:       libX11%{_isa} >= 1.6
Requires:       libXtst%{_isa} >= 1.2
Requires:       libappindicator%{_isa}
Requires:       libcxx%{_isa}

%description
Linux Release for Discord, a free proprietary VoIP application designed for 
gaming communities. 

%prep
%autosetup -n Discord

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/discord
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications

cp -r * $RPM_BUILD_ROOT/%{_libdir}/discord/
ln -sf %{_libdir}/discord/Discord $RPM_BUILD_ROOT/%{_bindir}/
desktop-file-install                            \
--set-icon=%{_libdir}/discord/discord.png       \
--set-key=Exec --set-value=%{_bindir}/Discord   \
--delete-original                               \
--dir=%{buildroot}/%{_datadir}/applications     \
discord.desktop

%files
%defattr(-,root,root)
%{_libdir}/discord/
%{_bindir}/Discord
%{_datadir}/applications/discord.desktop


%changelog
* Tue Dec 12 2017 Sean Callaway <seancallaway@fedoraproject.org> 0.0.3-1
- Update to 0.0.3
- Now using desktop-file-install.
- Removed unneeded requirements.

* Wed Aug 16 2017 Sean Callaway <seancallaway@fedoraproject.org> 0.0.2-1
- Update to 0.0.2
- Spec file cleanup.

* Thu Jan 12 2017 Sean Callaway <seancallaway@fedoraproject.org> 0.0.1-1
- Initial build using version 0.0.1
