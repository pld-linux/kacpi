Summary:	Kacpi is a laptop battery and CPU temperature monitor.
Summary(pl):	Kacpi to program monitoruj±cy temperaturê CPU oraz stan baterii laptopa.
Name:		kacpi
Version:	0.6.3d
Release:	1
License:	GPL
Vendor:		Jonas Genannt <jonasge@gmx.net>
Group:		X11/Applications
Source0:	http://www.elektronikschule.de/~genannt/kacpi/download/%{name}-%{version}.tar.bz2
URL:		http://www.elektronikschule.de/~genannt/kacpi
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	kernel >= 2.4

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
laptopa przeznaczony jest dla kerneli zawierajacych wsparcie dla ACPI
- status baterii aktualizowany co 5 minut lub za naci¶niêciem
  przycisku;
- informowanie o niskim stanie baterii co 12-15 minut ponownie 5 minut
  przed wyczerpaniem;
- panel dokujacy.

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

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name} --with-kde
%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_applnkdir}/Utilities/*
