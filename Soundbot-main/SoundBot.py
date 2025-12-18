from twitchAPI import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope, ChatEvent
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
import asyncio

APP_ID = 'REMOVED_PRIVACY'
APP_SECRET ='REMOVED_PRIVACY'
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
TARGET_CHANNEL = 'REMOVED_PRIVACY'
yes = True

welcomed = []
# this will be called when the event READY is triggered, which will be on bot start
async def on_ready(ready_event: EventData):
    print('Bot is ready for work, joining channels')
    # join our target channel, if you want to join multiple, either call join for each individually
    # or even better pass a list of channels as the argument
    await ready_event.chat.join_room(TARGET_CHANNEL)
    print("joined chat succesfully")
    # you can do other bot initialization things in here


# this will be called whenever a message in a channel was send by either the bot OR another user
async def on_message(msg: ChatMessage):
    CURSES = ("you are bad", "Savko sucks", "Christmas songs are ok","jazz is good","bigfollows")
    print(f'in {msg.room.name}, {msg.user.name} said: {msg.text}')
    if msg.text in CURSES:
        print("sad")
        await msg.reply('why would you say that??')
        
    if msg.user.name not in welcomed:
        await msg.reply(f'Hello, {msg.user.name}! Welcome to the stream')
        welcomed.append(msg.user.name)
    if msg.user.name in welcomed:
        print('already welcomed')
        


# this will be called whenever someone subscribes to a channel
async def on_sub(sub: ChatSub):
    print(f'New subscription in {sub.room.name}:\n'
          f'  Type: {sub.sub_plan}\n'
          f'  Message: {sub.sub_message}')
    await sub.reply(f'Thanks for the sub, {sub.user.name} !')


# this will be called whenever the !reply command is issued
async def test_command(cmd: ChatCommand):
    if len(cmd.parameter) == 0:
        await cmd.reply('you did not tell me what to reply with')
    else:
        await cmd.reply(f'{cmd.user.name}: {cmd.parameter}')
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
    #chat.register_command()
    chat.start()
    await chat.send_message("jesse_sound", "It's me, SoundBot! Jesse answers with his voice, and I just exist digitally.")
    await asyncio.sleep(3600)
    
  

    
 


# lets run our setup

asyncio.run(run())
