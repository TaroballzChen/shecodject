import os

class color:
    def __init__(self):
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

Color=color()

class UI:
    Version = "1.0"

    def __init__(self):
        pass

    def clearscreen(self):
        os.system('clear')

    def banner(self):
        self.clearscreen()
        print(r"       __                                __                       __      ")
        print(r"      /\ \                              /\ \    __               /\ \__   ")
        print(r"  ____\ \ \___      __    ___    ___    \_\ \  /\_\     __    ___\ \ ,_\  ")
        print(r" /',__\\ \  _ `\  /'__`\ /'___\ / __`\  /'_` \ \/\ \  /'__`\ /'___\ \ \/  ")
        print(r"/\__, `\\ \ \ \ \/\  __//\ \__//\ \L\ \/\ \L\ \ \ \ \/\  __//\ \__/\ \ \_ ")
        print(r"\/\____/ \ \_\ \_\ \____\ \____\ \____/\ \___,_\_\ \ \ \____\ \____\\ \__\'")
        print(r" \/___/   \/_/\/_/\/____/\/____/\/___/  \/__,_ /\ \_\ \/____/\/____/ \/__/")
        print(r'                                               \ \____/                   ')
        print(r'    shecodject  autoscript                      \/___/                    ')
        print(r'                 __          by                                  __      ')
        print(r'                /\ \__           OneTeam  Taroballz   __        /\ \__   ')
        print(r'   __     __  __\ \ ,_\   ___     ____    ___   _ __ /\_\  _____\ \ ,_\  ')
        print(r" /'__`\  /\ \/\ \\ \ \/  / __`\  /',__\  /'___\/\`'__\/\ \/\ '__`\ \ \/  ")
        print(r'/\ \L\.\_\ \ \_\ \\ \ \_/\ \L\ \/\__, `\/\ \__/\ \ \/ \ \ \ \ \L\ \ \ \_ ')
        print(r'\ \__/.\_\\ \____/ \ \__\ \____/\/\____/\ \____\\ \_\  \ \_\ \ ,__/\ \__\'')
        print(r' \/__/\/_/ \/___/   \/__/\/___/  \/___/  \/____/ \/_/   \/_/\ \ \/  \/__/')
        print(r'                                                             \ \_\       ')
        print(r'                                                              \/_/       ')

    def showmenu(self,options):
        print('select an options:',end='\n')
        for option in options:
            print('\t' + Color.OKBLUE + '[*]' + Color.ENDC,'%s \t---------> %s' % option )
        else:
            print("-------------------------------------------------------------------------------")

