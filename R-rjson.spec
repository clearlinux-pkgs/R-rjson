#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rjson
Version  : 0.2.15
Release  : 18
URL      : http://cran.r-project.org/src/contrib/rjson_0.2.15.tar.gz
Source0  : http://cran.r-project.org/src/contrib/rjson_0.2.15.tar.gz
Summary  : JSON for R
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n rjson

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library rjson
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library rjson


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rjson/DESCRIPTION
/usr/lib64/R/library/rjson/INDEX
/usr/lib64/R/library/rjson/Meta/Rd.rds
/usr/lib64/R/library/rjson/Meta/hsearch.rds
/usr/lib64/R/library/rjson/Meta/links.rds
/usr/lib64/R/library/rjson/Meta/nsInfo.rds
/usr/lib64/R/library/rjson/Meta/package.rds
/usr/lib64/R/library/rjson/Meta/vignette.rds
/usr/lib64/R/library/rjson/NAMESPACE
/usr/lib64/R/library/rjson/R/rjson
/usr/lib64/R/library/rjson/R/rjson.rdb
/usr/lib64/R/library/rjson/R/rjson.rdx
/usr/lib64/R/library/rjson/changelog.txt
/usr/lib64/R/library/rjson/doc/index.html
/usr/lib64/R/library/rjson/doc/json_rpc_server.Rnw
/usr/lib64/R/library/rjson/doc/json_rpc_server.pdf
/usr/lib64/R/library/rjson/help/AnIndex
/usr/lib64/R/library/rjson/help/aliases.rds
/usr/lib64/R/library/rjson/help/paths.rds
/usr/lib64/R/library/rjson/help/rjson.rdb
/usr/lib64/R/library/rjson/help/rjson.rdx
/usr/lib64/R/library/rjson/html/00Index.html
/usr/lib64/R/library/rjson/html/R.css
/usr/lib64/R/library/rjson/libs/rjson.so
/usr/lib64/R/library/rjson/libs/symbols.rds
/usr/lib64/R/library/rjson/rpc_server/server.r
/usr/lib64/R/library/rjson/rpc_server/some_script.r
/usr/lib64/R/library/rjson/rpc_server/start_server
/usr/lib64/R/library/rjson/rpc_server/start_server.bat
/usr/lib64/R/library/rjson/unittests/runtests.r
/usr/lib64/R/library/rjson/unittests/test.array.r
/usr/lib64/R/library/rjson/unittests/test.big.r
/usr/lib64/R/library/rjson/unittests/test.factors.r
/usr/lib64/R/library/rjson/unittests/test.list.r
/usr/lib64/R/library/rjson/unittests/test.number.r
/usr/lib64/R/library/rjson/unittests/test.strings.r
/usr/lib64/R/library/rjson/unittests/test.tojson.r
/usr/lib64/R/library/rjson/unittests/test.twitter.r
/usr/lib64/R/library/rjson/unittests/test.unicode.r
