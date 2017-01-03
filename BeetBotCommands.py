class commands(object):
    """docstring for commands."""
    def __init__(self, path):
        super(commands, self).__init__()
        self.path = path
        self.command_array = []
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
        except Exception as e:
            print('Command ' +command+' not found')
            raise

    def grab_command_info(self, command):
        path = self.grab_command_path(command)
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
    def search_help(self, )
