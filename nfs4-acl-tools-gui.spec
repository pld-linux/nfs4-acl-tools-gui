Summary:	GUI ACL utility for the Linux NFSv4 client
Summary(pl.UTF-8):	Graficzny interfejs użytkownika do ACL dla linuksowego klienta NFSv4
Name:		nfs4-acl-tools-gui
Version:	0.3.4
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://linux-nfs.org/~bfields/nfs4-acl-tools/nfs4-acl-tools-%{version}.tar.gz
# Source0-md5:	b72a83514cae9c754e64c3b266142eec
Patch0:		%{name}-strlcpy.patch
Patch1:		%{name}-system-libs.patch
URL:		http://linux-nfs.org/
BuildRequires:	QtGui-devel >= 4.1.4
BuildRequires:	attr-devel
BuildRequires:	nfs4-acl-tools-devel >= %{version}
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUI ACL utility for the Linux NFSv4 client.

%description -l pl.UTF-8
Graficzny interfejs użytkownika do ACL dla linuksowego klienta NFSv4.

%prep
%setup -q -n nfs4-acl-tools-%{version}
%patch0 -p1
%patch1 -p1

%build
cd GUI/nfs4-acl-editor
qmake-qt4 \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install GUI/nfs4-acl-editor/nfs4-acl-editor $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nfs4-acl-editor
