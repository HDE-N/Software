#主要驗證程式
#需要將Internet()內的連結，更換成自己的
import time;import requests
from Progress_Bar import progress_bar
from Encrypt import Comparison
import getpass

#初始訪客guest/guest
account = {'$2b$12$SytcVpW7MVZTkILTr3Hdcu.RNmi1hdHZ9szeXsN5eYxTCzkZ2.6fG':'$2b$12$WKFK8SPkRZIl9vU8Ro4.0OQuO22/rNTrt8dB.zcI/bHgeBIsCeCtO'}

def url_download(original_link):    #將分享連結轉成下載連結
    # 從原始連結中提取檔案ID
    file_id_start = original_link.find("/d/") + 3
    file_id_end = original_link.find("/view")
    file_id = original_link[file_id_start:file_id_end]

    # 生成直接下載連結
    direct_download_link = f"https://drive.google.com/uc?export=download&id={file_id}"
    return direct_download_link

def Internet():     #爬蟲
    try:
        for i in range(1, 334):
            time.sleep(0.001)
            progress_bar(i, 1000, 'Verification')

                                    #這裡輸入檔案連結
        download_url = url_download('https://drive.google.com/file/d/1EM1nPZcxCVbQSpRxpmXhnAl6u_0C8DSf/view?usp=sharing')
        
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
        print('No Internet Access, Guest Account Only...')
        return None

def Authorized():   #驗證
    global account
    if input('Have You Applied For An Account(Y/N)? ').lower()=='y':
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
        my_account=getpass.getpass('Enter Account: ')   #輸入時不會顯示
        my_password=getpass.getpass('Enter Password: ')
        for i in account:
            if Comparison(my_account,i):
                if Comparison(my_password,account[i]):
                    print('Verification Successful!!')
                    return my_account
                else:
                    print('Verification Failed...')
                    error+=1
                    break
        else:
            print('Verification Failed...')
            error+=1

            
    print("Exceeded Attempts...\nProgram Will Automatically Close In 3 Seconds...")
    time.sleep(3)
    exit()