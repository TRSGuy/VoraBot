#Imports
import VbIrcConnector as VbIrc #Used to handle the irc connection and communication to the irc server
import VbCommands as VbCom #Used to check for commands in the messages that are comming in through VbIrc
import VbSettings as VbSet #Used to grab settings from the ./settings/setttings.txt file
import threading

#Defines and Instances

sett = VbSet.settings('./settings/settings.txt') #instance settings

server = sett.grab_setting('server') #Grab server= in settings.txt file. This is the server address the VbIrc will try to connect to
port = int(sett.grab_setting('port')) #Grab server= in settings.txt file and convert it into an integer. This is the port that VbIrc will connect to
twitch_name = sett.grab_setting('twitch_name') #Grabs twitch_name= in settings file. This is the name of the twitch account that the oauth is asociated with
oauth = sett.grab_setting('oauth') #Creates the key.oauth file if it doesn't exist and then asks the user to input the oauth key for twitch. If the file does exist it just grabs what's in the file. This is used when authenticating with the twitch irc servers
channel_name = sett.grab_setting('channel_name') #Grabs channel_name= in settings file. This is the channel that the bot should be active in

irc = VbIrc.irc(server, port, oauth, twitch_name, channel_name) #Instancing VbIrc
commands = VbCom.commands(sett.grab_setting('commands_path')) #Instancing VbCom
#Threading
thread = threading.Thread(target=irc.connect) #put the main loop on a thread
thread.start() #Run the thread
