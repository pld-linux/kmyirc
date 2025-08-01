Summary:	IRC client for KDE
Summary(pl.UTF-8):	Klient IRC dla KDE
Name:		kmyirc
Version:	0.2.9
Release:	0.2
License:	GPL
Group:		X11/Applications
Vendor:		Stephan Hermann <sh@sourcecode.de>
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	8b51f6f064963ce8aa3fec6a6e2ed2b1
Patch0:		%{name}-opt.patch
Patch1:		%{name}-commas.patch
Patch2:		%{name}-include.patch
URL:		http://www.kmyirc.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	libjpeg-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IRC client for KDE.

%description -l pl.UTF-8
Klient IRC dla KDE.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
# don't regenerate am (broken AKA kdevelop-generated)
touch aclocal.m4 {,*/,*/*/,*/*/*/,*/*/*/*/}Makefile.in stamp-h.in
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
mv -f $RPM_BUILD_ROOT%{_applnkdir}/{Internet,Network/Communications}/kmyirc.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/lib*.so.*.*.*
%{_datadir}/apps/kmyirc
%{_datadir}/config/*
%{_pixmapsdir}/*/*/apps/*.png
%{_applnkdir}/Network/Communications/kmyirc.desktop
