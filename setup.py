import sys
from instagram import instaMenu
from youtube import youMenu

def init():
    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('  ONLINE Video/Audio DOWNLOADER  ')
    print()
    print('     Created By : Vinit Vijal    ')
    print('            @CodeVinu            ')
    print('              v0.1.0             ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\n\n')
    mainMenu()

def mainMenu():
    print('\n\n')
    print('1. YouTube')
    print('2. Instagram')
    print('3. Exit')
    choice =  int(input('Options : '))
    if choice == 1:
        youMenu()
    elif choice == 2:
        instaMenu()
    elif choice == 3:
        sys.exit()
    mainMenu
init()