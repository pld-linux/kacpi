Summary:	Kacpi is a laptop battery and CPU temperature monitor
Summary(pl.UTF-8):	Kacpi to program monitorujący temperaturę CPU oraz stan baterii laptopa
Name:		kacpi
Version:	0.6.3e
Release:	5
License:	GPL
Vendor:		Jonas Genannt <jonasge@gmx.net>
Group:		X11/Applications
Source0:	http://www.elektronikschule.de/~genannt/kacpi/download/%{name}-%{version}.tar.bz2
# Source0-md5:	4fca455edd54b9178711de04ffc8da12
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-gcc43.patch
URL:		http://www.elektronikschule.de/~genannt/kacpi/
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kacpi is a laptop battery and CPU temperature monitor for Linux
kernels with ACPI support.
- a battery status update every minute as well as a button to force a
  check;
- a low-battery warning with 12-15 minutes and again with 5 minutes
  remaining;
- docking in the panel.

%description -l pl.UTF-8
Kacpi to program monitorujący temperaturę CPU oraz stan baterii
laptopa, przeznaczony dla jąder zawierających obsługę ACPI. Cechy:
- status baterii aktualizowany co 5 minut lub za naciśnięciem
  przycisku;
- informowanie o niskim stanie baterii co 12-15 minut i ponownie
  5 minut przed wyczerpaniem;
- panel dokujący.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
# no icon themes, *.png installed directly to icondir - so use pixmapsdir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
cp -f /usr/share/automake/config.* admin
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*.png
%{_desktopdir}/*.desktop
