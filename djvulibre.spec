Summary: DjVu viewers, encoders and utilities
Name: djvulibre
Version: 3.5.15
Release: 1%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://djvulibre.djvuzone.org/
Source: http://dl.sf.net/djvu/djvulibre-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: xorg-x11-devel, qt-devel, libjpeg-devel, libtiff-devel
BuildRequires: mozilla, redhat-menus
# Provide these here, they're so small, it's not worth splitting them out
Provides: mozilla-djvulibre = %{version}-%{release}
Provides: djvulibre-devel = %{version}-%{release}

%description
DjVu is a web-centric format and software platform for distributing documents
and images.  DjVu content downloads faster, displays and renders faster, looks
nicer on a screen, and consume less client resources than competing formats.
DjVu was originally developed at AT&T Labs-Research by Leon Bottou, Yann
LeCun, Patrick Haffner, and many others.  In March 2000, AT&T sold DjVu to
LizardTech Inc. who now distributes Windows/Mac plug-ins, and commercial
encoders (mostly on Windows)

In an effort to promote DjVu as a Web standard, the LizardTech management was
enlightened enough to release the reference implementation of DjVu under the
GNU GPL in October 2000.  DjVuLibre (which means free DjVu), is an enhanced
version of that code maintained by the original inventors of DjVu. It is
compatible with version 3.5 of the LizardTech DjVu software suite.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
# Move plugin from the netscape directory to the main mozilla one
%{__mkdir_p} %{buildroot}%{_libdir}/mozilla/plugins/
%{__mv} %{buildroot}%{_libdir}/netscape/plugins/nsdejavu.so \
        %{buildroot}%{_libdir}/mozilla/plugins/nsdejavu.so

# Fix for the libs to get stripped correctly (still required in 3.5.15)
find %{buildroot}%{_libdir} -name '*.so*' | xargs %{__chmod} +x

# Move menu entry pixmap to new location
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
%{__mv} %{buildroot}%{_datadir}/pixmaps/djvu.png \
        %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/djvu.png


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig
gtk-update-icon-cache -q -f %{_datadir}/icons/hicolor || :
update-desktop-database /usr/share/applications || :

%postun
/sbin/ldconfig
gtk-update-icon-cache -q -f %{_datadir}/icons/hicolor || :
update-desktop-database /usr/share/applications || :


%files
%defattr(-, root, root, 0755)
%doc README COPYRIGHT COPYING NEWS TODO doc/
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/mozilla/plugins/nsdejavu.so
%{_datadir}/application-registry/djvu.applications
%{_datadir}/applications/djview.desktop
%{_datadir}/icons/hicolor/??x??/apps/djvu.png
%{_datadir}/icons/hicolor/??x??/mimetypes/djvu.png
%{_datadir}/djvu/
%{_datadir}/mime-info/djvu.*
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*

#files devel
#defattr(-, root, root, 0755)
%{_includedir}/libdjvu/
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
* Thu Aug  4 2005 Matthias Saou <http://freshrpms.net/> 3.5.15-1
- Update to 3.5.15.
- Move desktop icon to datadir/icons/hicolor.
- Add gtk-update-icon-cache calls for the new icon.
- Move browser plugin from netscape to mozilla directory instead of symlinking.
- Clean build requirements and add libtiff-devel.
- Add redhat-menus build req since it owns /etc/xdg/menus/applications.menu,
  which the configure script checks to install the desktop file.

* Tue May  3 2005 David Woodhouse <dwmw2@infradead.org> 3.5.14-6
- Remove files that were installed only for older KDE versions.

* Mon Feb 14 2005 David Woodhouse <dwmw2@infradead.org> 3.5.14-4
- Include %%{_datadir}/mimelnk/image/x-djvu.desktop

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 3.5.14-3
- Bump release to provide Extras upgrade path.

* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 3.5.14-2
- Re-enable the lib/mozilla/ symlink to the plugin.
- Add source of /etc/profile.d/qt.sh to fix weird detection problem on FC3...
  ...doesn't fix it, some lib required by qt is probably installed after and
  ldconfig not run.
- Added lib +x chmod'ing to get proper stripping and debuginfo package.

* Sat Oct 16 2004 Matthias Saou <http://freshrpms.net/> 3.5.14-2
- Added update-desktop-database scriplet calls.

* Mon Aug 16 2004 Matthias Saou <http://freshrpms.net/> 3.5.14-1
- Update to 3.5.14.
- Added newly introduced files to the package.

* Mon May 17 2004 Matthias Saou <http://freshrpms.net/> 3.5.13-1
- Update to 3.5.13.
- Added new Japanese man pages.

* Wed May  5 2004 Matthias Saou <http://freshrpms.net/> 3.5.12-4
- Changed the plugin directory for mozilla to %{_libdir}/mozilla,
  as suggested by Matteo Corti.
- Shortened the description.

* Wed Jan 14 2004 Matthias Saou <http://freshrpms.net/> 3.5.12-3
- Added XFree86-devel and libjpeg-devel build requirements.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 3.5.12-2
- Rebuild for Fedora Core 1.

* Mon Sep  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.5.12.

* Thu May  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.5.11.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Mar 20 2003 Matthias Saou <http://freshrpms.net/>
- Update to 3.5.10.

* Wed Jul 24 2002 Matthias Saou <http://freshrpms.net/>
- Update to 3.5.7.

* Fri Jul 19 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup and fixes.

* Wed May 29 2002 Leon Bottou <leon@bottou.org>
- bumped to version 3.5.6-1

* Mon Apr 1 2002 Leon Bottou <leonb@users.sourceforge.net>
- bumped to version 3.5.5-2
- changed group to Applications/Publishing

* Tue Mar 25 2002 Leon Bottou <leonb@users.sourceforge.net>
- bumped to version 3.5.5-2

* Tue Jan 22 2002 Leon Bottou <leonb@users.sourceforge.net>
- bumped to version 3.5.4-1.
- fixed for properly locating the man directory.
- bumped to version 3.5.4-2.

* Wed Jan 16 2002 Leon Bottou <leonb@users.sourceforge.net>
- bumped to version 3.5.3-1

* Fri Dec  7 2001 Leon Bottou <leonb@users.sourceforge.net>
- bumped to version 3.5.2-1.

* Wed Dec  5 2001 Leon Bottou <leonb@users.sourceforge.net>
- created spec file for rh7.x.

