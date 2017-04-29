%if 0%{?fedora}
%global with_python3 1
%endif
%global package_name ara

Name:           %{package_name}
Version:        0.13.0
Release:        1%{?dist}
Summary:        ARA: Ansible Analysis - Record and visualize Ansible Playbook runs

License:        ASL 2.0
URL:            https://git.openstack.org/cgit/openstack/ara
Source0:        https://dmsimard.com/%{package_name}-%{version}.tar.gz
#Source0:        https://pypi.io/packages/source/a/%{package_name}/%{package_name}-%{version}.tar.gz
Source1:        ara-server.service
Source2:        ara.cfg
Source3:        ara.logrotate
BuildArch:      noarch

%{?systemd_requires}
BuildRequires: systemd

Requires:       python2-%{package_name} = %{version}-%{release}
Requires:       %{package_name}-common = %{version}-%{release}

%description
ARA: Ansible Run Analysis

ARA records Ansible Playbook runs seamlessly to make them easier to visualize,
understand and troubleshoot. It integrates with Ansible wherever you run it.

%if 0%{?with_python3}
%package -n %{package_name}-python3
Summary:        %{summary}

%{?systemd_requires}
BuildRequires: systemd

Requires:       python3-%{package_name} = %{version}-%{release}
Requires:       %{package_name}-common = %{version}-%{release}

%description -n %{package_name}-python3
ARA: Ansible Run Analysis

ARA records Ansible Playbook runs seamlessly to make them easier to visualize,
understand and troubleshoot. It integrates with Ansible wherever you run it.
%endif

%package -n python2-%{package_name}
Summary:        %{summary}

BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools
BuildRequires:  gcc
BuildRequires:  libffi-devel
BuildRequires:  openssl-devel
BuildRequires:  redhat-rpm-config
BuildRequires:  git
# Test dependencies for %check
BuildRequires:  ansible >= 2.1.5.0
BuildRequires:  python-cliff
BuildRequires:  python2-debtcollector
BuildRequires:  python2-decorator >= 4.0.0
BuildRequires:  python2-flask
BuildRequires:  python2-flask-migrate
BuildRequires:  python-flask-script
BuildRequires:  python-frozen-flask
BuildRequires:  python2-junit_xml
BuildRequires:  python2-lxml
BuildRequires:  python2-pygments
BuildRequires:  python2-sqlalchemy
BuildRequires:  python2-XStatic
BuildRequires:  python2-XStatic-Bootstrap-SCSS
BuildRequires:  python2-XStatic-DataTables
BuildRequires:  python2-XStatic-jQuery
BuildRequires:  python2-XStatic-Patternfly
BuildRequires:  python2-pytest

Requires:       ansible >= 2.1.5.0
Requires:       python-cliff
Requires:       python2-debtcollector
Requires:       python2-decorator >= 4.0.0
Requires:       python2-flask
Requires:       python2-flask-migrate
Requires:       python-flask-script
Requires:       python-frozen-flask
Requires:       python2-junit_xml
Requires:       python2-pygments
Requires:       python2-sqlalchemy
Requires:       python2-XStatic
Requires:       python2-XStatic-Bootstrap-SCSS
Requires:       python2-XStatic-DataTables
Requires:       python2-XStatic-jQuery
Requires:       python2-XStatic-Patternfly

%{?python_provide:%python_provide python2-%{package_name}}

%description -n python2-%{package_name}
ARA: Ansible Run Analysis

ARA records Ansible Playbook runs seamlessly to make them easier to visualize,
understand and troubleshoot. It integrates with Ansible wherever you run it.

%package -n python2-%{package_name}-tests
Summary:        Tests for %{package_name}

Requires:       python2-%{package_name} = %{version}-%{release}
Requires:       python2-lxml
Requires:       python-pytest

%description -n python2-%{package_name}-tests
ARA: Ansible Run Analysis

ARA records Ansible Playbook runs seamlessly to make them easier to visualize,
understand and troubleshoot. It integrates with Ansible wherever you run it.

This package contains the test files.

%if 0%{?with_python3}
%package -n python3-%{package_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
BuildRequires:  gcc
BuildRequires:  libffi-devel
BuildRequires:  openssl-devel
BuildRequires:  redhat-rpm-config
BuildRequires:  git
# Test dependencies for %check
BuildRequires:  ansible-python3 >= 2.1.5.0
BuildRequires:  python3-cliff
BuildRequires:  python3-debtcollector
BuildRequires:  python3-decorator >= 4.0.0
BuildRequires:  python3-flask
BuildRequires:  python3-flask-migrate
BuildRequires:  python3-flask-script
BuildRequires:  python3-frozen-flask
BuildRequires:  python3-junit_xml
BuildRequires:  python3-lxml
BuildRequires:  python3-pygments
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-XStatic
BuildRequires:  python3-XStatic-Bootstrap-SCSS
BuildRequires:  python3-XStatic-DataTables
BuildRequires:  python3-XStatic-jQuery
BuildRequires:  python3-XStatic-Patternfly
BuildRequires:  python3-pytest

Requires:       ansible-python3 >= 2.1.5.0
Requires:       python3-cliff
Requires:       python3-debtcollector
Requires:       python3-decorator >= 4.0.0
Requires:       python3-flask
Requires:       python3-flask-migrate
Requires:       python3-flask-script
Requires:       python3-frozen-flask
Requires:       python3-junit_xml
Requires:       python3-pygments
Requires:       python3-sqlalchemy
Requires:       python3-XStatic
Requires:       python3-XStatic-Bootstrap-SCSS
Requires:       python3-XStatic-DataTables
Requires:       python3-XStatic-jQuery
Requires:       python3-XStatic-Patternfly

%{?python_provide:%python_provide python3-%{package_name}}

%description -n python3-%{package_name}
ARA: Ansible Run Analysis

ARA records Ansible Playbook runs seamlessly to make them easier to visualize,
understand and troubleshoot. It integrates with Ansible wherever you run it.

%package -n python3-%{package_name}-tests
Summary:        Tests for %{package_name}

Requires:       python3-%{package_name} = %{version}-%{release}
Requires:       python3-lxml
Requires:       python3-pytest

%description -n python3-%{package_name}-tests
ARA: Ansible Run Analysis

ARA records Ansible Playbook runs seamlessly to make them easier to visualize,
understand and troubleshoot. It integrates with Ansible wherever you run it.

This package contains the test files.
%endif

%package common
Summary:        Common files for %{package_name}

Requires(pre): shadow-utils

%description common
ARA: Ansible Run Analysis

ARA records Ansible Playbook runs seamlessly to make them easier to visualize,
understand and troubleshoot. It integrates with Ansible wherever you run it.

This package contains the common files.

%package doc
Summary:        Documentation for %{package_name}

BuildRequires:  python-sphinx
BuildRequires:  python-sphinx_rtd_theme

%description doc
ARA: Ansible Run Analysis

ARA records Ansible Playbook runs seamlessly to make them easier to visualize,
understand and troubleshoot. It integrates with Ansible wherever you run it.

This package contains the documentation.

%prep
%autosetup -n %{package_name}-%{version} -S git

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%py2_build
%if 0%{?with_python3}
pushd %{py3dir}
%py3_build
popd
%endif
sphinx-build -W -b html doc/source doc/build/html

%install
%py2_install
%if 0%{?with_python3}
pushd %{py3dir}
%py3_install
popd
%endif

# Setup directories
install -d -m 755 %{buildroot}%{_sysconfdir}/%{package_name}
install -d -m 755 %{buildroot}%{_sharedstatedir}/%{package_name}
install -d -m 755 %{buildroot}%{_localstatedir}/log/%{package_name}

# Setup systemd unit file
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{package_name}-server.service

# Setup default config
install -p -D -m 640 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{package_name}/%{package_name}.cfg

# Setup logrotate
install -p -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{package_name}

%check
%{__python2} -m py.test -v
# TODO: Run python3 unit tests once ARA has fixed python3 compatibility.

%pre common
getent group %{package_name} >/dev/null || groupadd -r %{package_name}
getent passwd %{package_name} >/dev/null || \
    useradd -r -g %{package_name} -d %{_sharedstatedir}/%{package_name} \
    -s /sbin/nologin -c "User for ARA" %{package_name}
exit 0

%post
%systemd_post %{package_name}-server.service

%preun
%systemd_preun %{package_name}-server.service

%postun
%systemd_postun_with_restart %{package_name}-server.service

%files
%doc README.rst
%license LICENSE
%{_bindir}/ara
%{_bindir}/ara-manage
%{_bindir}/ara-wsgi
%{_unitdir}/%{package_name}-server.service

%if 0%{?with_python3}
%files -n %{package_name}-python3
%doc README.rst
%license LICENSE
%{_bindir}/ara
%{_bindir}/ara-manage
%{_bindir}/ara-wsgi
%{_unitdir}/%{package_name}-server.service
%endif

%files -n python2-%{package_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{package_name}
%{python2_sitelib}/%{package_name}-*.egg-info
%exclude %{python2_sitelib}/%{package_name}/tests

%files -n python2-%{package_name}-tests
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{package_name}/tests

%if 0%{?with_python3}
%files -n python3-%{package_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{package_name}
%{python3_sitelib}/%{package_name}-*.egg-info
%exclude %{python3_sitelib}/%{package_name}/tests

%files -n python3-%{package_name}-tests
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{package_name}/tests
%endif

%files common
%doc README.rst
%license LICENSE
%dir %{_sysconfdir}/%{package_name}
%config(noreplace) %attr(0640, root, %{package_name}) %{_sysconfdir}/%{package_name}/%{package_name}.cfg
%config(noreplace) %{_sysconfdir}/logrotate.d/%{package_name}
%dir %attr(0750, %{package_name}, %{package_name}) %{_localstatedir}/log/%{package_name}
%dir %attr(0750, %{package_name}, %{package_name}) %{_sharedstatedir}/%{package_name}

%files doc
%doc README.rst doc/build/html
%license LICENSE

%changelog
* Mon May 1 2017 David Moreau Simard <dmsimard@redhat.com> - 0.13.0-1
- First packaged version of ARA
