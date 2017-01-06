import VbCommon
class commands(object):
    """docstring for commands."""
    def __init__(self, path):
        super(commands, self).__init__()
        self.path = path
        self.command_array = []
        self.VbCommon = VbCommon.common()
        self.read_commands()

    def read_commands(self):
        with open(self.path, 'r') as f:
            self.data = f.read()
        self.data = self.data.split('\n')
        for i in self.data:
            tmp_index = self.data.index(i)
            tmp = i.split('=')
            for i in tmp:
                self.command_array.append(i)

    def grab_command_path(self, command):
        try:
            command_index = self.command_array.index(command)
            return self.command_array[command_index + 1]
        except ValueError:
            print('Command ' +command+' not found')
            return None

    def grab_command_info(self, command):
        path = self.grab_command_path(command)
        if(path == None):
            return 'No such command'
        else:
            with open(path, 'r') as f:
                command_info = f.read()
            return command_info

    def help_command(self, command):
        self.info = self.grab_command_info(command)
        self.info = self.info.split('\n')
        self.info_array = []
        for i in self.info:
            tmp_index = self.info.index(i)
            tmp = i.split('=')
            for i in tmp:
                self.info_array.append(i)
        self.help_string = ''
        self.name = self.VbCommon.search_array(self.info_array, 'name')
        self.desc = self.VbCommon.search_array(self.info_array, 'description')
        self.use = self.VbCommon.search_array(self.info_array, 'usage')
        if(self.name == 'No such command' and self.desc == 'No such command' and self.use == 'No such command'):
            self.help_string = 'No such command' + str(command)
        else:
            self.help_string = 'Help for command ' + str(self.name) + '. ' + str(self.name) + ' ' + str(self.desc) + '. Usage: ' + str(self.use)
        return self.help_string
