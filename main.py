import random as rn
import pyperclip as pc
adjectives = ['pretty', 'relaxing', 'calm', 'quiet', 'wonderful', 'nice', 'incredible', 'amazing', 'small', 'futuristic', 'cozy', 'beautiful']
objects = ['street', 'beach', 'mountain', 'landscape', 'lake', 'planet', 'city', 'river', 'valley', 'tiger', 'cat', 'house near a lake', 'house', 'house near the beach', 'skyscraper', 'nature']
styles = ['trending on artstation', 'oil painting', 'by greg rutkowski', 'trending on cgsociety', 'minimalistic', 'realistic', '8 k', '4 k', 'detailed', 'intricate', 'hyperdetailed', 'natural', 'colored', '35mm', 'award-winning photography', 'sharp focus']

#Add your own adjectives, objects and styles to the list above!

numadjectives = 5
numstyles = 10

listadj = rn.sample(adjectives, numadjectives)
adj = ', '.join(listadj)
obj = rn.choice(objects)
prompt = adj + ' ' + obj
liststyles = rn.sample(styles, numstyles)
sty = ', '.join(liststyles)
prompt = prompt + ', ' + sty
print(prompt)
pc.copy(prompt)
print('\nThe prompt has been copied to your clipboard')
