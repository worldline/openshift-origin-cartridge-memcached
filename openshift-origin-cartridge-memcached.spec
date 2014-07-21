%global cartridgedir %{_libexecdir}/openshift/cartridges/v2/memcached

Summary:       Embedded memcached support for OpenShift
Name:          openshift-origin-cartridge-memcached
Version:       1.3
Release:       1%{?dist}
Group:         Network/Daemons
License:       ASL 2.0
URL:           http://www.openshift.com
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz
Requires:      memcached
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
BuildArch:     noarch

%description
Provides memcached cartridge support to OpenShift

%prep
%setup -q

%build
%__rm %{name}.spec
%__rm -rf rel-eng

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%post
# To modify an alternative you should:
# - remove the previous version if it's no longer valid
# - install the new version with an increased priority
# - set the new version as the default to be safe


%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Mon Jul 21 2014 Nicolas MESSIN <nicolas.messin@worldline.com> 1.3-1
- new package built with tito

* Mon Jul 21 2014 Nicolas MESSIN <nicolas.messin@worldline.com> 1.0.O
- Creation of initial memcached cartridge 

