%define name xdg-user-dirs
%define version 0.9
%define release %mkrel 1

Summary: XDG user dirs
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://user-dirs.freedesktop.org/releases/%{name}-%{version}.tar.bz2
# (fc) 0.8-2mdv use locale encoding on disk, not UTF-8
Patch0: xdg-user-dirs-0.8-locale.patch
# (fc) 0.8-2mdv disable some default directories
Patch1: xdg-user-dirs-0.8-mdv.patch
# (fc) 0.8-2mdv migrate old Mdk folders
Patch3: xdg-user-dirs-0.8-mdkfolders.patch
License: GPL
Group: System/Libraries
Url: http://www.freedesktop.org/wiki/Software/xdg-user-dirs

%description
xdg-user-dirs is a tool to help manage "well known" user directories
like the desktop folder and the music folder. It also handles
localization (i.e. translation) of the filenames.

%prep
%setup -q
%patch0 -p1 -b .locale
%patch1 -p1 -b .mdv
%patch3 -p1 -b .mdkfolders

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang %name
mkdir -p %buildroot%_sysconfdir/X11/xinit.d/
cat > %buildroot%_sysconfdir/X11/xinit.d/xdg-user-dirs-update << EOF
#!/bin/sh
if [ -x %_bindir/xdg-user-dirs-update ]; then
  %_bindir/xdg-user-dirs-update
fi
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README
%config(noreplace) %_sysconfdir/xdg/user-dirs.conf
%config(noreplace) %_sysconfdir/xdg/user-dirs.defaults
%attr(755,root,root) %_sysconfdir/X11/xinit.d/xdg-user-dirs-update
%_bindir/xdg-user-dir
%_bindir/xdg-user-dirs-update
