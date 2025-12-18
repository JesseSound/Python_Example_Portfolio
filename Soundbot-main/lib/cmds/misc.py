from datetime import timedelta
from sys import exit
from time import time

from .. import db

BOOT_TIME = time()
OWNER = "jesse_sound"
dis = "https://discord.gg/aR6MD3T"
mydis = "https://discord.gg/9GfuYgNGC7"
mvmbr= "https://movember.com/t/code-ninjas-barrie?mc=1"
def help(bot, prefix, cmds):
	bot.send_message(f"Registered commands: "
		+ ", ".join([f"{prefix}{cmd.callables[0]}" for cmd in sorted(cmds, key=lambda cmd: cmd.callables[0])]))

	bot.send_message(f"Registered commands (incl. aliases): "
		+ ", ".join([f"{prefix}{'/'.join(cmd.callables)}" for cmd in sorted(cmds, key=lambda cmd: cmd.callables[0])]))


def about(bot, user ,*args):
	bot.send_message("Jesse's Chatbot. Welcome to the stream!")


def hello(bot, user, *args):
	bot.send_message(f"Hey {user['name']}!")


def uptime(bot, user, *args):
	bot.send_message(f"The bot has been online for {timedelta(seconds=time()-BOOT_TIME)}.")


def userinfo(bot, user, *args):
	bot.send_message(f"Name: {user['name']}. ID: {user['id']}.")


def shutdown(bot, user, *args):
	if user["name"].lower() == OWNER:
		bot.send_message("Shutting down.")
		db.commit()
		db.close()
		bot.disconnect()
		exit(0)

	else:
		bot.send_message("You can't do that.")

def discord(bot,user, *args):
        bot.send_message("Come and join the Thirst Chat Conga discord: "+ dis)
        bot.send_message("Join my personal discord server!:  " + mydis)

def lurk(bot, user, *args):
        bot.send_message("Thanks for lurking! I appreciate the support!")

def donate(bot, user, *args):
        bot.send_message("Wow! You Want To Donate? You'll have to use my paypal link:")
        bot.send_message("https://paypal.me/jessesound?locale.x=en_US")

def so(bot, user, *args):
        pass
def court(bot, user, *args):
        bot.send_message(" Check out the spotify link here! https://open.spotify.com/artist/1L7OPN18gcuZj2dgYehAqS?si=G3ugxI4sQ0SF9MlLtt_1HA")
        bot.send_message("Youtube link: https://www.youtube.com/channel/UC_hSp61vpH7Lkh-qYqGu_8g")
        bot.send_message("Instagram : https://www.instagram.com/courtbowl/")
        bot.send_message("Facebook Link: https://www.facebook.com/courtbowles")
