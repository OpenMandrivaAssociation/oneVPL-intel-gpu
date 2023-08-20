Name:           oneVPL-intel-gpu
Version:        23.3.1
Release:        1
Summary:        Intel oneVPL GPU Runtime
License:        MIT
URL:            https://www.intel.com/content/www/us/en/developer/tools/oneapi/onevpl.html
Source0:        https://github.com/oneapi-src/%{name}/archive/refs/tags/%{version}/oneVPL-intel-gpu-intel-onevpl-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(vpl)
BuildRequires:  pkgconfig(libdrm) >= 2.4
BuildRequires:  pkgconfig(libva) >= 1.12
Requires:       onevpl

%description
Intel oneVPL GPU Runtime is a Runtime implementation of oneVPL API for Intel Gen
GPUs. Runtime provides access to hardware-accelerated video decode, encode and
filtering.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n oneVPL-intel-gpu-intel-onevpl-%{version}

%build
export VPL_BUILD_DEPENDENCIES="%{_prefix}"
%cmake \
    -DBUILD_TESTS:BOOL='OFF' \
    -DCMAKE_BUILD_TYPE:STRING="Fedora" \
    -DMFX_ENABLE_AV1_VIDEO_DECODE:BOOL='ON' \
    -DMFX_ENABLE_AV1_VIDEO_ENCODE:BOOL='ON'
%make_build

%install
%make_install -C build

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_libdir}/libmfx-gen.so.1.2
%{_libdir}/libmfx-gen.so.1.2.9
%dir %{_libdir}/libmfx-gen
%{_libdir}/libmfx-gen/enctools.so

%files devel
%{_libdir}/libmfx-gen.so
%{_libdir}/pkgconfig/libmfx-gen.pc
