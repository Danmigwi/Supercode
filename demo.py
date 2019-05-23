i=input()
j=i.split()
for i in range(0,len(j)):
    j[i]=int(j[i])
j.sort()
print(max(j),min(j),end="")
'''
score1=70
score2=85
print ('Student details are:')
print ('-'*20)
print ('Registration Number:')
rer_no=input()
print("Enter name:")
name=input()
print ('Name:',name)
print("Enter DOB:")
dob=input()
print ('Date of Birth:', dob)
print("Enter Address:")
add=input()
print ('Address:',add)
print("Enter city:")
city=input()
print ('City:',city)
print("Enter Phone no:")
phno=input()
print ('Phone number:', phno)
avg_score=(score1+score2)/2
print ('Average Score:', avg_score)
print ('-'*20)
print ('Name:',name)
print ('Date of Birth:', dob)
print ('Address:',add)
print ('City:',city)
print ('Phone number:', phno)
avg_score=(score1+score2)/2
print ('Average Score:', avg_score)

from collections import Counter
mylist=[1,2,3,1,5,6,2,1,1]
listcount=Counter(mylist)
print(listcount)
for thisitem in listcount.items():
     print('item: ',thisitem[0],
           'appeares: ',thisitem[1])

print('The value 1 appeares {0} times.'.format(listcount.get(1)))


Colors = ["Red", "Orange", "Yellow", "Green", "Blue"]
for Item in Colors:
    print(Item,end=" ")
print()

Formatted = "{:d}"
print(Formatted.format(7000))
Formatted = "{:,d}"
print(Formatted.format(7000))
Formatted = "{:^15,d}"
print(Formatted.format(7000))
Formatted = "{:*^15,d}"
print(Formatted.format(7000))
Formatted = "{:*^15.2f}"
print(Formatted.format(7000))
Formatted = "{:*>15X}"
print(Formatted.format(7000))
Formatted = "{:*<#15x}"
print(Formatted.format(7000))
Formatted = "A {0} {1} and a {0} {2}."
print(Formatted.format("blue", "car", "truck"))



def picnic(itemdict,leftwidth,rightwidth):
    print('PICNIC ITEMS'.center(leftwidth+rightwidth,'*'))
    for k,v in itemdict.items():
        print(k.ljust(leftwidth,'.')+str(v).rjust(rightwidth))

picitems={'sandwiches':4,'donats':5,'apples':5,'cups':5}
picnic(picitems,12,6)

          
    
import re
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search('my phone is (444) 555-4564.')
#print(mo.group(1))
print(mo.group())


while True:
    print("How are you?")
    feeling=input()
    if feeling.lower()=='great':
       print("I am also feeling the same")
    elif feeling=='bad':
        print("Hope you will be fine")
    else:
        print("mmh thats your day")



name='purity'
for i in name:
    print('***'+i+'***')


supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

catNames = []
while True:
    print('Enter the name ' + str(len(catNames) + 1) +
    ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
catNames = catNames + [name] # list concatenation
print('The names are:')
for name in catNames:
    print(' ' + name)   

import random
def getAnswer(num):
    if num ==1:
        return 'it is certain 1'
    elif num ==2:
        return 'it is decidedely so 2'
    elif num==3:
        return 'yes it is three'
    elif num == 4:
        return 'it is four'
    elif num==5:
        return'it is five'

#r=random.randint(1,5)
#fortune=getAnswer(r)
print(getAnswer(random.randint(1,5)))
    

def hello(name):
    print("hello "+name)

hello("Dan")

from random import *
for i in range(10):
    print(randint(1,10))


total=0
for num in range(10):
    total=total+num
print(total)

print("my name is")
for i in range(5):
    print("jimmy five times("+str(i)+")

name=""
while name !='your':
    print("please enter your name:")
    name=input()
    print('thank you')

while True:
    print("please enter  name")
    name=input()
    if name=='yours':
        continue
    print("please enter  password")
    password=''
    password=input()
    if password=='dan':
        break
print('thank you')
'''
'''
DJANGO TUTORIAL
to check if django is installed =django-admin --version
to create project=django-admin startproject Website
to start the django server=python manage.py runserver
to start an app type=python manage.py startapp music
to ensure that the app is connected to database =python manage.py migrate
To create a user in admin type=python manage.py createsuperuser=(username=danny and password=daniel24)


'''
