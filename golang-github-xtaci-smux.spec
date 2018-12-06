# https://github.com/xtaci/smux
%global goipath github.com/xtaci/smux
%global vtag    1.09
%global tag     v%{vtag}

Name:           golang-github-xtaci-smux
Version:        1.0.9
Release:        1%{?dist}
Summary:        Simple Stream Multiplexing for golang
License:        MIT

%gometa

URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

BuildRequires:  golang(github.com/pkg/errors)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%setup -q -n smux-%{vtag}


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Mon Oct 01 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.9-1
- Update to version 1.0.9.

* Fri Sep 28 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.8-1
- Update to version 1.0.8.

* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.7-3
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.7-1
- Update to version 1.0.7.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 01 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.6-1
- Update to version 1.0.6.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3.20170422.git2de5471
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2.20170422.git2de5471
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5-1.20170422.git2de5471
- Bump to commit 2de5471.

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.5-1
- First package for Fedora

