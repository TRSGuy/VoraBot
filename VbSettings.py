import VbCommon, os
class settings(object):
    def __init__(self, path):
        """docstring for settings."""
        super(settings, self).__init__()
        self.path = path
        self.read_settings()
        self.common = VbCommon.common()

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

    def grab_oauth(self):
        path = grab_setting('oauth_path')
        if(os.path.exist(path)):
            with open(path, 'r') as f:
                data = f.read()
            return data
        else:
            print('The oauth key was not found at the specified path')
            oauth = input_raw('Please enter your oauth key without the oauth: part: ')
            with open(path, 'a') as f:
                f.write(oauth)
            return oauth

    def grab_setting(self, setting):
        if(settings == 'oauth'):
            search = self.grab_oauth()
        else:
            search = self.common.search_array(self.settings_lst, setting, 'VbSettings')
        return search
