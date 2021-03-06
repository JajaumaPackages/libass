Name:           libass
Version:        0.13.7
Release:        1%{?dist}
Summary:        Portable library for SSA/ASS subtitles rendering

Group:          System Environment/Libraries
License:        ISC
URL:            https://github.com/libass
Source0:        https://github.com/libass/libass/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  enca-devel
BuildRequires:  fontconfig-devel
BuildRequires:  fribidi-devel
BuildRequires:  harfbuzz-devel >= 0.9.5
BuildRequires:  libpng-devel

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
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%check
make check


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc Changelog COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libass.pc

%changelog
* Sat Sep 02 2017 Jajauma's Packages <jajauma@yandex.ru> - 0.13.7-1
- Update to latest upstream release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 07 2016 Martin Sourada <mso@fedoraproject.org> - 0.13.4-1
- Update to 0.13.4
- Fixes CVE-2016-7969, CVE-2016-7970, CVE-2016-7972


* Tue Sep 27 2016 Martin Sourada <mso@fedoraproject.org> - 0.13.3-1
- Update to 0.13.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 17 2015 Martin Sourada <mso@fedoraproject.org> - 0.13.1-1
- Update to 0.13.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 26 2015 Martin Sourada <mso@fedoraproject.org> - 0.12.1-1
- Update to 0.12.1

* Thu Nov 06 2014 Martin Sourada <mso@fedoraproject.org> - 0.12.0-1
- Codebase moved from google code to github.
- Update to 0.12.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.10.2-1
- Update to 0.10.2
- Run make check

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 17 2012 Martin Sourada <mso@fedoraproject.org> - 0.10.1-2
- Fix a mistake in minimal required version of harfbuzz

* Wed Oct 17 2012 Martin Sourada <mso@fedoraproject.org> - 0.10.1-1
- New upstream release
  - various improvements and fixes
  - improved compatibility with vsfilter
- Build with harfbuzz from F18 onward for advanced opentype shaping

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Martin Sourada <mso@fedoraproject.org> - 0.10.0-1
- New upstream release
  - various improvements and fixes
- BuildRequires: fribidi-devel (bidirectional text suport)
- Fixes some wierd memory allocation related crash with freetype 2.4.6
  - rhbz 753017, rhbz 753065

* Tue May 31 2011 Martin Sourada <mso@fedoraproject.org> - 0.9.12-1
- New upstream release
  - Licence changed to ISC
  - Fixed word-wrapping
  - Improved charmap fallback matching
  - Various other improvements and fixes

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.9.11-2
- Rebuilt for gcc bug 634757

* Mon Sep 13 2010 Martin Sourada <mso@fedoraproject.org> - 0.9.11-1
- Fixes rhbz #630432
- New upstream release
  - Various fixes
  - Performance improvements
  - Calculate drawing bounding box like VSFilter
  - Better PAR correction if text transforms are used
  - Improved fullname font matching
  - Add ass_flush_events API function
  - Basic support for @font vertical text layout

* Fri Jul 30 2010 Martin Sourada <mso@fedoraproject.org> - 0.9.9-1
- Fixes rhbz #618733
- New upstream release
  - Parse numbers in a locale-independent way
  - Disable script file size limit
  - Match fonts against the full name ("name for humans")
  - Reset clip mode after \iclip
  - Improve VSFilter compatibility
  - A couple of smaller fixes and cleanups

* Sun Jan 10 2010 Martin Sourada <mso@fedoraproject.org> - 0.9.8-2
- Fix source URL

* Sun Oct 25 2009 Martin Sourada <mso@fedoraproject.org> - 0.9.8-1
- New upstream release
- See http://repo.or.cz/w/libass.git?a=blob;f=Changelog for changes

* Mon Aug 10 2009 Martin Sourada <mso@fedoraproject.org> - 0.9.7-1
- New upstream release
- Upstream changed from sourceforge to code.google

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 24 2009 Martin Sourada <mso@fedoraproject.org> - 0.9.6-2
- remove glibc-devel and freetype-devel BRs, they're already pulled in by the
  rest

* Sun Mar 22 2009 Martin Sourada <mso@fedoraproject.org> - 0.9.6-1
- update to newever version
- drop %%doc from -devel
- update source url to conform with fedora packaging guidelines

* Sun Mar 22 2009 Martin Sourada <mso@fedoraproject.org> - 0.9.5-1
- Initial rpm package
