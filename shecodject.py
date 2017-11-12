import os
import sys
file = os.getcwd()
sys.path.insert(0,file+'/module')
from core.ui import UI,color
from core.Menu import Menu

from shellcode_path import shellcode
from obfuscation import obshellcode
from msfvenom import msf_origin_raw
from make_exe import exe_options
from listener import msflistener


if __name__ == "__main__":

    if not os.path.exists('output/'):
        os.mkdir('output')

    if not os.path.exists('tmp/'):
        os.mkdir('tmp/')

    #pathfile
    shellcode_temp = ''
    msfconsole_rc = ''
    shellcode_raw = ''

    #initialize
    exit_flag = False
    ui = UI()
    menu = Menu()
    Color=color()

    #Menu initial
    while not exit_flag:
        ui.banner()
        menu_show = ui.showmenu(menu.options)
        choice = input("selected option >>> ")
        if choice in menu.allowinput:
            mod = None
            if choice == 'exit':
                exit_flag=True
            if choice == 'scc':
                mod = shellcode(ui)
                mod.do_action(ui.banner)
                shellcode_temp = './tmp/'+mod.values['tempfile']
            if choice == 'mpr':
                mod = msf_origin_raw(ui)
                mod.do_action(ui.banner)
                shellcode_raw = mod.outraw
                shellcode_temp = './tmp/'+mod.values['tempfile']
                msfconsole_rc = mod.msfrc
            if choice == 'obf':
                mod = obshellcode(ui)
                mod.values['source'] = shellcode_raw
                mod.do_action(ui.banner)
                shellcode_temp = './tmp/'+mod.values['tempfile']
            if choice == 'exe':
                mod = exe_options(ui)
                mod.values['source'] = shellcode_temp
                mod.do_action(ui.banner)
            if choice == 'msf':
                mod = msflistener(ui)
                mod.values['source'] = msfconsole_rc
                mod.do_action(ui.banner)

        else:
            print(Color.FAIL+"Invalid operation"+Color.ENDC)
