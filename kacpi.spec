Summary:	Kacpi is a laptop battery and CPU temperature monitor
Summary(pl):	Kacpi to program monitoruj±cy temperaturê CPU oraz stan baterii laptopa
Name:		kacpi
Version:	0.6.3e
Release:	2
License:	GPL
Vendor:		Jonas Genannt <jonasge@gmx.net>
Group:		X11/Applications
Source0:	http://www.elektronikschule.de/~genannt/kacpi/download/%{name}-%{version}.tar.bz2
# Source0-md5:	4fca455edd54b9178711de04ffc8da12
URL:		http://www.elektronikschule.de/~genannt/kacpi/
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	kernel >= 2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
Kacpi is a laptop battery and CPU temperature monitor for Linux
kernels with ACPI support.
- a battery status update every minute as well as a button to force a
  check;
- a low-battery warning with 12-15 minutes and again with 5 minutes
  remaining;
- docking in the panel.

%description -l pl
Kacpi to program monitoruj±cy temperaturê CPU oraz stan baterii
laptopa, przeznaczony dla j±der zawierajacych obs³ugê ACPI. Cechy:
- status baterii aktualizowany co 5 minut lub za naci¶niêciem
  przycisku;
- informowanie o niskim stanie baterii co 12-15 minut i ponownie
  5 minut przed wyczerpaniem;
- panel dokuj±cy.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_applnkdir}/Utilities/*
