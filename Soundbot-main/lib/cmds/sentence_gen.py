from .. import db
import random
#define words to fill certain grammar roles
adjective =[' whole',' little', ' big',' fucking',' shitty',' dumb',' giant',' sassy', ' ultra', ' mellow', ' receptive', ' grouchy', ' empty' , ' secretive', ' troubled', ' rapid', ' tranquil', ' electrical', ' sufficient', ' motionless', ' mere', ' adaptable', ' toothy', ' humourous', ' luxuriant', ' unwieldy', ' cheerful', ' curious', ' earsplitting', ' cuddly', ' available', ' ritzy', ' ditzy', ' plain', ' swanky', ' janky', ' jittery', ' faded', ' jaded', ' longing', ' aloof', ' colorful', ' colorless', ' naughty', ' steep', ' gleaming', ' alert', ' modern', ' many', ' agonizing', ' faulty', ' brainy', ' huge', ' weak', ' tremendous', ' disturbed', ' general', ' economic', ' unbiased', ' tame', ' holistic', ' smart', ' abandoned', ' makeshift', ' crazy', ' brown', ' moist', ' evasive', ' technical', ' crippling']
noun = [ ' hole', ' career', ' duck',' move',' bullshit',' fuck',' ass',' gun',' axe',' jeans hole',' game',' video game', ' JEESUS',' shit', 'dammit',' bitch',' uuuuh... move', ' secret asshole', ' bow', ' bath', ' bow', ' university', ' area', ' bird', ' error', ' quantity', ' freedom', ' coffee', ' coke', ' molly', ' situation', ' menu', ' recommendation', ' difference', ' region', ' establishment', ' statement', ' user', ' king', ' movie', ' lab', ' assistance', ' computer', ' Fall Guys', ' Halo', ' Among Us', ' Discord', ' version', ' cookie', ' story', ' drawing', ' girl', ' guest', ' currency', ' steak', ' bass', ' tooth', ' boy', ' non-binary', ' anal', ' mom', ' dad', ' complaint', ' world', ' ocean', ' depression', ' meat', ' library', ' army', ' Tik Tok', ' village', ' blood', ' hospital', ' thought']
verb =[' fuck',' kill',' wreck',' eat',' eats', ' sucks',' lick', ' shine', ' declare', ' correct', ' confine', ' reward', ' forgive', ' roll', ' say', ' demonstrate', ' erect', ' decide', ' await', ' search', ' proclaim', ' long', ' confirm', ' express', ' want', ' repair', ' progress', ' perform', ' contribute', ' dissolve', ' command', ' capture', ' connect', ' hate', ' drop', ' suit', ' shape', ' gaze', ' enter', ' spell', ' signal', ' brush', ' desire', ' leave', ' organize', ' convert', ' exhibit', ' touch', ' approve', ' enter', ' says', ' speaks', ' touches', ' laugh', ' accuse', ' hope', ' end', ' advance', ' appreciate', ' work', ' mount', ' explore', ' overcome', ' jizz', ' vanish', ' banish', ' protest', ' become', ' kick', ' hit', ' omit', ' sit', ' plunge', ' phone', ' deprive', ' market', ' equip', ' bid', 'narrow', ' invest', ' represent',  ' attain'] 
determiner =[" the"," a"," some", " which", " both", " this", " an",' a few', ' a little',' much',' many',' a lot of',' most',' some',' any', ' enough', ' that', ' these', ' those', ' first', ' second', ' third', ' next', ' last', ' all', ' all of', ' what', ' such', ' rather', ' quite', ' twice', ' double', ' both'] 
prep_phrase = [" to"," in"," on", " up", " inside", " as", 'at a rate of', ' at a speed of', ' at a standstill', ' at all costs', ' at least', ' at length', ' at issue',' in addition to', ' at most,', ' at noon', ' out of respect for', ' in spite of', ' in harmony with', ' in honor of', ' in fear of', ' by force of', ' by', ' in', ' on', ' at', ' on suspicion of', ' on order of', ' on the brink of', ' on the edge of', ' on behalf of', ' at a speed of', ' at a rate of', ' in answer to', ' by the name of', ' in the name of', ' for the love of', ' for the good of', ' for lack of', ' for fear of' ] 
adverb = [" abruptly", " absently", " close", " commonly", " coolly", " dearly", " delightfully"," arrogantly", " angrily", " bashfully", " freely", " messily",' cleverly', ' comprehensively', ' profanely', ' commonly', ' inexpectedly', ' preventively', ' being', ' purposefully', ' muddily', ' after', ' thoroughly', ' defiantly', ' inwardly', ' outwardly', ' needily', ' literally', ' less', ' gracefully', ' truly', ' loosely', ' slightly', ' steadily', ' annually', ' upwardly', ' perfectly', ' arrogantly', ' thus', ' softly', ' ahead', ' cheerfully', ' unethically', ' annually', ' poorly', ' never', ' instantly', ' sometimes', ' slowly', ' viciously', ' correctly', ' incorrectly']
 
def chomsky_sent(bot, user, *args):

    
    #generate less random gibberish
    optional = random.randint(1,11)
    print(optional)
    if optional == 1:
        noun_phrase = random.choice(determiner) +random.choice(adjective)+ random.choice(noun) +random.choice(prep_phrase)
        verb_phrase= random.choice(verb) + random.choice(adverb)
        sentence = noun_phrase + verb_phrase
        bot.send_message(sentence)
        #return sentence
    if optional == 2:
        noun_phrase = random.choice(adjective) + random.choice(noun) 
        verb_phrase = random.choice(verb)
        sentence = noun_phrase + verb_phrase
        bot.send_message("Chomsker says:"+ sentence)
        #return sentence
    if optional == 3:
        noun_phrase = random.choice(determiner)+random.choice(adjective) ++ random.choice(noun) +random.choice(prep_phrase)
        verb_phrase = random.choice(verb)
        sentence = noun_phrase + verb_phrase
        bot.send_message("Chomsker says:"+ sentence)
        #return sentence
    if optional == 4:
        noun_phrase = random.choice(determiner) + random.choice(noun)+ random.choice(adjective)
        verb_phrase= random.choice(verb)
        sentence = noun_phrase + verb_phrase
        bot.send_message("Chomsker says:"+ sentence)
        #return sentence
    if optional == 5:
        noun_phrase = random.choice(determiner) + random.choice(noun)
        verb_phrase= random.choice(verb) + random.choice(adverb)
        sentence = noun_phrase + verb_phrase
        bot.send_message("Chomsker says:"+ sentence)
        #return sentence
    if optional == 6:
        noun_phrase = random.choice(adjective) + random.choice(noun) 
        verb_phrase = random.choice(verb) + random.choice(adverb)
        sentence = noun_phrase + verb_phrase
        #return sentence
    if optional == 7:
        noun_phrase = random.choice(determiner) + random.choice(noun) 
        verb_phrase = random.choice(verb)+random.choice(verb) + random.choice(adverb)+random.choice(determiner)+random.choice(noun)
        sentence = noun_phrase + verb_phrase
        bot.send_message("Chomsker says:"+ sentence)
        #return sentence
    if optional == 8:
        noun_phrase = random.choice(determiner) + random.choice(noun) 
        verb_phrase = random.choice(verb) 
        verb_phrasetwo = random.choice(verb) + random.choice(adverb)+random.choice(determiner)+random.choice(noun)
        sentence = noun_phrase + verb_phrase + verb_phrasetwo
        bot.send_message("Chomsker says:"+ sentence)
        #return sentence
    if optional == 9:
        noun_phrase =random.choice(determiner)+ random.choice(adjective) + random.choice(adjective)+random.choice(noun) 
        verb_phrase = random.choice(verb)
        sentence = noun_phrase + verb_phrase
        bot.send_message("Chomsker says:"+ sentence)
        #return sentence
    if optional == 10:
        noun_phrase = random.choice(adjective) + random.choice(adjective) +random.choice(noun) 
        verb_phrase = random.choice(verb)
        sentence = noun_phrase + verb_phrase
        bot.send_message("Chomsker says:"+ sentence)
    if optional == 11:
        sentence = random.choice(adjective)+random.choice(adjective)+random.choice(noun)+random.choice(verb)+random.choice(adverb)
        bot.send_message("Chomsker says:"+ sentence)
        #return sentence
#print(chomsky_sent())
         
        
