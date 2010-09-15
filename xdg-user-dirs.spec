Summary:	XDG user dirs
Name:		xdg-user-dirs
Version:	0.13
Release:	%mkrel 1
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
# (fc) 0.10-2mdv handle HOME overriding pw_dir
Patch4:		xdg-user-dirs-0.10-home.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
xdg-user-dirs is a tool to help manage "well known" user directories
like the desktop folder and the music folder. It also handles
localization (i.e. translation) of the filenames.

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

make -C po update-po

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

mkdir -p %{buildroot}%{_sysconfdir}/X11/xinit.d/
cat > %{buildroot}%{_sysconfdir}/X11/xinit.d/xdg-user-dirs-update << EOF
#!/bin/sh
if [ -x %{_bindir}/xdg-user-dirs-update ]; then
  %{_bindir}/xdg-user-dirs-update
fi
EOF

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.conf
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.defaults
%attr(755,root,root) %{_sysconfdir}/X11/xinit.d/xdg-user-dirs-update
%{_bindir}/xdg-user-dir
%{_bindir}/xdg-user-dirs-update
