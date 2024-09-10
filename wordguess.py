import random

#library that we use in order to choose
#on ramdom words from a list of words

name = input("What is your name???")
#here the user is asked to enter his/her name

print('Good luck!!!', name)

words = ['rainbow','python','computer','science','programming','math','condition'
,'reserve']
word = random.choice(words)