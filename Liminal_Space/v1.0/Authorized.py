import time
import getpass
import requests
import color as c
from Encrypt import verify
from Progress_Bar import progress_bar

account = {'$argon2id$v=19$m=65536,t=3,p=4$lSgCPppude43lBIXbK017A$Z9mX6Ai+8UicOStFrmTdfdJ+N/fuAuq4KzWCzHoAC/o':'$argon2id$v=19$m=65536,t=3,p=4$I/5K/DMs46A1r36JZdB7NA$9sBWxlLP5C0mwVNnzSp52vyrQxIHtMxqmP1xsRB849M'}

def url_download(original_link):
    return original_link.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")

def Internet():
    try:
        for i in range(1, 334):
            time.sleep(0.001)
            progress_bar(i, 1000, 'Verification')
        download_url = url_download('https://github.com/HDE-N/Software/blob/File_Conversion/File_Conversion/v1.1_Official/ID/Account.txt')
        response = requests.get(download_url, verify=True)
        for i in range(334, 667):
            time.sleep(0.001)
            progress_bar(i, 1000, 'Verification')
    except Exception as e:
        print(f'\nError: {e}\nNo Internet Access, Guest Account Only...')
        return None
    if response.status_code == 200:
        for i in range(667, 1001):
            time.sleep(0.001)
            progress_bar(i, 1000, 'Verification')
        time.sleep(1)
        return response.text
    else:
        print('\nNo Internet Access, Guest Account Only...')
        return None

def Authorized(my_account, my_password):
    global account
    if my_account != my_password != None:
        file_content = Internet()
        print()
        try:
            for i in file_content.split('\n'):
                if i.strip():
                    a,b=i.split()
                    account[a]=b
        except:pass
    elif input(c.cyan('Have You Applied For An Account(Y/N)? ')).lower()=='y':
        file_content = Internet()
        print()
        try:
            for i in file_content.split('\n'):
                if i.strip():
                    a,b=i.split()
                    account[a]=b
        except:pass
    error=0
    while error<3:
        if my_account == my_password == None:
            my_account=getpass.getpass(c.magenta('Enter Account: '))
            my_password=getpass.getpass(c.magenta('Enter Password: '))
        for i in account:
            if verify(my_account,i):
                if verify(my_password,account[i]):
                    print(c.green('Verification Successful!!'))
                    return my_account, my_password
                else:
                    print(c.red('Verification Failed...'))
                    error+=1
                    my_account = None
                    my_password = None
                    break
        else:
            print(c.red('Verification Failed...'))
            error+=1
            my_account = None
            my_password = None
    print(c.red("Exceeded Attempts...\nProgram Will Automatically Close In 3 Seconds..."))
    time.sleep(3);exit()