with open('settings/settings.txt', 'r') as f:
    read_data = f.read()

class settings(object):
    """docstring for settings."""
    def __init__(self, path):
        super(settings, self).__init__()
        self.path = path
        self.read_settings()
    def read_settings(self):
        with open(self.path, 'r') as f:
            self.data = f.read()
        print(self.data)
        self.split_data = self.data.split('\n')
        self.settings_lst = []
        for i in self.split_data:
            tmp_index = self.split_data.index(i)
            tmp = i.split('=')
            for i in tmp:
                self.settings_lst.append(i)
        for i in self.settings_lst:
            tmp = ''
            if (self.settings_lst.index(i) % 2 == 0):
                tmp = str(i) + ': '
            else:
                tmp = tmp + i  + ' \n'
            print(tmp)

    def grab_setting(self, setting):
        try:
            self.setting_index = self.settings_lst.index(setting)
            self.setting_value = self.settings_lst[self.setting_index + 1]
            return self.setting_value
        except Exception as e:
            print(e)
            print('Can not find setting: ' + str(setting))
            pass
