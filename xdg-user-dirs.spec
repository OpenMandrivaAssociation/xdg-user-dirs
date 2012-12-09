Summary:	XDG user dirs
Name:		xdg-user-dirs
Version:	0.14
Release:	%mkrel 3
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


%changelog
* Sat May 21 2011 Götz Waschk <waschk@mandriva.org> 0.14-1mdv2011.0
+ Revision: 676596
- update to new version 0.14

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.13-2
+ Revision: 671293
- mass rebuild

* Wed Sep 15 2010 Götz Waschk <waschk@mandriva.org> 0.13-1mdv2011.0
+ Revision: 578426
- new version
- rediff patch 3
- drop patch 5

* Fri Sep 03 2010 Götz Waschk <waschk@mandriva.org> 0.12-4mdv2011.0
+ Revision: 575627
- rebuild
- update patch 5 to fix all translations

* Thu Sep 02 2010 Götz Waschk <waschk@mandriva.org> 0.12-2mdv2011.0
+ Revision: 575540
- fix russian translation (bug #54244)

* Mon Nov 23 2009 Götz Waschk <waschk@mandriva.org> 0.12-1mdv2010.1
+ Revision: 469293
- new version
- drop patch 5

* Tue Oct 06 2009 Frederic Crozat <fcrozat@mandriva.com> 0.11-2mdv2010.0
+ Revision: 454544
- Patch5 (upstream): update po files

* Sat Sep 26 2009 Frederik Himpe <fhimpe@mandriva.org> 0.11-1mdv2010.0
+ Revision: 449613
- Update to new version 0.11
- Rediff mdv patch

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.10-7mdv2009.1
+ Revision: 351211
- rebuild

* Fri Sep 19 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.10-6mdv2009.0
+ Revision: 285917
- new license policy
- s,,%%{_buildroot}
- get rid of stupid redefines
- fix mixture of tabs and spaces
- spec file clean
- really apply the patch

  + Götz Waschk <waschk@mandriva.org>
    - really update patch 1

* Thu Sep 18 2008 Götz Waschk <waschk@mandriva.org> 0.10-4mdv2009.0
+ Revision: 285600
- reenable templates (bug #43965)

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.10-3mdv2009.0
+ Revision: 226026
- rebuild

* Thu Mar 06 2008 Frederic Crozat <fcrozat@mandriva.com> 0.10-2mdv2008.1
+ Revision: 180882
- Patch4: handle HOME overriding pw_dir

* Tue Feb 12 2008 Götz Waschk <waschk@mandriva.org> 0.10-1mdv2008.1
+ Revision: 166142
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 28 2007 Götz Waschk <waschk@mandriva.org> 0.9-1mdv2008.0
+ Revision: 72503
- new version
- drop patch 2

* Thu Aug 02 2007 Frederic Crozat <fcrozat@mandriva.com> 0.8-2mdv2008.0
+ Revision: 58255
- Patch0: use locale encoding on disk, not always UTF-8
- Patch1: disable some default directories (template, public sharing)
- Patch2 (CVS): fix crashes
- Patch3: migrate old Mdk folders to the new system (directory names preserved)

* Tue May 29 2007 Götz Waschk <waschk@mandriva.org> 0.8-1mdv2008.0
+ Revision: 32480
- new version
- fix URL

* Wed Apr 25 2007 Götz Waschk <waschk@mandriva.org> 0.6-2mdv2008.0
+ Revision: 18327
- start from xinit.d

* Tue Apr 17 2007 Götz Waschk <waschk@mandriva.org> 0.6-1mdv2007.1
+ Revision: 13559
- Import xdg-user-dirs



* Wed Apr 11 2007 Götz Waschk <waschk@mandriva.org> 0.6-1mdv2007.1
- initial package
