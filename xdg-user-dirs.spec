%define _disable_rebuild_configure 1

Summary:	XDG user dirs
Name:		xdg-user-dirs
Version:	0.17
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://freedesktop.org/wiki/Software/xdg-user-dirs
Source0:	http://user-dirs.freedesktop.org/releases/%{name}-%{version}.tar.gz
# (fc) 0.8-2mdv use locale encoding on disk, not UTF-8
Patch0:		xdg-user-dirs-0.8-locale.patch
# (fc) 0.8-2mdv disable some default directories
Patch1:		xdg-user-dirs-0.11-mdv.patch
# (fc) 0.8-2mdv migrate old Mdk folders
Patch3:		xdg-user-dirs-0.13-mdkfolders.patch
BuildRequires:	xsltproc
BuildRequires:	docbook-style-xsl

%description
xdg-user-dirs is a tool to help manage "well known" user directories
like the desktop folder and the music folder. It also handles
localization (i.e. translation) of the filenames.

%prep
%setup -q
%apply_patches

%build
%configure
%make

make -C po update-po

%install
%makeinstall_std

%find_lang %{name}

mkdir -p %{buildroot}%{_sysconfdir}/X11/xinit.d/
cat > %{buildroot}%{_sysconfdir}/X11/xinit.d/xdg-user-dirs-update << EOF
#!/bin/sh
if [ -x %{_bindir}/xdg-user-dirs-update ]; then
  %{_bindir}/xdg-user-dirs-update
fi
EOF

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.conf
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.defaults
%attr(755,root,root) %{_sysconfdir}/X11/xinit.d/xdg-user-dirs-update
%{_sysconfdir}/xdg/autostart/xdg-user-dirs.desktop
%{_bindir}/xdg-user-dir
%{_bindir}/xdg-user-dirs-update
%{_mandir}/man1/xdg-user-dir.1.*
%{_mandir}/man1/xdg-user-dirs-update.1.*
%{_mandir}/man5/user-dirs.conf.5.*
%{_mandir}/man5/user-dirs.defaults.5.*
%{_mandir}/man5/user-dirs.dirs.5.*
