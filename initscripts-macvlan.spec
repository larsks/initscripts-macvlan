Name:		initscripts-macvlan
Version:	0.1
Release:	3
BuildArch:	noarch
Summary:	macvlan ifup/down scripts
License:	GPLv2 and GPLv2+
URL:		https://github.com/eugenepaniot/initscripts-macvlan

Source:		%{name}-%{version}.tar.gz

Requires:	initscripts >= 9.49.30
Requires:	iproute >= 3.10


%description
initscripts-macvlan provides scripts to manage macvlan network interfaces

%prep
%setup -q


%install
%{__mkdir} -p %{buildroot}/etc/sysconfig/network-scripts

%{__install} -p -m 0755 ifup-macvlan   %{buildroot}/etc/sysconfig/network-scripts/
%{__install} -p -m 0755 ifdown-macvlan %{buildroot}/etc/sysconfig/network-scripts/

%files
%defattr(-,root,root)
/etc/sysconfig/network-scripts/ifup-macvlan
/etc/sysconfig/network-scripts/ifdown-macvlan

%doc


%changelog

