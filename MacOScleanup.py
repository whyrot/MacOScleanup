import os
import time
import psutil



def show_cleared(bytes_cleared):
    if bytes_cleared < 1024**3:
        print(f'you have cleared {bytes_cleared / (1024**2):.2f} MB of files')
    else:
        print(f'you have cleared {bytes_cleared / (1024**3):.2f} GB of files')

#function that deletes unneeded files.
def clearuseless():
    free_before = psutil.disk_usage('/').free

    homepath = os.path.expanduser('~/Library/Caches')
    os.system(f'rm -rf "{homepath}"/*')
    print('cache files cleared!')

    homepath = os.path.expanduser('/var/log')
    os.system(f'rm -rf "{homepath}"/*')
    print('logs have been cleared')

    free_after = psutil.disk_usage('/').free
    cleared = free_after - free_before
    show_cleared(cleared)

#function that deletes downloads folders
def deletedownloads():
    warning2 = input('are you SURE you want to do this? your ENTIRE downloads folder will be deleted permanantly\nContinue? y/n: ')
    if warning2 == 'n':
        exit()

    free_before = psutil.disk_usage('/').free

    homepath = os.path.expanduser('~/Downloads')
    os.system(f'rm -rf "{homepath}"/*')
    print('downloads have been deleted!')

    free_after = psutil.disk_usage('/').free
    cleared = free_after - free_before
    show_cleared(cleared)

#resets the downloads, applications and the documents to maximize storage cleared
def fullreset():
    warning2 = input('are you SURE you want to do this? doing this will clear most files (inlcluding apps)\nhis is meant to be similar to a full reset without actually resetting your pc\nContinue? y/n: ')
    if warning2 == 'n':
        exit()

    free_before = psutil.disk_usage('/').free

    folders = ['~/Downloads', '~/Applications', '~/Documents']
    for folder in folders:
        homepath = os.path.expanduser(folder)
        os.system(f'rm -rf "{homepath}"/*')
        print(f'{folder} cleared!')

    free_after = psutil.disk_usage('/').free
    cleared = free_after - free_before
    show_cleared(cleared)

#warns user
print('MacOS Cleanup Tool')
time.sleep(0.5)
warning = input('WARNING! this is a tool that clears up storage on your mac by DELETING FILES\n\nPlease backup any important files before proceeding\n\nI am not responsible for any loss of data\n\nContinue? y/n: ')
if warning == 'n':
    exit()

print('\nrunning this with admin privliges may delete important files PLEASE do not run this with admin perms :D')
time.sleep(2)

#main menu
menu = input("""\n
1. clear arbitrary files (clears files not in use/not needed by system)                    
2. delete downloads folder (will delete EVERYTHING in downloads folder. BE CAREFUL!)
3. delete applications and other main folders (documents and downloads) (THIS IS PERMANENT!)
4. exit
: """)

if menu == "1":
    clearuseless()
if menu == "2":
    deletedownloads()
if menu == '3':
    fullreset()
if menu == '4':
    exit()
