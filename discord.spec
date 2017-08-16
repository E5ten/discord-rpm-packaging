%global         debug_package %{nil}
%global         __strip /bin/true

Name:           discord
Version:        0.0.2
Release:        1%{?dist}
Summary:        All-in-one voice and text chat for gamers

License:        Proprietary
URL:            https://discordapp.com/
Source0:        https://dl.discordapp.net/apps/linux/%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:	x86_64

BuildRequires:  libXScrnSaver%{_isa}
BuildRequires:  sed%{_isa}

Requires:       glibc%{_isa}
Requires:       alsa-lib%{_isa}
Requires:       GConf2%{_isa}
Requires:       libnotify%{_isa}
Requires:       nspr%{_isa} >= 4.13
Requires:       nss%{_isa} >= 3.27
Requires:       libstdc++%{_isa} >= 6
Requires:       libX11%{_isa} >= 1.6
Requires:       libXtst%{_isa} >= 1.2
Requires:       libappindicator%{_isa}
Requires:       libcxx%{_isa}


%description
Linux Release for Discord, a free proprietary VoIP application designed for 
gaming communities. 

%prep
%autosetup -n Discord
# Fix the .desktop file, as their paths are incorrect.
sed -i 's|^Exec=.*|Exec=%{_bindir}/Discord|g' discord.desktop
sed -i 's|^Icon=.*|Icon=%{_libdir}/discord/discord.png|g' discord.desktop

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/discord
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications

cp -r * $RPM_BUILD_ROOT/%{_libdir}/discord/
ln -sf %{_libdir}/discord/Discord $RPM_BUILD_ROOT/%{_bindir}/
install -m 755 discord.desktop %{buildroot}/%{_datadir}/applications/

%files
%defattr(-,root,root)
%{_libdir}/discord/
%{_bindir}/Discord
%{_datadir}/applications/discord.desktop


%changelog
* Wed Aug 16 2017 Sean Callaway <seancallaway@fedoraproject.org> 0.0.2-1
- Update to 0.0.2
- Spec file cleanup.

* Thu Jan 12 2017 Sean Callaway <seancallaway@fedoraproject.org> 0.0.1-1
- Initial build using version 0.0.1
