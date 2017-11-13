class Menu:
    def __init__(self):
        self.options = []
        self.options.append(('scc'  , 'set custom msf_payload raw file path'))
        self.options.append(('mpr' , 'create common msf payload raw file'))
        self.options.append(('obf'  , 'obfuscate code(only for common rev_tcp)'))
        self.options.append(('exe' , 'pack python_file to exe by pyinstaller'))
        self.options.append(('msf' , 'start listener with msf'))
        self.options.append(('exit', 'bye-bye'))
        self.allowinput=[option[0] for option in self.options]
