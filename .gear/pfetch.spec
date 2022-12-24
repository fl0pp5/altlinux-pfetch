Name: pfetch
Version: 0.6.0
Release: alt1
Summary: A pretty system information tool written in POSIX sh

License: MIT
Url: https://github.com/dylanaraps/pfetch
Source0: %name-%version.tar
Patch: %name-%version.patch

Group: Monitoring
BuildArch: noarch

%description
The goal of this project is to implement a simple system information tool in POSIX sh using features built into the language itself (where possible).

The source code is highly documented and I hope it will act as a learning resource for POSIX sh and simple information detection across various different operating systems.

If anything in the source code is unclear or is lacking in its explanation, open an issue. Sometimes you get too close to something and you fail to see the "bigger picture"!

%prep
%setup

%install
mkdir -p %buildroot/%_bindir
install -Dm755 %name %buildroot/%_bindir/%name

%files
%doc LICENSE.md README.md
%_bindir/%name

%changelog
* Sat Dec 24 2022 fl0pp5 <fl0pp5@altlinux.org>
- Initial build for ALT
