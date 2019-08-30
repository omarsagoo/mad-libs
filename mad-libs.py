from random import shuffle

def actionStory():
    nouns = list()
    adjectives = list()
    verbs = list()
    professions = list()
    names = list()

    print('So let\'s start!')
    
    print('Let\'s make a list of 5 nouns to use in the story, they can be anything but let\'s try to make them action related.')
    userInput(nouns)
    
    print('Good! now we need to create some adjectives! give me 5 Adjectives to use in the story.')
    userInput(adjectives)
    
    print('Just a few more steps! let\'s now list out some verbs to use!')
    userInput(verbs)
   
    print('Now give me 5 professions.')
    userInput(professions)
    
    print('Now lastly give me some names for the charecters. 5 names would be great!')
    userInput(names)

    randomize(names)
    randomize(professions)
    randomize(adjectives)
    randomize(verbs)
    randomize(nouns)

    print('It starts on a ' + adjectives[0] + ' day. Everything is nice and calm. Suddenly, ' + names[0] + ' busts through the door! They are a ' + professions[0] +
    '. They were wanting to ' + verbs[0] + ' in the very ' + adjectives[1] + ' building. Suddenly the doors exploded open and '+ adjectives[2] +' men with ' + nouns[0] +
     's burst through. they then arrested everyone that was involved. even ' + names[3] + ' who did nothing wrong. At the jail, the ' + adjectives[2] + ' ' +professions[1] + '. Who\'s name was ' +
     names[1] + ' decided to ' + verbs[1] + ' very ' + adjectives[3] + '. This made everyone very ' + adjectives[4] + '. After the jail everyone ' + verbs[2] + ' home to live a ' + adjectives[4] + ' life.')

   
    
#function for randomizing the pos inputs
def randomize(raw_lists):
    shuffle(raw_lists)

#function for collecting user input and storing it in the variable
def userInput(pos):
    for _ in range(5):
        pos.append(input('-->'))


print('Hello! What is your name?')
name = input('-->')
print('It is so nice to meet you ' + name + '! Lets make an action story!')
actionStory()


