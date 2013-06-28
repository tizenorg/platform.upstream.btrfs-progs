Name:           btrfs-progs
Version:        0.20.rc1
Release:        0
Summary:        Utilities for the Btrfs filesystem
Group:          Base/File Systems
License:        GPL-2.0
Url:            http://btrfs.wiki.kernel.org/index.php/Main_Page
Source:         %{name}-%{version}.tar.xz
Source1001: 	btrfs-progs.manifest
BuildRequires:  libacl-devel
BuildRequires:  lzo-devel
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
# for /bin/true
Requires:       coreutils

%description
Utilities needed to create and maintain btrfs file systems under Linux.

%prep
%setup -q
cp %{SOURCE1001} .

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} prefix=%{_prefix} bindir=%{_sbindir} mandir=%{_mandir}
ln -s %{_sbindir}/btrfsck %{buildroot}%{_sbindir}/fsck.btrfs


%docs_package

%files
%manifest %{name}.manifest
%license COPYING
%{_sbindir}/btrfs
%{_sbindir}/btrfs-convert
%{_sbindir}/btrfs-debug-tree
%{_sbindir}/btrfs-find-root
%{_sbindir}/btrfs-image
%{_sbindir}/btrfs-map-logical
%{_sbindir}/btrfs-restore
%{_sbindir}/btrfs-show
%{_sbindir}/btrfs-vol
%{_sbindir}/btrfs-zero-log
%{_sbindir}/btrfsck
%{_sbindir}/btrfsctl
%{_sbindir}/btrfstune
%{_sbindir}/fsck.btrfs
%{_sbindir}/mkfs.btrfs
