from .. import db


import random



def gen_oneliner(bot, user, *args):
    name =str(user['name'])
    one_liners = ["I tried cooking with wine yesterday for the first time... after 5 glasses I forgot why I was in the kitchen.",
                  "they say make up sex is the best, which is lucky, because all my sex is made up.",
                  "So.... my erectile dysfunction support group was a flop", "The Russian covid-19 vaccine is completely safe, with with иo side effects whatsoeveя and I feelshκι χoρoshό я чувствую.",
                  "I don't know what your problem is, but I'll bet it's hard to pronounce.",
                  name + ", everyone who has ever loved you was wrong",name+ ", I'm thinking you weren't burdened with an overabundance of schooling",
                  name + " How's your wife and my kids?", "You are the best argument for post-term abortion.",
                  "Everyone has the right to be stupid, but you're just abusing the privilege.",
                  "You have a face for radio", "You have a voice for the deaf", "May the rest of your day be as pleasant as you are.",
                  "I don't think you're stupid. You just have bad luck when thinking.",
                  "I may be drunk, Miss, but in the morning I will be sober and you will still be ugly.""I may be drunk, Miss, but in the morning I will be sober and you will still be ugly.",
                  "You're not being the person Mr. Rogers knew you could be.",
                  "I do desire we may be better strangers", "why don't you slip into something more comfortable, like a coma",
                  "I hope your children are born naked and illiterate!",
                  "I'd agree with you, but then we'd both be wrong",
                  "I'd explain it to you, but I have neither the time nor crayons.",
                  "Your mother should've swallowed you",name + ", no matter what everyone says about you, you're alright.",
                  "Your future self is going to be so disappointed", "You look like the kind of guy that would fuck a person in the ass, and not even have the god damn common courtesy to give him a reach around",
                 
                  "I don't really want to do that function. Bye.",
                  "Go suck a fuck", "Nobody has ever accused you of being smart",
                  "Normally I'd enjoy having a battle of wits, but I see that you are unarmed.",
                  "It's rude enough being alive when no one wants you.",
                  "Everyone who has ever left you was right.",
                  "Herr, wirf hirn vom himmel, oder steine haupstace er terrft", "I envy people who have never met you.",
                  "You couldn’t pour piss out of a boot if the instructions were on the heel",
                  "You're as useful as Anne Frank's drumkit.", "You and Rapunzel have a lot in common. Only Rapunzel let down her hair while you let down everyone in your life.",
                  "Somewhere in this world, a tree is tirelessly producing oxygen for your brain to function. You need to find that tree and apologize to it.",
                  "How tall are you?! I didn't know they stacked shit that high!", "You had best unfuck yourself or I will unscrew your head and shit down your neck!",
                  "If ‘unenthusiastic hand job’ had a face, "+name+" would be it.","“It’s not that obesity runs in your family, it’s that no one runs in your family",
                  "If you were half as smart as you think you are, you’d be twice as smart as you really are.",
                  "You're the reason that there's instructions on shampoo bottles.",
                  "Your mother was a hamster, and your father smelt of elderberries",
                  "I never forget a face. But in your case, I’ll make an exception."]

    send_line= random.choice(one_liners)

    bot.send_message(send_line)
        

    
 

