from random import shuffle

def actionStory():
    nouns = list()
    adjectives = list()
    verbs = list()
    professions = list()
    names = list()
    print('I see you have chosen to make an action story with me today! What a good choice ' + name + '!')
    print('So let\'s start!')
    
    print('Let\'s make a list of 5 nouns to use in the story, they can be anything but let\'s try to make them action related.')
    userInput(nouns)
    
    print('Good! now we need to create some adjectives! give me 5 Adjectives to use in the story.')
    userInput(adjectives)
    
    print('Just a few more steps! lets now list out some verbs to use!')
    userInput(verbs)
   
    print('Now give me 5 professions.')
    userInput(professions)
    
    print('Now lastly give me some names for the charecters. 5 names would be great!')
    userInput(names)

    randomize(names)
    randomize(professions)
    
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


