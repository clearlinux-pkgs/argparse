#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x243ACFA951F78E01 (tw-public@gmx.de)
#
Name     : argparse
Version  : 1.4.0
Release  : 19
URL      : http://pypi.debian.net/argparse/argparse-1.4.0.tar.gz
Source0  : http://pypi.debian.net/argparse/argparse-1.4.0.tar.gz
Source99 : http://pypi.debian.net/argparse/argparse-1.4.0.tar.gz.asc
Summary  : Python command-line parsing library
Group    : Development/Tools
License  : Python-2.0
Requires: argparse-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
interfaces.
        
        The program defines what arguments it requires, and argparse will figure out
        how to parse those out of sys.argv. The argparse module also automatically
        generates help and usage messages and issues errors when users give the
        program invalid arguments.
        
        As of Python >= 2.7 and >= 3.2, the argparse module is maintained within the
        Python standard library. For users who still need to support Python < 2.7 or
        < 3.2, it is also provided as a separate package, which tries to stay
        compatible with the module in the standard library, but also supports older
        Python versions.
        
        Also, we can fix bugs here for users who are stuck on some non-current python
        version, like e.g. 3.2.3 (which has bugs that were fixed in a later 3.2.x
        release).
        
        argparse is licensed under the Python license, for details see LICENSE.txt.
        
        
        Compatibility
        -------------

%package legacypython
Summary: legacypython components for the argparse package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the argparse package.


%package python
Summary: python components for the argparse package.
Group: Default

%description python
python components for the argparse package.


%prep
%setup -q -n argparse-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519398954
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
