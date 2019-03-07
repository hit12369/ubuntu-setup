import os

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
	exec(f'pip install --upgrade {package}')

# Update pre-installed packages
apt('update')
apt('upgrade')
apt('dist-upgrade')
apt('autoremove')

# Install Restricted Extras (Like MP3 Codecs & all)
install('ubuntu-restricted-extras')

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
# Guake / Tilix / Terminator
install('tilix')
# Terminal settings (history / font / tiling)

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

# Mackup (To restore settings and all)
pip('mackup')
exec('mackup restore')
