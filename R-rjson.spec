#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rjson
Version  : 0.2.21
Release  : 76
URL      : https://cran.r-project.org/src/contrib/rjson_0.2.21.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rjson_0.2.21.tar.gz
Summary  : JSON for R
Group    : Development/Tools
License  : GPL-2.0
Requires: R-rjson-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-rjson package.
Group: Libraries

%description lib
lib components for the R-rjson package.


%prep
%setup -q -c -n rjson
cd %{_builddir}/rjson

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641951499

%install
export SOURCE_DATE_EPOCH=1641951499
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rjson
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rjson
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rjson
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rjson || :


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
/usr/lib64/R/library/rjson/libs/rjson.so
/usr/lib64/R/library/rjson/libs/rjson.so.avx2
/usr/lib64/R/library/rjson/libs/rjson.so.avx512
