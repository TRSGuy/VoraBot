#Imports
import VbIrcConnector as VbIrc
import VbCommands as VbCom
import VbSettings as VbSet
import threading

#Defines and Instances

sett = VbSet.settings('./settings/settings.txt')

server = sett.grab_setting('server')
port = int(sett.grab_setting('port'))
oauth = sett.grab_setting('oauth')
twitch_name = sett.grab_setting('twitch_name')
channel_name = sett.grab_setting('channel_name')

irc = VbIrc.irc(server, port, oauth, twitch_name, channel_name)
commands = VbCom.commands(sett.grab_setting('commands_path'))
#Threading
thread = threading.Thread(target=irc.connect)
thread.start()
