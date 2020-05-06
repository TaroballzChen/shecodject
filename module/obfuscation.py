import os
import re
import binascii
import time
import random
from module import Moduleobject

class obshellcode(Moduleobject):
    def __init__(self,ui):
        super(obshellcode,self).__init__()
        self.ui=ui
        ui.banner()
        self.values={'source':'',
                     'ob_output':'./tmp/ob_raw_%s_%s'%(time.strftime('%m%Y'),str(random.randint(0,100))),
                     'tempfile':'%s'%(time.strftime('%m%Y')+'.tmp'),
                     'range':'0-184',
                     'passes':'1',
                     'mixflow':'5',
                     }
        if os.path.isfile('./tmp/'+self.values['tempfile']):
            self.values['tempfile'] = self.values['tempfile'] + '_' + str(random.randint(1000,9999))

    def run_action(self):
        if os.path.isfile(self.values['source']):
            os.system('python3 ./module/x86obf.py -i %s -o %s -r %s -p %s -f %s'
                      %(self.values['source'],
                        self.values['ob_output'],
                        self.values['range'],
                        self.values['passes'],
                        self.values['mixflow'],))
            time.sleep(2)
            print('\033[92m'+'[*]'+'\033[0m'+'ob_shellcode raw file was created succesfully ! ! ')
        else:
            print('Error!!!')

        if os.path.isfile(self.values['ob_output']):
            with open (self.values['ob_output'],'rb') as raw:
                shellcodec = binascii.hexlify(raw.read())
                shellcode_hex_string = shellcodec.decode()
                for char in re.findall("..",shellcode_hex_string):
                    with open('./tmp/'+self.values['tempfile'],'a') as temp:
                        temp.write("\\x" + char)
                else:
                    time.sleep(2)
                    print('\033[92m'+'[*]'+'\033[0m'+'------> shellcode readed <------')
                    time.sleep(2)
                    input(" Type any key to Continue!!! ")
        else:
            print('File Error!!!')