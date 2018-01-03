Name:           benchmark
Version:	%{VERSION}
Release:        1%{?dist}
Summary:	A microbenchmark support library 
License:	Apache 2.0
URL:		https://github.com/google/benchmark
Source:         %{name}-%{version}.tar.gz
Patch1:		so.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	cmake
BuildRequires:	gtest-devel

%description
A microbenchmark support library 

%package devel
Summary:	%{name} development package
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for %{name}.

%prep
%setup -n %{name}-%{version}
%patch1 -p0

%build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT%{_libdir}
rm -r $RPM_BUILD_ROOT%{_libdir}/cmake

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md docs/tools.md
%{_libdir}/*.so*

%files devel
%defattr(-,root,root,-)
%{_includedir}

%changelog
