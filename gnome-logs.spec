#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-logs
Version  : 42.0
Release  : 20
URL      : https://download.gnome.org/sources/gnome-logs/42/gnome-logs-42.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-logs/42/gnome-logs-42.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: gnome-logs-bin = %{version}-%{release}
Requires: gnome-logs-data = %{version}-%{release}
Requires: gnome-logs-license = %{version}-%{release}
Requires: gnome-logs-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : desktop-file-utils
BuildRequires : glib-dev
BuildRequires : gtk3-dev
BuildRequires : itstool
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(libhandy-1)
BuildRequires : pkgconfig(libsystemd)

%description
GNOME Logs is a log viewer for the systemd journal
https://wiki.gnome.org/Apps/Logs

%package bin
Summary: bin components for the gnome-logs package.
Group: Binaries
Requires: gnome-logs-data = %{version}-%{release}
Requires: gnome-logs-license = %{version}-%{release}

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
%setup -q -n gnome-logs-42.0
cd %{_builddir}/gnome-logs-42.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648495183
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-logs
cp %{_builddir}/gnome-logs-42.0/COPYING %{buildroot}/usr/share/package-licenses/gnome-logs/8624bcdae55baeef00cd11d5dfcfa60f68710a02
DESTDIR=%{buildroot} ninja -C builddir install
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
/usr/share/gnome-logs/gl-style.css
/usr/share/icons/hicolor/scalable/apps/org.gnome.Logs.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Logs-symbolic.svg
/usr/share/metainfo/org.gnome.Logs.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/gnome-logs/index.page
/usr/share/help/C/gnome-logs/introduction.page
/usr/share/help/C/gnome-logs/legal.xml
/usr/share/help/C/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/C/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/C/gnome-logs/permissions.page
/usr/share/help/ca/gnome-logs/index.page
/usr/share/help/ca/gnome-logs/introduction.page
/usr/share/help/ca/gnome-logs/legal.xml
/usr/share/help/ca/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/ca/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/ca/gnome-logs/permissions.page
/usr/share/help/cs/gnome-logs/index.page
/usr/share/help/cs/gnome-logs/introduction.page
/usr/share/help/cs/gnome-logs/legal.xml
/usr/share/help/cs/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/cs/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/cs/gnome-logs/permissions.page
/usr/share/help/da/gnome-logs/index.page
/usr/share/help/da/gnome-logs/introduction.page
/usr/share/help/da/gnome-logs/legal.xml
/usr/share/help/da/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/da/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/da/gnome-logs/permissions.page
/usr/share/help/de/gnome-logs/index.page
/usr/share/help/de/gnome-logs/introduction.page
/usr/share/help/de/gnome-logs/legal.xml
/usr/share/help/de/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/de/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/de/gnome-logs/permissions.page
/usr/share/help/el/gnome-logs/index.page
/usr/share/help/el/gnome-logs/introduction.page
/usr/share/help/el/gnome-logs/legal.xml
/usr/share/help/el/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/el/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/el/gnome-logs/permissions.page
/usr/share/help/en_GB/gnome-logs/index.page
/usr/share/help/en_GB/gnome-logs/introduction.page
/usr/share/help/en_GB/gnome-logs/legal.xml
/usr/share/help/en_GB/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/en_GB/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/en_GB/gnome-logs/permissions.page
/usr/share/help/es/gnome-logs/index.page
/usr/share/help/es/gnome-logs/introduction.page
/usr/share/help/es/gnome-logs/legal.xml
/usr/share/help/es/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/es/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/es/gnome-logs/permissions.page
/usr/share/help/eu/gnome-logs/index.page
/usr/share/help/eu/gnome-logs/introduction.page
/usr/share/help/eu/gnome-logs/legal.xml
/usr/share/help/eu/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/eu/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/eu/gnome-logs/permissions.page
/usr/share/help/fr/gnome-logs/index.page
/usr/share/help/fr/gnome-logs/introduction.page
/usr/share/help/fr/gnome-logs/legal.xml
/usr/share/help/fr/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/fr/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/fr/gnome-logs/permissions.page
/usr/share/help/gl/gnome-logs/index.page
/usr/share/help/gl/gnome-logs/introduction.page
/usr/share/help/gl/gnome-logs/legal.xml
/usr/share/help/gl/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/gl/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/gl/gnome-logs/permissions.page
/usr/share/help/hu/gnome-logs/index.page
/usr/share/help/hu/gnome-logs/introduction.page
/usr/share/help/hu/gnome-logs/legal.xml
/usr/share/help/hu/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/hu/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/hu/gnome-logs/permissions.page
/usr/share/help/id/gnome-logs/index.page
/usr/share/help/id/gnome-logs/introduction.page
/usr/share/help/id/gnome-logs/legal.xml
/usr/share/help/id/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/id/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/id/gnome-logs/permissions.page
/usr/share/help/ko/gnome-logs/index.page
/usr/share/help/ko/gnome-logs/introduction.page
/usr/share/help/ko/gnome-logs/legal.xml
/usr/share/help/ko/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/ko/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/ko/gnome-logs/permissions.page
/usr/share/help/nl/gnome-logs/index.page
/usr/share/help/nl/gnome-logs/introduction.page
/usr/share/help/nl/gnome-logs/legal.xml
/usr/share/help/nl/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/nl/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/nl/gnome-logs/permissions.page
/usr/share/help/pl/gnome-logs/index.page
/usr/share/help/pl/gnome-logs/introduction.page
/usr/share/help/pl/gnome-logs/legal.xml
/usr/share/help/pl/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/pl/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/pl/gnome-logs/permissions.page
/usr/share/help/pt/gnome-logs/index.page
/usr/share/help/pt/gnome-logs/introduction.page
/usr/share/help/pt/gnome-logs/legal.xml
/usr/share/help/pt/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/pt/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/pt/gnome-logs/permissions.page
/usr/share/help/pt_BR/gnome-logs/index.page
/usr/share/help/pt_BR/gnome-logs/introduction.page
/usr/share/help/pt_BR/gnome-logs/legal.xml
/usr/share/help/pt_BR/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/pt_BR/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/pt_BR/gnome-logs/permissions.page
/usr/share/help/ru/gnome-logs/index.page
/usr/share/help/ru/gnome-logs/introduction.page
/usr/share/help/ru/gnome-logs/legal.xml
/usr/share/help/ru/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/ru/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/ru/gnome-logs/permissions.page
/usr/share/help/sv/gnome-logs/index.page
/usr/share/help/sv/gnome-logs/introduction.page
/usr/share/help/sv/gnome-logs/legal.xml
/usr/share/help/sv/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/sv/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/sv/gnome-logs/permissions.page
/usr/share/help/tr/gnome-logs/index.page
/usr/share/help/tr/gnome-logs/introduction.page
/usr/share/help/tr/gnome-logs/legal.xml
/usr/share/help/tr/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/tr/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/tr/gnome-logs/permissions.page
/usr/share/help/uk/gnome-logs/index.page
/usr/share/help/uk/gnome-logs/introduction.page
/usr/share/help/uk/gnome-logs/legal.xml
/usr/share/help/uk/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/uk/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/uk/gnome-logs/permissions.page
/usr/share/help/zh_CN/gnome-logs/index.page
/usr/share/help/zh_CN/gnome-logs/introduction.page
/usr/share/help/zh_CN/gnome-logs/legal.xml
/usr/share/help/zh_CN/gnome-logs/media/gnome-logs-3-34.png
/usr/share/help/zh_CN/gnome-logs/media/org.gnome.Logs.svg
/usr/share/help/zh_CN/gnome-logs/permissions.page

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-logs/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files locales -f gnome-logs.lang
%defattr(-,root,root,-)

