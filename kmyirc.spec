Summary:	IRC client for KDE
Summary(pl):	Klient IRC dla KDE
Name:		kmyirc
Version:	0.2.9
Release:	0.1
License:	GPL
Group:		X11/Applications
Vendor:		Stephan Hermann <sh@sourcecode.de>
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-acinclude.patch
URL:		http://www.kmyirc.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
IRC client for KDE

%description -l pl
Klient IRC dla KDE

%prep
%setup -q


%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*
%{_datadir}/*/*
