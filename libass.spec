Name:           libass
Version:        0.9.6
Release:        3%{?dist}
Summary:        Portable library for SSA/ASS subtitles rendering

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://code.google.com/p/libass/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libpng-devel
BuildRequires:  enca-devel
BuildRequires:  fontconfig-devel


%description
Libass is a portable library for SSA/ASS subtitles rendering.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc Changelog COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libass.pc

%changelog
* Martin Sourada <mso@fedoraproject.org>
- Upstream changed from sourceforge to code.google

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 24 2008 Martin Sourada <mso@fedoraproject.org> - 0.9.6-2
- remove glibc-devel and freetype-devel BRs, they're already pulled in by the
  rest

* Sun Mar 22 2008 Martin Sourada <mso@fedoraproject.org> - 0.9.6-1
- update to newever version
- drop %%doc from -devel
- update source url to conform with fedora packaging guidelines

* Sun Mar 22 2008 Martin Sourada <mso@fedoraproject.org> - 0.9.5-1
- Initial rpm package
