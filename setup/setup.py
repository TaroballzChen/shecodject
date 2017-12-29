import os

os.system('dpkg --add-architecture i386 && apt-get update && apt-get install wine32')
os.system('sudo apt-get update')
os.system('sudo apt-get install wine')
os.system('sudo apt-get install winetricks')
os.system('pip install distorm3')
os.system('WINEPREFIX="$HOME/prefix32" WINEARCH=win32 wine wineboot')
os.system('WINEPREFIX="$HOME/prefix32"  wine msiexec /i python-3.4.3.msi')
os.system('WINEPREFIX="$HOME/prefix32" wine /root/prefix32/drive_c/Python34/python.exe /root/prefix32/drive_c/Python34/Scripts/pip.exe install pyinstaller')
