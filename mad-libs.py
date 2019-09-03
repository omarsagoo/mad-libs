from random import shuffle


def action_story():
    nouns = list()
    adjectives = list()
    verbs = list()
    professions = list()
    names = list()

    print('So let\'s start!')
    
    print('Let\'s make a list of 3 nouns to use in the story, they can be anything but let\'s try to make them action related.')
    user_input(nouns, 3)
   
    print('Good! now we need to create some adjectives! give me 5 Adjectives to use in the story.')
    user_input(adjectives, 5)
   
    print('Just a few more steps! let\'s now list out some verbs to use!')
    user_input(verbs, 3)
    
    print('Now give me 2 professions.')
    user_input(professions, 2)
    
    print('Now lastly give me some names for the charecters. 2 names would be great!')
    user_input(names, 2)
   
    randomize(names)
    randomize(professions)
    randomize(adjectives)
    randomize(verbs)
    randomize(nouns)
   
    print('It starts on a ' + adjectives[0] + ' day. Everything is nice and calm. Suddenly, ' + names[0] + ' busts through the door! They are a ' + professions[0] +
    '. They were wanting to ' + verbs[0] + ' in the very ' + adjectives[1] + ' building. Suddenly the doors exploded open and '+ adjectives[2] +' men with ' + nouns[0] +
     's burst through. they then arrested everyone that was involved. even ' + names[1] + ' who did nothing wrong. At the jail, the ' + adjectives[2] + ' ' +professions[1] + '. Who\'s name was ' +
     names[1] + ' decided to ' + verbs[1] + ' very ' + adjectives[3] + '. This made everyone very ' + adjectives[4] + '. After the jail everyone ' + verbs[2] + ' home to live a ' + adjectives[4] + ' life.')

#function for randomizing the pos inputs
def randomize(raw_lists):
    shuffle(raw_lists)

#function for collecting user input and storing it in the variable
def user_input(pos, x):
    for _ in range(x):
        pos.append(input('-->'))


print('Hello! What is your name?')
name = input('-->')
print('It is so nice to meet you ' + name + '! Lets make an action story!')
action_story()