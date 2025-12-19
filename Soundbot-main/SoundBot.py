from twitchAPI import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope, ChatEvent
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
import asyncio
import random
import os
import oneLiners# type: ignore
import sentence_gen # type: ignore
import toronto_man # type: ignore
import savbot # type: ignore
APP_ID = 'shhhh'
APP_SECRET = 'shhhh'
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
TARGET_CHANNEL = 'shhh'
yes = True




#variables for other things
CURSES = ("you are bad", "Savko sucks", "Christmas songs are ok","jazz is good","bigfollows")
GOODBYES = ("goodbye", "good bye", "sayonara", "peace out", "see you later")


workspace_dir = os.path.dirname(os.path.abspath(__file__))
textfile = os.path.join(workspace_dir, "deathcount.txt")
slangfile = os.path.join(workspace_dir, "generatedslang.txt")
welcomed = []
# this will be called when the event READY is triggered, which will be on bot start
async def on_ready(ready_event: EventData):
    print('Bot is ready for work, joining channels')
    # join our target channel, if you want to join multiple, either call join for each individually
    # or even better pass a list of channels as the argument
    await ready_event.chat.join_room(TARGET_CHANNEL)
    print("joined chat succesfully")
    # you can do other bot initialization things in here
    print("trying txt file..")
    try:
        with open(textfile, "r+") as file:
            death = int(file.readline().strip())
            print("It worked! Death count is:", death)
    except FileNotFoundError:
        print("File not found, creating a new one...")
        with open(textfile, "w") as file:
            file.write("0")
            print("File created and initialized with 0 deaths")
    except Exception as e:
        print("An error occurred while reading the file:", e)

# this will be called whenever a message in a channel is sent by either the bot OR another user
async def on_message(msg: ChatMessage):
    try:
        room_name = msg.room.name if msg.room and hasattr(msg.room, "name") else "UnknownRoom"
        user_name = msg.user.name if msg.user and hasattr(msg.user, "name") else "UnknownUser"

        print(f'in {room_name}, {user_name} said: {msg.text}')

        if msg.text in CURSES:
            print("sad")
            await msg.reply('why would you say that??')
        elif user_name not in welcomed:
            await msg.reply(f'Hello, {user_name}! Welcome to the stream')
            welcomed.append(user_name)
        elif msg.text in GOODBYES:
            print(f"{user_name} is leaving")
            await msg.reply(f"Goodbye {user_name}")
            welcomed.remove(user_name)    
        elif user_name in welcomed:
            print('already welcomed')
    except Exception as e:
        print("An error occurred while trying to handle messages:", e)


# this will be called whenever someone subscribes to a channel
async def on_sub(sub: ChatSub):
    print(f'New subscription in {sub.room.name}:\n'
          f'  Type: {sub.sub_plan}\n'
          f'  Message: {sub.sub_message}')
    await sub.reply(f'Thanks for the sub, {sub.user.name} !')

#coinflipper
async def coin_flip(cmd: ChatCommand):
    result = random.choice(["heads", "tails"])
    await cmd.reply("The coin is: " + result)
# this will be called whenever the !reply command is issued
async def test_command(cmd: ChatCommand):
    if len(cmd.parameter) == 0:
        await cmd.reply('you did not tell me what to reply with')
    else:
        await cmd.reply(f'{cmd.user.name}: {cmd.parameter}')
#death trackers
async def death_add(cmd: ChatCommand):
    with open(textfile, "r+") as file:
        death = int(file.readline().strip())
        death +=1
             # Update the death count in the file
        file.seek(0)  # Move the file cursor to the beginning
        file.write(str(death))  # Update the death count in the file
        file.truncate()  # Remove any extra characters beyond the new count
        print("Death count updated")

        await cmd.reply( f"Ah, dang! This brings my death count to: " + str(death) + " deaths. F. jesses15Aghhhh")

      
async def death_tell(cmd: ChatCommand):
    with open(textfile, "r") as file:
        death_count = int(file.readline().strip())
        
        if death_count == 0:
            message = "I have not died yet!"
        elif 1 <= death_count <= 5:
            message = f"I have died a total of: {death_count} times. F :("
        elif 6 <= death_count <= 9:
            message = f"Shit, I need to get good. Death count: {death_count}"
        elif 10 <= death_count <= 14:
            message = f"I'm not bad, you're bad! Death count: {death_count}"
        elif 15 <= death_count <= 19:
            if welcomed:
                message = f"I blame {random.choice(welcomed)} Death count: {death_count}"
            else:
                message = f"Death count: {death_count}"

        elif 20 <= death_count <= 50:
            message = f"I'm deleting the game after this stream. Death count: {death_count}"
        else:
            message = f"Cool. cool-cool-cool. Death count: {death_count}"
        await cmd.reply(message)
async def death_reset(cmd: ChatCommand):
    if cmd.user.name.lower() == "jesse_sound":
        await cmd.reply("Resetting death count...")
        with open(textfile, "w") as file:
            file.write("0")
        await cmd.reply("Reset complete.")


#One liners and various generators

async def one_liner(cmd: ChatCommand):
    name = cmd.user.name
    send = oneLiners.random_insult(name)
    await cmd.reply(send)


async def sentence_make(cmd: ChatCommand):
    send = sentence_gen.chomsky_sent()
    await cmd.reply("Chomsky says: " + send)

async def toronto_slang(cmd: ChatCommand):
    send = toronto_man.gen_mans()
    name = str(cmd.user.name).lower()
    with open(slangfile, "a") as f:
        f.write(name + ": " +send + "\n")  # Append the message followed by a newline
    await cmd.reply( send)
    print("wrote and closed the file")


async def sav_gen(cmd: ChatCommand):
    name = random.choice(welcomed)
    send = savbot.gen_quote(name)
    await cmd.reply(send)



#function to list all the commands viewers can use
async def command_list(cmd: ChatCommand):
    await cmd.reply('Here are the different commands you can use! try em out!: !reply, !coinflip, !death, !death+, !insults, !chomsky, !torontoslang, !discord, !savkosays, !commandlist')

async def discord(cmd:ChatCommand):
    await cmd.reply(" You can join my personal discord here!: ")

async def run():
   
    # set up twitch api instance and add user authentication with some scopes
    twitch = await Twitch(APP_ID, APP_SECRET)
    auth = UserAuthenticator(twitch, USER_SCOPE)
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    # create chat instance
    chat = await Chat(twitch)
    
   
    chat.register_event(ChatEvent.READY, on_ready)
    # listen to chat messages
    chat.register_event(ChatEvent.MESSAGE, on_message)
    # listen to channel subscriptions
    chat.register_event(ChatEvent.SUB, on_sub)
    # there are more events, you can view them all in this documentation

    # you can directly register commands and their handlers, this will register the !reply command
    chat.register_command('reply', test_command)
    chat.register_command('coinflip', coin_flip)
    chat.register_command('death+',death_add)
    chat.register_command('death',death_tell)
    chat.register_command('deathreset',death_reset)
    chat.register_command('insults', one_liner)
    chat.register_command('chomsky', sentence_make)
    chat.register_command('torontoslang', toronto_slang)
    chat.register_command('commandlist', command_list)
    chat.register_command('discord', discord)
    chat.register_command('savkosays', sav_gen)
    chat.start()
    await chat.send_message("jesse_sound", "It's me, SoundBot! Jesse answers with his voice, and I just exist digitally.")
    await asyncio.Event().wait()
    
  

    
 


# lets run our setup

asyncio.run(run())
