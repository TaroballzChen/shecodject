import os

os.system('sudo apt-get update')
os.system("sudo apt-get install -y python3-pip")
os.system("pip3 install pyinstaller")
os.system('pip3 install distorm3')
os.system("curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -")
os.system("echo 'deb [arch=amd64] https://download.docker.com/linux/debian buster stable' | sudo tee /etc/apt/sources.list.d/docker.list")
os.system("sudo apt-get update")
os.system("sudo apt-get remove docker docker-engine docker.io")
os.system("sudo apt-get -y install docker-ce")
os.system("sudo systemctl start docker")
os.system("sudo systemctl enable docker")
os.system("sudo usermod -aG docker $USER")
os.system("docker pull cdrx/pyinstaller-windows:python3-32bit")

