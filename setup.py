import sys
from instagram import instaMenu
from youtube import youMenu
import os 

os.chdir('Downloads')


def init():
    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('  ONLINE Video/Audio DOWNLOADER  ')
    print('~~~Instagram YouTube Supported~~~')
    print('     Created By : Vinit Vijal    ')
    print('            @CodeVinu            ')
    print('              v0.1.0             ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    mainMenu()

def mainMenu():
    print('\n\n')
    print('1. YouTube')
    print('2. Instagram')
    print('3. Exit')
    choice =  int(input('Choose Your Option : '))
    if choice == 1:
        youMenu()
    elif choice == 2:
        instaMenu()
    elif choice == 3:
        print('''\n\nThanks For Using AnyLoader v0.1.0 
        See You Soon, Byy''')
        sys.exit()
    mainMenu()
init()