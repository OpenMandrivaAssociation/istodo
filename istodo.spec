# Debug is empty here
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Organizer for students
Name:		istodo
Version:	1.2
Release:	1
License:	Freeware
Group:		Education
Url:		http://istodo.ru/
Source0:	http://istodo.ru/distribs/%{name}-linux-%{version}-i386.tar.gz
Source1:	http://istodo.ru/distribs/%{name}-linux-%{version}-amd64.tar.gz
ExclusiveArch:	%{ix86} x86_64

%description
iStodo is an organizer for students with scheduling and planning features.

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*

#----------------------------------------------------------------------------

%prep
%setup -q -T -c
%ifarch %{ix86}
tar -xf %{SOURCE0}
%else
tar -xf %{SOURCE1}
%endif

%build

%install
pushd %{name}-linux-%{version}-*

mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

sed -i s,"Version=.*","Version=1.0", %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install icons of various sizes.
for s in 256 128 64 48 32 ; do
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
    cp icons/${s}x${s}/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done

popd
