#主要驗證程式
#需將Internet()內的連結，更改成自己的
import time;import requests
from Progress_Bar import progress_bar
from Encrypt import sha_256
import getpass

account = {'84983c60f7daadc1cb8698621f802c0d9f9a3c3c295c810748fb048115c186ec':'84983c60f7daadc1cb8698621f802c0d9f9a3c3c295c810748fb048115c186ec'}

def Internet():
    try:
        for i in range(1,334):
            time.sleep(0.001)
            progress_bar(i,1000,'Verification')

                        #這裡放上Google Drive「下載」連結
        download_url = 'https://drive.google.com/uc?id=1e_QnDAjkrXT99UM6HYvgPLTowgy8gUU_'
        time.sleep(1)
        response = requests.get(download_url)
        for i in range(334,667):
            time.sleep(0.001)
            progress_bar(i,1000,'Verification')
    except:
        print('\nNo Internet Access, Guest Account Only...')
        return None

    if response.status_code == 200:
        for i in range(667,1001):
            time.sleep(0.001)
            progress_bar(i,1000,'Verification')
        time.sleep(1)
        return response.text
    else:
        print('No Internet Access, Guest Account Only...')
        return None

def Authorized():
    global account
    if input('Have You Applied For An Account(Y/N)? ').lower()=='y':
        file_content = Internet()
        print()
        try:
            for i in file_content.split('\n'):
                if i.strip():
                    a,b=i.split()
                    account[a]=b
        except:
            pass
    
    error=0
    while error<3:
        acc=getpass.getpass('Enter Account: ')
        my_account = sha_256(acc)
        pas=getpass.getpass('Enter Password: ')
        my_password = sha_256(pas)
        if my_account in account:
            if my_password==account[my_account]:
                print('Verification Successful!!')
                return acc
            else:
                print('Verification Failed...')
                error+=1
        else:
            print('Verification Failed...')
            error+=1
    print("Exceeded Attempts...\nProgram Will Automatically Close In 3 Seconds...")
    time.sleep(3)
    exit()