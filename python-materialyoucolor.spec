#
# spec file for package python-material-color-utilities-python
#
# Copyright (c) 2022 SUSE LLC
#a
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

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define pythons python3
%global debug_package %{nil}
Name:           python-materialyoucolor
Version:        2.0.9
Release:        1%{?dist}
Summary:        Material You color algorithms for Python
License:        MIT
URL:            https://github.com/T-Dynamos/materialyoucolor-python
Source0:        %{url}/archive/v%{version}/materialyoucolor-python-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module wheel >= 0.37.1}
BuildRequires:  %{python_module regex}
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
%if 0%{?fedora}
Requires:       python3-pillow
%else
Requires:       python311-Pillow
%endif
BuildArch:      x86_64

%description
Python port of material-color-utilities used for Material You colors.

%prep
%autosetup -p1 -n materialyoucolor-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{$python3_sitearch}/materialyoucolor/

%files
%license LICENSE
%{python3_sitearch}/materialyoucolor/
%{python3_sitearch}/materialyoucolor-%{version}*.*-info/

%changelog
* Sun May 19 2024 Luis Bocanegra <luisbocanegra@users.noreply.github.com> 2.0.9-1
- new package built with tito
