import pyttsx3
engine = pyttsx3.init()
#print('Enter what you think: ')
#dan=input()
engine.say('''Sampling is very often used in our daily life. For example while purchasing food grains from a
shop we usually examine a handful from the bag to assess the quality of the commodity. A
doctor examines a few drops of blood as sample and draws conclusion about the blood
constitution of the whole body. Thus most of our investigations are based on samples.''')
engine.runAndWait()
