import socket
class irc(object):
    """docstring for irc."""
    def __init__(self, server, port, oauth, twitch_name, channel_name):
        super(irc, self).__init__()
        self.s = socket.socket() #Instanciate the socket
        self.server = server #Çhanging the namespace of the arguments parsed when instanciating the irc class 
        self.port = port
        self.oauth = str('oauth:') + oauth
        self.twitch_name = twitch_name
        self.channel_name = channel_name

    def send_to_server(self, message): #converts the message into a form which the irc server accepts and then sends it. This is usefull because the rest of the application doesn't have to deal with bytearrays
        self.regex_message = message + '\r\n' #appends \r\n to the message to make the irc client actually send the messages
        self.byte_message = self.regex_message.encode('utf-8') #Convert the message into a bytearray. This is requred as of python 3
        self.s.send(self.byte_message) #Call the socket.send function to send the converted message.

    def send_msg(self, message): # This function appends the neccesary information that the irc server requires to deliver the messages successfully to the right place.
        self.privmsg = 'PRIVMSG ' + self.channel_name + ' :' + message #Tells the server that this is a text message that is supposed to be sent to the chann self.channel_name
        self.send_to_server(self.privmsg)

    def connect(self): #This function uses all of the things that was passed into the class and uses it to make a connection through the socket to the irc server
        self.s.connect((self.server, self.port)) 
        self.send_to_server('PASS ' + self.oauth)
        self.send_to_server('NICK ' + self.twitch_name)
        self.send_to_server('JOIN ' + self.channel_name)
        print('Done authenticating with server')
        self.irc_loop() #See self.irc_loop()

    def get_args(self, message): #This function gets all the arguments following a command and append them to an array
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
