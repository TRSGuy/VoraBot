import socket
class irc(object):
    """docstring for irc."""
    def __init__(self, server, port, oauth, twitch_name, channel_name):
        super(irc, self).__init__()
        self.s = socket.socket()
        self.server = server
        self.port = port
        self.oauth = str('oauth:') + oauth
        self.twitch_name = twitch_name
        self.channel_name = channel_name

    def send_to_server(self, message):
        self.regex_message = message + '\r\n'
        self.byte_message = self.regex_message.encode('utf-8')
        self.s.send(self.byte_message)

    def send_msg(self, message):
        self.privmsg = 'PRIVMSG ' + self.channel_name + ' :' + message
        self.send_to_server(self.privmsg)

    def connect(self):
        self.s.connect((self.server, self.port))
        self.send_to_server('PASS ' + self.oauth)
        self.send_to_server('NICK ' + self.twitch_name)
        self.send_to_server('JOIN ' + self.channel_name)
        print('Done authenticating with server')
        self.irc_loop()

    def get_args(self, message):
        try:
            tmp = message.split(' ')
            tmplen = len(tmp)
            tmp = tmp[1:tmplen]
            return tmp
        except(IndexError, AttributeError):
            return None

    def get_nick(self, text):
        tmp = text.split('@')
        try:
            self.final = tmp[0].split('!')[1]
            return self.final
        except(IndexError):
            return None

    def get_msg(self, text):
        try:
            split = text.split(':')[2]
            return split
        except(IndexError):
            return None

    def irc_loop(self):
        while 1:
            self.text = self.s.recv(2048)
            self.strtext = str(self.text)
            self.strtext = self.strtext[0:len(self.strtext) - 5]
            self.nick = self.get_nick(self.strtext)
            self.message = self.get_msg(self.strtext)
            self.args = self.get_args(self.message)
            self.command = 'None'
            try:
                self.commandBool = self.message.startswith('!')
            except(AttributeError):
                self.commandBool = False
            if(self.commandBool):
                self.command = str(self.message.split(' ')[0])

            print('RAW TEXT: ' + self.strtext)
            print('MESSAGE: ' + str(self.message))
            print('NICK: ' + str(self.nick))
            print('ARGS: ' + str(self.args))
            print('IS COMMAND: ' + str(self.commandBool))
            if(self.commandBool):
                print('COMMAND: ' + self.command)
            print('='*100)

            if('PING' in self.strtext):
                self.send_to_server('PONG :tmi.twitch.tv')
