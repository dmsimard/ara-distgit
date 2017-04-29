%if 0%{?fedora}
%global with_python3 1
%endif
%global package_name ara

Name:           %{package_name}
Version:        0.13.0
Release:        1%{?dist}
Summary:        ARA: Ansible Analysis - Record and visualize Ansible Playbook runs

# ARA is Apache v2 but Ansible plugins are GPLv3
License:        APSLv2 and GPLv3
URL:            https://git.openstack.org/cgit/openstack/ara
Source0:        https://dmsimard.com/%{package_name}-%{version}.tar.gz
#Source0:        https://pypi.io/packages/source/a/%{package_name}/%{package_name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       python2-%{package_name} = %{version}-%{release}

%description
ARA: Ansible Run Analysis

ARA records Ansible Playbook runs seamlessly to make them easier to visualize,
understand and troubleshoot. It integrates with Ansible wherever you run it.

# TODO:
# - Subpackage for embedded webserver with systemd implementation
# - Subpackage for httpd+mod_wsgi implementation

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
BuildRequires:  ansible >= 2.1.5.0
BuildRequires:  python3-cliff
BuildRequires:  python3-debtcollector
BuildRequires:  python3-decorator >= 4.0.0
BuildRequires:  python3-flask
BuildRequires:  python3-flask-migrate
BuildRequires:  python3-flask-script
BuildRequires:  python3-frozen-flask
Requires:       python3-junit_xml
BuildRequires:  python3-lxml
BuildRequires:  python3-pygments
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-XStatic
BuildRequires:  python3-XStatic-Bootstrap-SCSS
BuildRequires:  python3-XStatic-DataTables
BuildRequires:  python3-XStatic-jQuery
BuildRequires:  python3-XStatic-Patternfly
BuildRequires:  python3-pytest

Requires:       ansible >= 2.1.5.0
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

%package -n %{package_name}-doc
Summary:        Documentation for %{package_name}

BuildRequires:  python-sphinx
BuildRequires:  python-sphinx_rtd_theme

%description -n %{package_name}-doc
ARA: Ansible Run Analysis

ARA records Ansible Playbook runs seamlessly to make them easier to visualize,
understand and troubleshoot. It integrates with Ansible wherever you run it.

This package contains the documentation.

%prep
%autosetup -n %{package_name}-%{version} -S git

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif
sphinx-build -W -b html doc/source doc/build/html

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%check
%{__python2} -m py.test
# TODO: Run python3 unit tests once ARA has fixed python3 compatibility.

%files -n python2-%{package_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{package_name}
%{python2_sitelib}/%{package_name}-*.egg-info
%{_bindir}/ara
%{_bindir}/ara-manage
%{_bindir}/ara-wsgi
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
%{_bindir}/ara
%{_bindir}/ara-manage
%{_bindir}/ara-wsgi
%exclude %{python3_sitelib}/%{package_name}/tests

%files -n python3-%{package_name}-tests
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{package_name}/tests
%endif

%files -n %{package_name}-doc
%doc README.rst doc/build/html
%license LICENSE

%changelog
* Mon May 1 2017 David Moreau Simard <dmsimard@redhat.com> - 0.13.0-1
- First packaged version of ARA
