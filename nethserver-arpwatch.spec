# nethserver-arpwatch.spec, 2015/10/21 dz00te

%define name nethserver-arpwatch
%define version 1.0.0
%define release 1
%define dist .ns6

Summary: Arpwatch is a tool that monitors ethernet activity
Name: %{name}
Version: %{version}
Release: %{release}%{dist}
License: GNU GPL version 3
Source: %{name}-%{version}.tar.gz

BuildArchitectures: noarch
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name}


BuildRequires: nethserver-devtools
#BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot

AutoReq: no
#Requires: nethserver-base
Requires: arpwatch

%description
Arpwatch is a tool that monitors ethernet activity and keeps
a database of ethernet/ip address pairings.
It also reports certain changes via email.
Arpwatch uses libpcap, a system-independent interface for 
user-level packet capture.


%prep
#%setup -q -n %{name}-%{version}
%setup

%build
#%{makedocs}
perl createlinks
%{__mkdir_p} root/var/lib/arpwatch

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

#%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
	--dir /var/lib/arpwatch 'attr(0775,root,root)' \
> %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f e-smith-%{version}-filelist
#%files -f %{name}-%{version}-filelist
#%defattr(-,root,root)

%post

%changelog
* Tue Oct 21 2015 dz00te <dz00te@framassa.org> 1.0.0-1.ns6
- First release to Nethserver
  Thanks to Stephane de Labrusse, JP Pialasse, Daniel B.

* Mon Sep 07 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 0.2-3.sme
- changed the user pcap to arpwatch [SME: 8429]

* Mon Jun 16 2014 JP Pialasse <tests@pialasse.com> 0.2-1.sme
- initial import to SME9 contribs

* Tue Mar 03 2009 Daniel B. <daniel@firewall-services.com> [0.1-2]
- Add e-smith-devtools as a build dependency

* Tue Jan 27 2009 Daniel B. <daniel@firewall-services.com> [0.1-1]
- Service not supervised (as the only option to disable forking is -d
  which also disable email alerts)

* Tue Jan 27 2009 Daniel B. <daniel@firewall-services.com> [0.1-0]
- Initial release

