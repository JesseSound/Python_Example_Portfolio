import random
from .. import db
         
        
affections = [" cuzo", ' fam', ' bro', ' sweeterman', ' dimepiece', ' greezy' , ' guy', ' sweeter', ' wifey']
insults = [' waste yute',' sus', ' broke boys', ' bozos', ' buck-t', ' waste yute', ' snake', ' cyattie', ' cyat', ' thot',  ' dumb', ' NIZE it', ' bean', ' waste mon', ' weak', " that's beat", ' slime', ' mix up', ' gaffer']
intro = [' nyah eh', ' ah ah', ' jheeeez', ' so fam', ' so yoh', ' wagwan', ' HOOOOOOOOOOOLLLLLLLYYYYYY', ' topleft', ' say word', ' yoh guy']
verbs = [' hold a', ' breeze', ' run that', ' reach', ' flex', ' scoop me', ' Llow it', ' link up', ' come thru',  ' cut', ' scrap', ' rate', ' link up', ' regulate', ' bout it', ' tun up', ' two twos', ' rinse', ' feel', ' say less', ' light up' ]
verbs_pres = [' wheeling',' preeing',' coolin'," mossin'", ' gwannin', ' pushin', ' marvin']
adjectives = [' extra', ' greezy', ' lit', ' sav', ' cheesed', ' flex', ' wild' , ' waste', ' dry', ' weak', ' bare', ' breeze', ' yute', ' slimy', ' truuuu', ' snake', ' arms',' lowkey',' mix up', ' deafaz', ' differently', ' merked', ' sus', ' lowe', ' amped', ' blem', ' bless', ' cheesed', ' so beg', ' checking', ' chop', ' dealing', ' deezed' ]
verbs_past=[ ' copped', ' copped', ' blessed', ' rinsed', ' marved', ' merked']
nouns = [' sludem',' tings', ' ting', ' bill', ' fam', ' mandems', ' mans', ' Tdot', ' gyal', ' u', ' 6ix', ' liqs', ' lick boh', ' bogie', ' bitty', ' gyaldom', ' gyallis', ' mandem', ' backie', ' shawty', ' junior McChicken']
end_phrase = [' styll', ' ahlie', ' fom', ' live', ' boi', ' szeen', ' sketch', ' gyal', ' worldstarrr', ' like damn', ' u', ' are u dumb',' gheeeeeez!']
weird_prse = [' thats wild',' breeze', " that's beat", " don't cheese me", ' Yeah eh?', ' nahhh', ' scoop me', ' link up', ' truuu', ' dun kno', ' bout it', ' from time', ' run up']
weird_ins = [' finna', ' in a minute', ' from time',' are u dumb', ' chat to you']



def gen_mans(bot, user, *args):


    sent_forms = [random.choice(weird_prse) + random.choice(end_phrase), random.choice(weird_prse)+ random.choice(insults),random.choice(weird_prse)+ random.choice(affections), random.choice(intro) + ", are you tryna"+ random.choice(verbs)+"?",
                      random.choice(intro)+','+random.choice(nouns)+random.choice(adjectives)+ random.choice(weird_ins) + random.choice(verbs)+ random.choice(end_phrase), random.choice(intro)+" my"+ random.choice(affections), random.choice(intro)+","+random.choice(nouns)+" got"+ random.choice(verbs_past), random.choice(intro) + ", are you tryna"+ random.choice(verbs)+random.choice(nouns)+","+random.choice(insults),
                  random.choice(intro)+", I'm "+random.choice(verbs_pres)+' all these'+random.choice(nouns)+", yah" +random.choice(verbs)+random.choice(affections)+'?', random.choice(verbs)+" this"+random.choice(nouns),random.choice(verbs)+" this"+random.choice(insults), random.choice(nouns)+" a real"+random.choice(insults)+","+random.choice(end_phrase),
                  random.choice(verbs)+random.choice(verbs)+" this"+random.choice(nouns),"Say less"+ random.choice(affections),"Say less"+ random.choice(insults), random.choice(nouns)+ ' got bare'+ random.choice(nouns)+','+random.choice(end_phrase), random.choice(nouns)+ " is a" +random.choice(affections)+','+random.choice(end_phrase),
                  random.choice(nouns)+ " is a" +random.choice(insults)+','+random.choice(end_phrase), random.choice(nouns)+ ' got themselves a'+ random.choice(affections), random.choice(nouns)+ ' got themselves a'+ random.choice(nouns),random.choice(nouns)+ ' got themselves a'+ random.choice(insults), 'are yah'+ random.choice(insults)+random.choice(nouns), "I'm"+ random.choice(adjectives)+random.choice(verbs_past),"Who's"+random.choice(nouns)+" is this?",
                  random.choice(nouns)+' is'+ random.choice(verbs_past)+ random.choice(end_phrase),random.choice(nouns)+' tryna'+random.choice(verbs), "Tryna" +random.choice(verbs)+random.choice(nouns),"Tryna" +random.choice(verbs)+random.choice(affections),"Tryna" +random.choice(verbs)+random.choice(insults), random.choice(intro)+" check this"+ random.choice(insults),random.choice(intro)+" "+str(user['name'])+ ' are u' + random.choice(adjectives)+random.choice(end_phrase)]


    sent= random.choice(sent_forms)
    bot.send_message(sent)
    f = open("generatedslang.txt","a+")
    f.write(str(user['name'])+": "+sent +"\n")
    f.close()
    #return sent


