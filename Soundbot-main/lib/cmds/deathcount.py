from .. import db

OWNER = 'jesse_sound'
def death_count(bot, user, *args):

    with open("deathtrack.txt", 'r+') as reader:
        #print(reader.readline(5)) leave incase of large deaths
        deathstr = reader.readline()
        #print(deathstr) leave for debugging
        death_compare = int(deathstr)
        death = int(deathstr)
        death= death + 1
        #send death to twitch!
        #print(death)
        bot.send_message("Ahh shit, :( this brings my death count to: "+str(death)+" deaths. f")
         
        #deathtrack= str(death)
        if death > death_compare:
            f = open("deathtrack.txt",'w')
            f.write(str(death))
            f.close()
        else:
            pass
       
        


def death_tell(bot, user, *args):
    with open("deathtrack.txt","r") as read:
        death_tell = read.readline()
        if int(death_tell) == 0:
            bot.send_message("I have not died yet!")
        elif 1 <= int(death_tell) <= 5: 
            bot.send_message("I have died a total of: "+death_tell+" times. F :(")
        elif 6 <= int(death_tell) <= 9:
            bot.send_message("Shit, I need to get good. Death count: "+death_tell)
        elif 10 <= int(death_tell) <= 14:
            bot.send_message("I'm not bad, you're bad! Death count: "+ death_tell)
        elif 15 <= int(death_tell) <= 19:
            bot.send_message(" I blame "+str(user['name'])+". Death count: "+death_tell)
        elif 20 <= int(death_tell) <= 50:
            bot.send_message("I'm deleting the game after this stream. Death count: "+death_tell)
        else:
            bot.send_message("Cool. cool-cool-cool. Death count: " + death_tell)




def death_reset(bot, user, *args):
	if user["name"].lower() == OWNER:
		bot.send_message("resetting..")
		f = open("deathtrack.txt", 'r+')
		f.write("0")
		f.close()
		bot.send_message("reset!")

	else:
		bot.send_message("You can't do that.")
            
