Name:           benchmark
Version:	%{VERSION}
Release:        1%{?dist}
Summary:	A microbenchmark support library 
License:	Apache 2.0
URL:		https://github.com/google/benchmark
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	cmake3
BuildRequires:	gtest-devel
BuildRequires:	gmock-devel

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

%build
cmake3 . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS=ON
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md docs/*
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}_main.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/*.cmake

%changelog
