Name:           linux-madness-fortune
Version:        1.0
Release:        1%{?dist}
Summary:        Fortune file with absurd, sarcastic, and AI-related tech jokes
License:        WTFPL
Source0:        linux_madness_ascii.tar.gz
BuildArch:      noarch
BuildRequires:  fortune-mod
Requires:       fortune-mod

%description
A collection of over 300 sarcastic, offensive and AI-related fortunes for the command-line fortune program.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/share/games/fortunes
strfile linux_madness
cp linux_madness* %{buildroot}/usr/share/games/fortunes/

%files
/usr/share/games/fortunes/linux_madness
/usr/share/games/fortunes/linux_madness.dat

%changelog
* Thu Jun 19 2025 Alessandro <alessandro@example.com> - 1.0-1
- Initial package with 300+ tech jokes and AI humor
