Name:       disable-kalman-filter
Version:    0.1
Release:    1%{?dist}
Summary:    Patch to disable kalman filter on Jolla C
License:    LGPLv2
Source:     %{name}.tar.gz
URL:        https://github.com/toxip/disable-kalman-filter
BuildArch:  noarch
Packager:   toxip
Requires:   patchmanager
Requires:   sailfish-version >= 2.1.0

%description
Improves screen responsiveness on Jolla C by disabling kalman filter

%define debug_package %{nil}

%prep
%setup -q -n %{name}

%build
%qmake5

%install
rm -rf %{buildroot}
%qmake5_install

%files
/usr/share/patchmanager/patches/%{name}/

%pre
if [ -d /usr/share/patchmanager/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
/usr/sbin/patchmanager -u %{name} || true