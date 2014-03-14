%define debug_package %{nil}

Summary:		Simple JACK audiofile recorder-encoder
Name:		jack_capture
Version:		0.9.61
Release:		2
URL:		http://archive.notam02.no/arkiv/src/
License:		GPLv2+
Group:		Sound
Source0:		%{name}-%{version}.tar.gz
BuildRequires:	gtk+2.0-devel
BuildRequires:	jackit-devel
BuildRequires:	sndfile-devel
BuildRequires:	libogg-devel
BuildRequires:	flac-devel
BuildRequires:	meterbridge
Requires:	meterbridge

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


%files
%doc README
%{_bindir}/jack_capture
%{_bindir}/jack_capture_gui2
%{_datadir}/applications/jack_capture_gui2.desktop


%changelog
* Wed Oct 31 2012 Giovanni Mariani <mc2374àmclink.it> 0.9.61-2
- Dropped BuildRoot, %%mkrel, %%defattr and %%clean section
- Fixed Breq for libsndfile devel package

* Sat Dec 24 2011 Frank Kober <emuse@mandriva.org> 0.9.61-1
+ Revision: 745017
- new version 0.9.61

* Mon Dec 06 2010 Frank Kober <emuse@mandriva.org> 0.9.57-1mdv2011.0
+ Revision: 612952
- new version 0.9.57
  o old jack_capture_gui dropped (no longer install target)
  o license updated

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.44-2mdv2011.0
+ Revision: 612435
- the mass rebuild of 2010.1 packages

* Fri Apr 02 2010 Frank Kober <emuse@mandriva.org> 0.9.44-1mdv2010.1
+ Revision: 530793
- add missing BR
- import jack_capture


