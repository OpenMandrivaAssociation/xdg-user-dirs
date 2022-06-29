%define _disable_rebuild_configure 1

Summary:	XDG user dirs
Name:		xdg-user-dirs
Version:	0.17
Release:	4
License:	GPLv2+
Group:		System/Libraries
Url:		http://freedesktop.org/wiki/Software/xdg-user-dirs
Source0:	http://user-dirs.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Systemd integration, shamelessly stolen from Arch
Source1:	https://raw.githubusercontent.com/archlinux/svntogit-packages/packages/xdg-user-dirs/trunk/xdg-user-dirs-update.service
# (fc) 0.8-2mdv use locale encoding on disk, not UTF-8
Patch0:		xdg-user-dirs-0.8-locale.patch
# (fc) 0.8-2mdv disable some default directories
Patch1:		xdg-user-dirs-0.11-mdv.patch
# (fc) 0.8-2mdv migrate old Mdk folders
Patch3:		xdg-user-dirs-0.13-mdkfolders.patch
Patch4:		http://svnweb.mageia.org/packages/cauldron/xdg-user-dirs/current/SOURCES/xdg-user-dirs-fdo-use-fuzzy.patch
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl
BuildRequires:	systemd-rpm-macros
Requires:	filesystem

%description
xdg-user-dirs is a tool to help manage "well known" user directories
like the desktop folder and the music folder. It also handles
localization (i.e. translation) of the filenames.

%prep
%autosetup -p1
%configure

%build
%make_build
make -C po update-po

%install
%make_install

mkdir -p %{buildroot}%{_userunitdir}
install -c -m 644 %{S:1} %{buildroot}%{_userunitdir}/xdg-user-dirs-update.service

install -d %{buildroot}%{_userpresetdir}
cat > %{buildroot}%{_userpresetdir}/86-%{name}.preset << EOF
enable xdg-user-dirs-update.service
EOF

# We use the systemd service instead
rm -rf %{buildroot}%{_sysconfdir}/xdg/autostart

%find_lang %{name}

%post
%systemd_user_post xdg-user-dirs-update.service

%preun
%systemd_user_preun xdg-user-dirs-update.service

%files -f %{name}.lang
%doc AUTHORS NEWS README
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.conf
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.defaults
%{_userpresetdir}/86-%{name}.preset
%{_userunitdir}/xdg-user-dirs-update.service
%{_bindir}/xdg-user-dir
%{_bindir}/xdg-user-dirs-update
%doc %{_mandir}/man?/*.*
