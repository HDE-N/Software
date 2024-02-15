import time
import color
import requests as r
from Progress_Bar import progress_bar

def github_url_to_raw(github_url):
    parts = github_url.split('/')
    raw_url = f'https://raw.githubusercontent.com/{parts[3]}/{parts[4]}/{"/".join(parts[6:])}'
    return raw_url

def main(id):
    print(color.yellow('Connect To The Database...'))
    if id == 'guest':
        for i in range(1, 501):
            time.sleep(0.002)
            progress_bar(i, 1000, 'Link')
        time.sleep(1)
        for i in range(501, 1001):
            time.sleep(0.003)
            progress_bar(i, 1000, 'Link')
        time.sleep(1)
        print(color.green('\nLink Established, Acquiring Data...'))
    
    if id == 'guest':
        for i in range(1, 334):
            time.sleep(0.003)
            progress_bar(i, 1000, 'Fetch Data')
    else:progress_bar(1, 3, 'Fetch Data')
    url = github_url_to_raw('https://github.com/HDE-N/Software/blob/main/General_Table.txt')
    response = r.get(url)
    if id == 'guest':
        for i in range(334, 667):
            time.sleep(0.004)
            progress_bar(i, 1000, 'Fetch Data')
    else:progress_bar(2, 3, 'Fetch Data')
    if response.status_code == 200:
        if id == 'guest':
            for i in range(667, 1001):
                time.sleep(0.005)
                progress_bar(i, 1000, 'Fetch Data')
        else:progress_bar(3, 3, 'Fetch Data')
        file_content = response.text.split('\n')
        s=[]
        for i in file_content:
            if i:s.append(i.split())
        print(color.green('\nFetch Data Successful!!'))
        return s
    else:
        print(f'{color.red("Unable To Retrieve The File, Status Code:")} {response.status_code}')

