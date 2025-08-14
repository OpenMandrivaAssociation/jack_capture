%global	debug_package %{nil}

%define	gitdate	20230104

# The GUI is gtk+-2.0 and won't build ATM
%bcond_with gui

Summary:		Simple JACK audiofile recorder-encoder
Name:		jack_capture
Version:		0.9.73
Release:		1
License:		GPLv2+
Group:	Sound
Url:		https://github.com/kmatheussen/jack_capture
#Source0:	https://archive.notam02.no/arkiv/src/%%{name}-%%{version}.tar.gz
# Use git HEAD from a more live fork
Source0:	%{name}-%{gitdate}.tar.xz
Patch0:	jack_capture-0.9.73-fix-Makefile.patch
BuildRequires:	gcc
BuildRequires:	atomic-devel
BuildRequires:	pkgconfig(flac)
%if %{with gui}
BuildRequires:	pkgconfig(gtk+-2.0)
%endif
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(lame)
BuildRequires:	pkgconfig(liblo)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(sndfile)
# Not provided yet; perhaps not used
Recommends:	meterbridge

%description
Small audio file recorder with on-the-fly encoding capabilities for the
JACK Audio Connection Kit. Jack_capture comes with two control GUIs, one
of which is deliberately simple. Supported save file formats are wav
(with 4GB limit bypass), ogg, flac, wav, wavex, au, aiff and raw.

%files
%doc README
%{_bindir}/%{name}
%if %{with gui}
%{_bindir}/%{name}_gui2
%{_datadir}/applications/%{name}_gui2.desktop
%endif

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{gitdate}


%build
%set_build_flags
%make_build

%if %{with gui}
# We have to build the legacy gui program at our own risk
make %{name}_gui2
%endif


%install
%makeinstall_std

%if %{with gui}
install %{name}_gui2 %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_datadir}/applications
cat > %buildroot%_datadir/applications/jack_capture_gui2.desktop << EOF
[Desktop Entry]
Name=%{name}_gui2
Comment=Simple JACK audiofile recorder-encoder GTK GUI
Exec=%{name}_gui2
Icon=sound_section
Categories=Audio;X-OpenMandrivaLinux-Sound;
Terminal=false
Type=Application
EOF
%endif
