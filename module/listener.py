import os
from module import Moduleobject

class msflistener(Moduleobject):
    def __init__(self,ui):
        super(msflistener,self).__init__()
        self.ui=ui
        ui.banner()
        self.values={'source':'',
                     'IP':'',
                     'Port':'',
                     'payload':'',
                     }

    def run_action(self):
        if self.values['source']:
            os.system('msfconsole -r %s'%self.values['source'])
        else:
            os.system('msfconsole -r %s')
            os.system('msfconsole -x "use multi/handler;set PAYLOAD %s;set LHOST %s;set LPORT %s;exploit -j -z"'
                      % (self.values['payload'],
                         self.values['IP'],
                         self.values['Port'],))