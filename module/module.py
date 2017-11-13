class Moduleobject:
    def __init__(self):
        self.allow=[]
        self.allow.append(("show","show module variables"))
        self.allow.append(('set', 'set value'))
        self.allow.append(('run', "run the module"))
        self.allow.append(('back','Go back'))

    def show_allowed(self):
        for command in self.allow:
            print('\t[*]%s\t----> %s'%command)

    def show_vars(self):
        print ('The value you have to set\n')
        for value,key in self.values.items():
            print('\033[94m'+'[+]'+'\033[0m'+value.ljust(12,' ') +'>>>'.center(10,' ')+'%s'%key)

    def show_menu(self):
        self.show_vars()
        print('-'*50)
        print("Allow options:\n")
        self.show_allowed()
        print('-'*50)

    def input_allow_action(self,action):
        for allow_action in self.allow:
            if action in allow_action[0]:
                return True
        return False

    def exec_action(self,data):
        execute = data.split(' ',1)[0]
        if execute == "run":
            self.run_action()
        if execute == "set":
            self.set_action(data)
        if execute == "show":
            self.show_vars()

    def do_action(self,banner):
        exit_module_flag=False
        while not exit_module_flag:
            self.show_menu()
            action = input("operation >>> ")
            if action == 'back':
                exit_module_flag = True

            if self.input_allow_action(action.split(' ')[0]):
               self.exec_action(action)
               banner()
            else:
               banner()

    def set_action(self,vars):
        try :
            act,key,value = vars.split(' ',2)
        except:
            pass
        if key in self.values:
            self.values[key] = value
        else:
            print("Invalid variable")
