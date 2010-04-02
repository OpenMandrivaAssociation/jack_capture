%define name    jack_capture

%define version 0.9.44
%define release %mkrel 1

Summary:    Simple JACK audiofile recorder-encoder
Name:       %name
Version:    %version
Release:    %release
URL:        http://archive.notam02.no/arkiv/src/

# jack_capture_gui2 is under BSD License
License:    GPLv2+ and BSD
Group:      Sound
Source:     %name-%version.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  gtk2-devel jackit-devel
BuildRequires:  libsndfile-devel libogg-devel libflac-devel
BuildRequires:  meterbridge

Requires:   meterbridge Xdialog

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

%install
rm -rf %{buildroot}
%makeinstall_std
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

cat > %buildroot%_datadir/applications/jack_capture_gui.desktop << EOF
[Desktop Entry]
Name=Jack_capture_gui
Comment=Simple JACK audiofile recorder-encoder
Exec=jack_capture_gui
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
%_bindir/jack_capture_gui
%_bindir/jack_capture_gui2
%_datadir/applications/jack_capture_gui.desktop
%_datadir/applications/jack_capture_gui2.desktop
%doc README
