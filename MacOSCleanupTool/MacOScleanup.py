import os
import time

print('MacOS Cleanup Tool')
time.sleep(0.5)
warning = input('WARNING! this is a tool that clears up storage on your mac by DELETING FILES\n\nPlease backup any important files before proceeding\n\nI am not responsible for any loss of data\n\nContinue? y/n: ')
if warning == 'y':
    pass
if warning == 'n':
    exit()

def clearcache():
    homepath = os.path.expanduser('~/Library/Caches')
    os.chdir(homepath)
    os.system('rm -rf *')
    print('cache files cleared!')

def deletedownloads():
    warning2 = input('are you SURE you want to do this? your ENTIRE downloads folder will be deleted permanantly\nContinue? y/n: ')
    if warning2 == 'y':
        pass
    if warning2 == 'n':
        exit()
    homepath = os.path.expanduser(f'~/Downloads')
    os.chdir(homepath)
    os.system('rm -rf *')
    print('downloads have been deleted!')

print('\nrunning this with admin privliges may delete important files PLEASE do not run this with admin perms :D')
time.sleep(2)

menu = input("""\n
1. clear cache (removes arbitrary files stores in /Library/Caches)                     
2. delete downloads folder (will delete EVERYTHING in downloads folder. BE CAREFUL!)
: """)

if menu == "1":
    clearcache()
if menu == "2":
    deletedownloads()
