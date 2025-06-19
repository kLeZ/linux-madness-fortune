Name:           linux-madness-fortune
Version:        1.0
Release:        1%{?dist}
Summary:        Fortune file with absurd, sarcastic, and AI-related tech jokes
License:        WTFPL

BuildArch:      noarch
BuildRequires:  fortune-mod
Requires:       fortune-mod

%description
A collection of over 300 sarcastic, offensive and AI-related fortunes for the command-line fortune program.

%prep
# niente, si lavora direttamente sui file

%build
# niente da compilare

%install
mkdir -p %{buildroot}/usr/share/games/fortunes
strfile linux_madness
cp linux_madness* %{buildroot}/usr/share/games/fortunes/

%files
/usr/share/games/fortunes/linux_madness
/usr/share/games/fortunes/linux_madness.dat

%changelog
* Thu Jun 19 2025 Alessandro <klez@pm.me> - 1.0-1
- Package rebuilt with direct git workflow (no tarball)
