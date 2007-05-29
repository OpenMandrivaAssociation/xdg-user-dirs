%define name xdg-user-dirs
%define version 0.8
%define release %mkrel 1

Summary: XDG user dirs
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://user-dirs.freedesktop.org/releases/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Libraries
Url: http://www.freedesktop.org/wiki/Software/xdg-user-dirs
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
xdg-user-dirs is a tool to help manage "well known" user directories
like the desktop folder and the music folder. It also handles
localization (i.e. translation) of the filenames.

%prep
%setup -q

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
%_bindir/xdg-user-dirs-update
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
