#! Python37
#pw.py-an insecure password locker program.
password={'email':'qwertyuiop123',
          'blog':'asdfgh1234jkl',
          'luggage':'1234567'}

import sys,pyperclip
if len(sys.argv)<2:
    print('usage: python pw.py[account] - copy account password')
    sys.exit()
account= sys.argv[1] 

if account in password:
    pyperclip.copy(password[account])
    print('password for '+account+ 'copied to clipboard')
else:
    print('There is no account named' +account)
