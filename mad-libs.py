def actionStory():
    nouns = list()
    adjectives = list()
    verbs = list()
    professions = list()
    names = list()
    print('I see you have chosen to make an action story with me today! What a good choice ' + name + '!')
    print('So lets start!')
    print('Lets make a list of 5 nouns to use in the story, they can be anything but lets try to make them action related.')
    for noun in range(5):
        nouns.append(input('-->'))
    
    print('Good! now we need to create some adjectives! give me 5 Adjectives to use in the story.')
    for adjective in range(5): 
        adjectives.append(input('-->'))
    
    print('Just a few more steps! lets now list out some verbs to use!')
    for verb in range(5):
        verbs.append(input('-->'))
   
    print('Now give me 5 professions.')
    for profession in range(5):
        professions.append(input('-->'))
    
    print('Now lastly give me some names for the charecters. 5 names would be great!')
    for newName in range(5):
        names.append(input())
    
    

def professionals(names, professions):
    


print('Hello! What is your name?')
name = input('-->')
print('It is so nice to meet you ' + name + '! Lets make an action story!')
actionStory()


