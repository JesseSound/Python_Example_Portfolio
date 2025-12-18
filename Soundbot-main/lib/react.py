from collections import defaultdict
from datetime import datetime, timedelta
from random import randint
from re import search
from time import time

from . import db


welcomed = []
messages = defaultdict(int)


def process(bot, user, message):
	update_records(bot, user)

	if user["id"] not in welcomed:
		welcome(bot, user)

	elif "bye" in message:
		say_goodbye(bot, user)

	

	if (match := search(r'cheer[0-9]+', message)) is not None:
		thank_for_cheer(bot, user, match)

	
def add_user(bot, user):
	db.execute("INSERT OR IGNORE INTO users (UserID, UserName) VALUES (?, ?)",
		user["id"], user["name"].lower())


def update_records(bot, user):
	db.execute("UPDATE users SET UserName = ?, MessagesSent = MessagesSent + 1 WHERE UserID = ?",
		user["name"].lower(), user["id"])

	
def welcome(bot, user):
	bot.send_message(f"Welcome to the stream {user['name']}!")
	welcomed.append(user["id"])


def say_goodbye(bot, user):
	bot.send_message(f"See ya later {user['name']}!")
	welcomed.remove(user["id"])




def thank_for_cheer(bot, user, match):
	bot.send_message(f"Thanks for the {match.group[5:]:,} bits {user['name']}! That's really appreciated!")
