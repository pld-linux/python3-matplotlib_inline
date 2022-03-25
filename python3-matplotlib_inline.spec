%define		pypi_name	matplotlib-inline
%define		module	matplotlib_inline
Summary:	Inline Matplotlib backend for Jupyter
Summary(pl.UTF-8):	Backend Jupytera pozwalający na wstawki używające Matplotliba
Name:		python3-%{module}
Version:	0.1.2
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/matplotlib-inline/
Source0:	https://files.pythonhosted.org/packages/source/m/matplotlib-inline/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	7af8f8ae6ea5217134dd7bd115c78ac3
URL:		https://github.com/ipython/matplotlib-inline
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline Matplotlib backend for Jupyter.

%description -l pl.UTF-8
Backend Jupytera pozwalający na wstawki używające Matplotliba.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}/*.py
%{py3_sitescriptdir}/%{module}/__pycache__
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
