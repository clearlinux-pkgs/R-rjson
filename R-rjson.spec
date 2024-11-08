#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v19
# autospec commit: f35655a
#
Name     : R-rjson
Version  : 0.2.23
Release  : 79
URL      : https://cran.r-project.org/src/contrib/rjson_0.2.23.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rjson_0.2.23.tar.gz
Summary  : JSON for R
Group    : Development/Tools
License  : GPL-2.0
Requires: R-rjson-lib = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package lib
Summary: lib components for the R-rjson package.
Group: Libraries

%description lib
lib components for the R-rjson package.


%prep
%setup -q -n rjson
pushd ..
cp -a rjson buildavx2
popd
pushd ..
cp -a rjson buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726519286

%install
export SOURCE_DATE_EPOCH=1726519286
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rjson/DESCRIPTION
/usr/lib64/R/library/rjson/INDEX
/usr/lib64/R/library/rjson/Meta/Rd.rds
/usr/lib64/R/library/rjson/Meta/features.rds
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
/usr/lib64/R/library/rjson/rpc_server/server.r
/usr/lib64/R/library/rjson/rpc_server/some_script.r
/usr/lib64/R/library/rjson/rpc_server/start_server
/usr/lib64/R/library/rjson/rpc_server/start_server.bat
/usr/lib64/R/library/rjson/unittests/runtests.r
/usr/lib64/R/library/rjson/unittests/test.array.r
/usr/lib64/R/library/rjson/unittests/test.big.r
/usr/lib64/R/library/rjson/unittests/test.crash.r
/usr/lib64/R/library/rjson/unittests/test.factors.r
/usr/lib64/R/library/rjson/unittests/test.largedata.r
/usr/lib64/R/library/rjson/unittests/test.list.r
/usr/lib64/R/library/rjson/unittests/test.number.r
/usr/lib64/R/library/rjson/unittests/test.strings.r
/usr/lib64/R/library/rjson/unittests/test.tojson.r
/usr/lib64/R/library/rjson/unittests/test.twitter.r
/usr/lib64/R/library/rjson/unittests/test.unicode.r

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/rjson/libs/rjson.so
/V4/usr/lib64/R/library/rjson/libs/rjson.so
/usr/lib64/R/library/rjson/libs/rjson.so
