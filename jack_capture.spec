Summary:    Simple JACK audiofile recorder-encoder
Name:       jack_capture
Version:    0.9.61
Release:    1
URL:        http://archive.notam02.no/arkiv/src/

License:    GPLv2+
Group:      Sound
Source:     %name-%version.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  gtk2-devel jackit-devel
BuildRequires:  libsndfile-devel libogg-devel libflac-devel
BuildRequires:  meterbridge

Requires:   meterbridge

%description
Small audio file recorder with on-the-fly encoding capabilities for the
JACK Audio Connection Kit. Jack_capture comes with two control GUIs, one
of which is deliberately simple. Supported save file formats are wav
(with 4GB limit bypass), ogg, flac, wav, wavex, au, aiff and raw.

%prep
%setup -q
perl -pi -e 's/usr\/local/usr/g' Makefile
perl -pi -e 's/-march=native//g' Makefile

%build
%make
#we have to build the legacy gui program at our own risk
make jack_capture_gui2

%install
rm -rf %{buildroot}
%makeinstall_std
install jack_capture_gui2 %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_datadir}/applications
cat > %buildroot%_datadir/applications/jack_capture_gui2.desktop << EOF
[Desktop Entry]
Name=Jack_capture_gui2
Comment=Simple JACK audiofile recorder-encoder
Exec=jack_capture_gui2
Icon=sound_section
Categories=Audio;X-MandrivaLinux-Sound;
Terminal=false
Type=Application
X-Desktop-File-Install-Version=0.15
EOF

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%_bindir/jack_capture
%_bindir/jack_capture_gui2
%_datadir/applications/jack_capture_gui2.desktop
%doc README
