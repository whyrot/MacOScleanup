import os
import time

#function that deletes unneeded files.
def clearuseless():
    homepath = os.path.expanduser('~/Library/Caches')
    os.chdir(homepath)
    os.system('rm -rf *')
    print('cache files cleared!')
    homepath = os.path.expanduser('/var/log')
    os.chdir(homepath)
    os.system('rm -rf *')
    print('logs have been cleared')

#function that deletes downloads folders
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

#warns user
print('MacOS Cleanup Tool')
time.sleep(0.5)
warning = input('WARNING! this is a tool that clears up storage on your mac by DELETING FILES\n\nPlease backup any important files before proceeding\n\nI am not responsible for any loss of data\n\nContinue? y/n: ')
if warning == 'y':
    pass
if warning == 'n':
    exit()

print('\nrunning this with admin privliges may delete important files PLEASE do not run this with admin perms :D')
time.sleep(2)

#main menu
menu = input("""\n
1. clear arbitrary files (clears files not in use/not needed by system)                    
2. delete downloads folder (will delete EVERYTHING in downloads folder. BE CAREFUL!)
3. exit
: """)

if menu == "1":
    clearuseless()
if menu == "2":
    deletedownloads()
if menu == '3':
    exit()