import os
import signal
import sys

def exec(cmd):
	os.system(cmd)

def sudo(cmd):
	exec(f'sudo {cmd}')

def apt(cmd):
	sudo(f'apt {cmd} -y')

def apt_key(url):
	exec(f'wget -qO - {url} | sudo apt-key add -')

def apt_add(repo):
	sudo(f'apt-add-repository "{repo}" -y')
	apt('update')

def install(package):
	apt(f'install {package}')

def install_deb(url):
	exec(f'wget {url} -O program.deb')
	install('./program.deb')
	exec('rm ./program.deb')

def snap(package):
	exec(f'sudo snap install {package}')

def pip(package):
	exec(f'pip3 install --system --upgrade {package}')

def exit():
	apt('autoclean')
	sys.exit(0)

# Setup signal handler
signal.signal(signal.SIGINT, exit)

# Change directory to /tmp for temporary downloads and all
os.chdir('/tmp')

# Fix existing issues with dpkg (due to premature exit)
exec('sudo dpkg --configure -a')

# Update pre-installed packages
apt('update')
apt('upgrade')
apt('dist-upgrade')
apt('autoremove')

# Install Restricted Extras (Like MP3 Codecs & all)
exec('echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | debconf-set-selections')
install('ubuntu-restricted-extras')

# Git
install('git')

# Ansible
apt_add('ppa:ansible/ansible')
install('ansible')

# Sublime Text
apt_key('https://download.sublimetext.com/sublimehq-pub.gpg')
apt_add('deb https://download.sublimetext.com/ apt/stable/')
install('sublime-text')
# disable update check
# install package control
# install packages
# settings

# VS Code
install_deb('https://go.microsoft.com/fwlink/?LinkID=760868')
# install packages
# settings

# Google Chrome
install_deb('https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')

# VLC
install('vlc')

# Install Shutter (Screenshot Tool)
install('shutter')

# Terminal Emulator
install('tilix')
# Terminal settings (history / font / tiling)
# Start with session by modifying desktop file (sudo vim /usr/share/applications/com.gexperts.Tilix.desktop)

# WPS Office
install_deb('http://kdl.cc.ksosoft.com/wps-community/download/6757/wps-office_10.1.0.6757_amd64.deb')

# Markdown Editor
apt_key('https://typora.io/linux/public-key.asc')
apt_add('deb https://typora.io/linux ./')
install('typora')

# System Wide Search
# Albert?

# CopyQ (Clipboard Manager)
apt_add('ppa:hluk/copyq')
install('copyq')

# Stacer (System Monitoring)
apt_add('ppa:oguzhaninan/stacer')
install('stacer')

# SpeedCrunch (Scientific Calculator)
install('speedcrunch')

# NitroShare (File Sharing)
install('nitroshare')

# Flatpak (For flatpak installations)
install('flatpak')

# Nomacs (Image Viewer)
install('nomacs')

# GParted (Partition Manager)
install('gparted')

# QBitTorrent (Torrent client)
install('qbittorrent')

# SimpleNote (Note Taking App)
snap('simplenote')

# Install Fonts
install('fonts-roboto')
install('fonts-lato')
install('fonts-hack-ttf')

# Albert (System wide search)
apt_key('https://build.opensuse.org/projects/home:manuelschneid3r/public_key')
apt_add('deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_18.04/ /')
install('albert')

# Gnome Extensions
install('gnome-tweak-tool')
install('gnome-shell-extensions')

def gnome_enable(ext):
	exec(f'gnome-shell-extension-tool -e {ext}')

def gnome_disable(ext):
	exec(f'gnome-shell-extension-tool -d {ext}')

def gnome_install(ext):
	exec(f'gnome-shell-extension-cli install {ext}')

# Install gnome shell extension cli
exec('wget https://raw.githubusercontent.com/martin-sucha/gnome-shell-extension-cli/master/gnome-shell-extension-cli')
sudo('mv gnome-shell-extension-cli /usr/bin/')
sudo('chmod +x /usr/bin/gnome-shell-extension-cli')

# Install Gnome Extensions
# Windows like taskbar
gnome_install('https://extensions.gnome.org/extension/1160/dash-to-panel/')
# Windows like start menu
gnome_install('https://extensions.gnome.org/extension/1228/arc-menu/')
# Prevent PC from sleeping
gnome_install('https://extensions.gnome.org/extension/517/caffeine/')
# Remove dropdown arrows from icons and menus
gnome_install('https://extensions.gnome.org/extension/800/remove-dropdown-arrows/')
# Reduce spacing between icons
gnome_install('https://extensions.gnome.org/extension/355/status-area-horizontal-spacing/')

# Paper Theme
apt_add('ppa:snwh/ppa')
install('paper-icon-theme')

# Adapta Theme
apt_add('ppa:tista/adapta')
install('adapta-gtk-theme')

# Arc Theme
install('arc-theme')

# Mackup (To restore settings and all)
pip('mackup')
exec('mackup restore')
