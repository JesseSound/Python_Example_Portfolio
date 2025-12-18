from .. import db


import random



def gen_quote(bot, user, *args):
    verbs = ['fuck','kill','wreck','eat','suck','lick']
    adjectives = ['whole','little','big','fucking','shitty','dumb','giant']
    nouns = ['hole', 'career', 'duck','move','bullshit','fuck','ass','gun','axe','jeans hole','game','video game','career hole', 'JEESUS','shit','min','dammit','bitch','uuuuh... move', 'secret asshole', 'bow']
    expletives = ['FUCK','SHIT','JEESUS', 'DAMNIT', 'WTF', 'EXCUSE ME', 'GOD']

   

    random_verb = random.choice(verbs)
    random_noun = random.choice(nouns)
    random_adjective = random.choice(adjectives)
    random_adjective2 = random.choice(adjectives)
    random_name = str(user['name'])
    
    random_expletive = random.choice(expletives)
    

    sentence_formats = [random_verb + ' my ' + random_noun, random_verb +' my '+random_adjective+' '+random_noun,'You know what they say, '+random_verb+' my '+ random_noun,
                        'You know what they say, '+random_verb+' my '+random_adjective+' '+ random_noun,'Yeah, '+random_noun+ ' could be a vibe','Guys, I never say this, but '+random_verb+' my '+random_noun,
                        'Guys, I never say this, but '+random_verb+' my '+random_adjective+' '+random_noun, random_noun +' to meet you', "OOH it's a "+random_adjective+' '+ random_noun +'-min',
                        "OOOOH it's a "+random_noun+'-min', random_expletive+'! '+random_name+'........ '+random_name+', PLEASE tell me something good about your day!',
                        'I fucking hate this '+random_adjective+' '+random_noun, 'Eh? You like that huh? You '+random_adjective+' '+random_noun+'. Fuck you.', "I'm a fucking "+random_noun, 'Wait, am I the '+random_noun+'?',
                        random_name+ " thanks so much for tuning in, I'll see you around", 'This game can '+random_verb+' a '+random_adjective+' '+random_noun,'I hate this '+random_expletive+' game',
                        'uhh mods please ban ' +random_name, 'Oooh, its a '+random_adjective+', uuuuuh, a '+random_adjective+' '+random_noun,
                        "I can't believe this "+random_adjective+' '+random_noun+' is so fucking '+random_adjective2,
                        'Fuck my ' +random_noun+' for free','I am the greatest video game player of all time','Awww, '+random_name+'. AHHHHH! Thank you so much for your gift sub to '+random_name,
                        'Imagine being a '+random_adjective+ ' '+random_noun, 'This '+random_noun+ ' is so fucked','This '+random_noun+ ' is so '+random_adjective,
                        'Imagine being so '+random_adjective+" you couldn't even " +random_verb+' a '+random_adjective2+' '+random_noun, "Can we get a new game? I don't wan't to cry anymore",'Hey '+random_name+', on a scale of 1 to '+random_noun+ ' how '+ random_adjective+' are you tonight?']
  
    sav_says= random.choice(sentence_formats)
    
        

    
    bot.send_message(sav_says)

