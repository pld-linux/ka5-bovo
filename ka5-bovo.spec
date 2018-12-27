%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		bovo
Summary:	A Gomoku like game
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	eccd654f5f77cc0d5591273fd80f5a27
URL:		http://www.kde.org/
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= 18.12.0
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.30.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bovo is a Gomoku like game for two players, where the opponents
alternate in placing their respective pictogram on the game board.
(Also known as: Connect Five, Five in a row, X and O, Naughts and
Crosses)

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bovo
%{_desktopdir}/org.kde.bovo.desktop
%{_datadir}/bovo
%{_iconsdir}/hicolor/128x128/apps/bovo.png
%{_iconsdir}/hicolor/16x16/apps/bovo.png
%{_iconsdir}/hicolor/22x22/apps/bovo.png
%{_iconsdir}/hicolor/32x32/apps/bovo.png
%{_iconsdir}/hicolor/48x48/apps/bovo.png
%{_iconsdir}/hicolor/64x64/apps/bovo.png
%dir %{_datadir}/kxmlgui5/bovo
%{_datadir}/kxmlgui5/bovo/bovoui.rc
%{_datadir}/metainfo/org.kde.bovo.appdata.xml
