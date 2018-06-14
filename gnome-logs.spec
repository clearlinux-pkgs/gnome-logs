#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-logs
Version  : 3.28.3
Release  : 6
URL      : https://download.gnome.org/sources/gnome-logs/3.28/gnome-logs-3.28.3.tar.xz
Source0  : https://download.gnome.org/sources/gnome-logs/3.28/gnome-logs-3.28.3.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: gnome-logs-bin
Requires: gnome-logs-data
Requires: gnome-logs-license
Requires: gnome-logs-locales
BuildRequires : desktop-file-utils
BuildRequires : gettext
BuildRequires : glib-dev
BuildRequires : gtk3-dev
BuildRequires : itstool
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : meson
BuildRequires : ninja
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gsettings-desktop-schemas)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : python3
BuildRequires : sed

%description
GNOME Logs is a log viewer for the systemd journal
https://wiki.gnome.org/Apps/Logs

%package bin
Summary: bin components for the gnome-logs package.
Group: Binaries
Requires: gnome-logs-data
Requires: gnome-logs-license

%description bin
bin components for the gnome-logs package.


%package data
Summary: data components for the gnome-logs package.
Group: Data

%description data
data components for the gnome-logs package.


%package doc
Summary: doc components for the gnome-logs package.
Group: Documentation

%description doc
doc components for the gnome-logs package.


%package license
Summary: license components for the gnome-logs package.
Group: Default

%description license
license components for the gnome-logs package.


%package locales
Summary: locales components for the gnome-logs package.
Group: Default

%description locales
locales components for the gnome-logs package.


%prep
%setup -q -n gnome-logs-3.28.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528992706
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1528992706
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/gnome-logs
cp COPYING %{buildroot}/usr/share/doc/gnome-logs/COPYING
%make_install
%find_lang gnome-logs

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-logs

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Logs.desktop
/usr/share/dbus-1/services/org.gnome.Logs.service
/usr/share/glib-2.0/schemas/org.gnome.Logs.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.Logs.gschema.xml
/usr/share/icons/hicolor/16x16/apps/gnome-logs.png
/usr/share/icons/hicolor/22x22/apps/gnome-logs.png
/usr/share/icons/hicolor/24x24/apps/gnome-logs.png
/usr/share/icons/hicolor/256x256/apps/gnome-logs.png
/usr/share/icons/hicolor/32x32/apps/gnome-logs.png
/usr/share/icons/hicolor/48x48/apps/gnome-logs.png
/usr/share/icons/hicolor/512x512/apps/gnome-logs.png
/usr/share/icons/hicolor/symbolic/apps/gnome-logs-symbolic.svg
/usr/share/metainfo/org.gnome.Logs.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/gnome-logs/index.page
/usr/share/help/C/gnome-logs/introduction.page
/usr/share/help/C/gnome-logs/legal.xml
/usr/share/help/C/gnome-logs/media/gnome-logs-3-12.png
/usr/share/help/C/gnome-logs/media/gnome-logs.png
/usr/share/help/C/gnome-logs/permissions.page
/usr/share/help/cs/gnome-logs/index.page
/usr/share/help/cs/gnome-logs/introduction.page
/usr/share/help/cs/gnome-logs/legal.xml
/usr/share/help/cs/gnome-logs/media/gnome-logs-3-12.png
/usr/share/help/cs/gnome-logs/media/gnome-logs.png
/usr/share/help/cs/gnome-logs/permissions.page
/usr/share/help/da/gnome-logs/index.page
/usr/share/help/da/gnome-logs/introduction.page
/usr/share/help/da/gnome-logs/legal.xml
/usr/share/help/da/gnome-logs/media/gnome-logs-3-12.png
/usr/share/help/da/gnome-logs/media/gnome-logs.png
/usr/share/help/da/gnome-logs/permissions.page
/usr/share/help/de/gnome-logs/index.page
/usr/share/help/de/gnome-logs/introduction.page
/usr/share/help/de/gnome-logs/legal.xml
/usr/share/help/de/gnome-logs/media/gnome-logs-3-12.png
/usr/share/help/de/gnome-logs/media/gnome-logs.png
/usr/share/help/de/gnome-logs/permissions.page
/usr/share/help/el/gnome-logs/index.page
/usr/share/help/el/gnome-logs/introduction.page
/usr/share/help/el/gnome-logs/legal.xml
/usr/share/help/el/gnome-logs/media/gnome-logs-3-12.png
/usr/share/help/el/gnome-logs/media/gnome-logs.png
/usr/share/help/el/gnome-logs/permissions.page
/usr/share/help/es/gnome-logs/index.page
/usr/share/help/es/gnome-logs/introduction.page
/usr/share/help/es/gnome-logs/legal.xml
/usr/share/help/es/gnome-logs/media/gnome-logs-3-12.png
/usr/share/help/es/gnome-logs/media/gnome-logs.png
/usr/share/help/es/gnome-logs/permissions.page
/usr/share/help/fr/gnome-logs/index.page
/usr/share/help/fr/gnome-logs/introduction.page
/usr/share/help/fr/gnome-logs/legal.xml
/usr/share/help/fr/gnome-logs/media/gnome-logs-3-12.png
/usr/share/help/fr/gnome-logs/media/gnome-logs.png
/usr/share/help/fr/gnome-logs/permissions.page
/usr/share/help/gl/gnome-logs/index.page
/usr/share/help/gl/gnome-logs/introduction.page
/usr/share/help/gl/gnome-logs/legal.xml
/usr/share/help/gl/gnome-logs/media/gnome-logs-3-12.png
/usr/share/help/gl/gnome-logs/media/gnome-logs.png
/usr/share/help/gl/gnome-logs/permissions.page
/usr/share/help/hu/gnome-logs/index.page
/usr/share/help/hu/gnome-logs/introduction.page
/usr/share/help/hu/gnome-logs/legal.xml
/usr/share/help/hu/gnome-logs/media/gnome-logs-3-12.png
/usr/share/help/hu/gnome-logs/media/gnome-logs.png
/usr/share/help/hu/gnome-logs/permissions.page
/usr/share/help/ko/gnome-logs/index.page
/usr/share/help/ko/gnome-logs/introduction.page
/usr/share/help/ko/gnome-logs/legal.xml
/usr/share/help/ko/gnome-logs/media/gnome-logs-3-12.png
/usr/share/help/ko/gnome-logs/media/gnome-logs.png
/usr/share/help/ko/gnome-logs/permissions.page
/usr/share/help/pl/gnome-logs/index.page
/usr/share/help/pl/gnome-logs/introduction.page
/usr/share/help/pl/gnome-logs/legal.xml
/usr/share/help/pl/gnome-logs/media/gnome-logs-3-12.png
/usr/share/help/pl/gnome-logs/media/gnome-logs.png
/usr/share/help/pl/gnome-logs/permissions.page
/usr/share/help/pt_BR/gnome-logs/index.page
/usr/share/help/pt_BR/gnome-logs/introduction.page
/usr/share/help/pt_BR/gnome-logs/legal.xml
/usr/share/help/pt_BR/gnome-logs/media/gnome-logs-3-12.png
/usr/share/help/pt_BR/gnome-logs/media/gnome-logs.png
/usr/share/help/pt_BR/gnome-logs/permissions.page
/usr/share/help/ru/gnome-logs/index.page
/usr/share/help/ru/gnome-logs/introduction.page
/usr/share/help/ru/gnome-logs/legal.xml
/usr/share/help/ru/gnome-logs/media/gnome-logs-3-12.png
/usr/share/help/ru/gnome-logs/media/gnome-logs.png
/usr/share/help/ru/gnome-logs/permissions.page
/usr/share/help/sv/gnome-logs/index.page
/usr/share/help/sv/gnome-logs/introduction.page
/usr/share/help/sv/gnome-logs/legal.xml
/usr/share/help/sv/gnome-logs/media/gnome-logs-3-12.png
/usr/share/help/sv/gnome-logs/media/gnome-logs.png
/usr/share/help/sv/gnome-logs/permissions.page

%files license
%defattr(-,root,root,-)
/usr/share/doc/gnome-logs/COPYING

%files locales -f gnome-logs.lang
%defattr(-,root,root,-)

