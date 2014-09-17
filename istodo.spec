Summary:	Organizer for students
Name:		istodo
Version:	1.3.0
Release:	1
License:	GPLv3+
Group:		Education
Url:		http://istodo.ru/
# Repack from http://dev.istodo.ru/istodo-desktop/get/v%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
Patch0:		istodo-1.3.0-no-iOS.patch
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)

%description
iStodo is an organizer for students with scheduling and planning features.

%files
%doc linux_deploy_1.0/source_amd64/license.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%qmake_qt5
%make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 desktop/iStodo %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 linux_deploy_1.0/source_amd64/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i s,"Version=.*","Version=1.0", %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install icons of various sizes.
for s in 256 128 64 48 32 ; do
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
    cp linux_deploy_1.0/source_amd64/icons/${s}x${s}/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done

