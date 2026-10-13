%define module tidalapi

Name:		python-%{module}
Version:	0.8.11
Release:	2
Summary:	Unofficial API for TIDAL music streaming service.
Source0:	https://files.pythonhosted.org/packages/source/t/%{module}/%{module}-%{version}.tar.gz
URL:		https://pypi.org/project/tidalapi/
License:	LGPL-3.0-or-later
Group:		Development/Python
BuildArch:	noarch

BuildSystem:	python

BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
Unofficial Python API for TIDAL music streaming service.

%files
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}.dist-info
