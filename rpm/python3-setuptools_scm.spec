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
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  fdupes
BuildRequires:  python3-rpm-macros
Requires:       python3-setuptools
Recommends:     git-core

%description
The setuptools_scm package handles managing one's Python package versions
in SCM metadata. It also handles file finders for the supperted SCMs.

%prep
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%setup -q -n %{name}-%{version}/setuptools_scm

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python_sitelib}/*

%changelog
