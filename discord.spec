Name:           discord
Version:        0.0.1
Release:        1%{?dist}
Summary:        All-in-one voice and text chat for gamers

License:        Proprietary
URL:            https://discordapp.com/
Source0:        https://dl.discordapp.net/apps/linux/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  libXScrnSaver
AutoReqProv:    no

%description
Linux Release for Discord, a free proprietary VoIP application designed for 
gaming communities. 

%global debug_package %{nil}

%prep
%autosetup -n Discord
# Fix the .desktop file, as their paths are incorrect.
sed -i 's|^Exec=.*|Exec=/usr/bin/Discord|g' discord.desktop
sed -i 's|^Icon=.*|Icon=/usr/lib64/discord/discord.png|g' discord.desktop

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
mkdir -p $RPM_BUILD_ROOT/usr/lib64/discord
mkdir -p $RPM_BUILD_ROOT/usr/share/applications

cp -r * $RPM_BUILD_ROOT/usr/lib64/discord/
ln -sf /usr/lib64/discord/Discord $RPM_BUILD_ROOT/%{_bindir}/
install -m 755 discord.desktop %{buildroot}/%{_datadir}/applications/

%files
%defattr(-,root,root)
/usr/lib64/discord/
%{_bindir}/Discord
/usr/share/applications/discord.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Jan 12 2017 Sean Callaway <seancallaway@fedoraproject.org> 0.0.1-1
- Initial build using version 0.0.1
