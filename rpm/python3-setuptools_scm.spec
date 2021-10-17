#
# spec file for package python-setuptools_scm
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define python_version python3
Name:           python3-setuptools_scm
Version:        3.3.3
Release:        0
Summary:        Python setuptools handler for SCM tags
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pypa/setuptools_scm
Source0:        %{name}-%{version}.tar.gz
#Source:         https://files.pythonhosted.org/packages/source/s/setuptools_scm/setuptools_scm-%{version}.tar.gz
# Patch0:         add-rpmfail-pytest-markers.patch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  fdupes
BuildRequires:  python3-rpm-macros
Requires:       python3-setuptools
#BuildArch:      noarch
%if %{with test}
# Testing requirements
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest < 4.0}
BuildRequires:  %{python_module setuptools_scm = %{version}}
BuildRequires:  git-core
%endif
Recommends:     git-core
# %python_subpackages

%description
The setuptools_scm package handles managing one's Python package versions
in SCM metadata. It also handles file finders for the supperted SCMs.

%prep
%setup -q -n %{name}-%{version}/setuptools_scm
# %autopatch -p1

%build
%py3_build

%install
#%if !%{with test}
%py3_install
# %python_expand %fdupes %{buildroot}%{$python_sitelib}
#%endif

%if %{with test}
%check
# %python_expand PYTHONPATH=%{$python_sitelib} py.test-%{$python_bin_suffix} -v -k 'not (rpmfail_github_connect or test_mercurial or hg)'
%endif

%if !%{with test}
%files
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python_sitelib}/*
%endif

%changelog
