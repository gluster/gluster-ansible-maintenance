%global rolesdir %{_sysconfdir}/ansible/roles/gluster.maintenance
%global docdir %{_datadir}/doc/gluster.maintenance
%global pkgrelease 12

Name:      gluster-ansible-maintenance
Version:   1.0.1
Release:   %{pkgrelease}%{?dist}
Summary:   Ansible roles for GlusterFS infrastructure management

URL:       https://github.com/gluster/gluster-ansible-maintenance
Source0:   %{url}/archive/v%{version}-%{pkgrelease}.tar.gz#/%{name}-%{version}-%{pkgrelease}.tar.gz
License:   GPLv3
BuildArch: noarch

Requires:  ansible-core >= 2.12

%description
Collection of Ansible roles for facilitating the day three operations like
replace-node, replace-brick ...


%prep
%setup -q -n %{name}-%{version}-%{pkgrelease}

%build

%install
mkdir -p %{buildroot}/%{rolesdir}
cp -dpr defaults handlers roles vars tasks LICENSE \
   %{buildroot}/%{rolesdir}

mkdir -p %{buildroot}/%{docdir}
cp -dpr README.md examples %{buildroot}/%{docdir}

%files
%{rolesdir}
%doc %{docdir}

%license LICENSE

%changelog
* Fri Apr 01 2022 Sandro Bonazzola <sbonazzo@redhat.com> - 1.0.1-12
- Rebase on upstream v1.0.1-12

* Fri Aug 31 2018 Sachidananda Urs <sac@redhat.com> 0.1
- Initial release
