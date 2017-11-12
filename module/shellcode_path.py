import os
import re
import binascii
import time
import random
from module import Moduleobject

class shellcode(Moduleobject):
    def __init__(self,ui):
        super(shellcode,self).__init__()
        self.ui=ui
        ui.banner()
        self.values={'source':'',
                     'tempfile':'%s'%(time.strftime('%m%Y')+'.tmp')
                     }
        if os.path.isfile('./tmp/'+self.values['tempfile']):
            self.values['tempfile'] = self.values['tempfile'] + '_' + str(random.randint(1000,9999))

    def decode_shellcode(self,file_path):
        with open(file_path, 'rb') as raw:
            shellcodec = binascii.hexlify(raw.read())
            shellcode_hex_string = shellcodec.decode()
            for char in re.findall("..", shellcode_hex_string):
                with open('./tmp/' + self.values['tempfile'], 'a') as temp:
                    temp.write("\\x" + char)
            else:
                print('\033[92m' + '[*]' + '\033[0m''------> shellcode readed <------')

    def run_action(self):
        if os.path.isfile(self.values['source']):
            self.decode_shellcode(self.values['source'])
            input(" Type any key to Continue!!! ")
        else:
            print('File Not Found')