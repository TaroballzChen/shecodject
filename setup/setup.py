import os

os.system('sudo apt-get update')
os.system('sudo apt-get install wine')
os.system('sudo apt-get install wineticks')
os.system('pip install distorm3')
os.system('wine msiexec /i python-3.4.3.msi /L*v log.txt')
os.system('wine /root/.wine/drive_c/Python34/python.exe /root/.wine/drive_c/Python34/Scripts/pip.exe install pyinstaller')
