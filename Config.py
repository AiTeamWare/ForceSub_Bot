import os

class Config():
  #Get it from @botfather
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "1887382044:AAG3mTPscVcHV7pQ8lXF9Xg_lDAlDP0Od_Y")
  # Your bot updates channel username without @ or leave empty
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  # Heroku postgres DB URL
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  # get it from my.telegram.org
  APP_ID = os.environ.get("APP_ID", 4940448)
  API_HASH = os.environ.get("API_HASH", "c9fea4bfc51719d4d26d39151bb1ead5")
  # Sudo users( goto @JVToolsBot and send /id to get your id)
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "1204927413 1405957830").split()))
  SUDO_USERS.append(1204927413)
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username or channel ID} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n/source_code - To get bot source code😍\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
       "**Devloped By @AiTorrent_Ware**"
      ]
      SC_MSG = "**Hey [{}](tg://user?id={})**\n click on below👇 button to get my source code, for more help ask in my support group👇👇 "

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
