%global rolesdir %{_sysconfdir}/ansible/roles/gluster.maintenance
%global docdir %{_datadir}/doc/gluster.maintenance
%global buildnum 1

Name:      gluster-ansible-maintenance
Version:   1.0.0
Release:   1%{?dist}
Summary:   Ansible roles for GlusterFS infrastructure management

URL:       https://github.com/gluster/gluster-ansible-maintenance
Source0:   %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}-%{buildnum}.tar.gz
License:   GPLv3
BuildArch: noarch

Requires:  ansible-core >= 2.12

%description
Collection of Ansible roles for facilitating the day three operations like
replace-node, replace-brick ...


%prep
%autosetup -p1

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
* Thu Feb 21 2019 Sachidananda Urs <sac@redhat.com> 1.0.0-1
- Bump the version number to 1

* Fri Aug 31 2018 Sachidananda Urs <sac@redhat.com> 0.1
- Initial release
