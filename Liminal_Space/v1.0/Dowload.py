import os
import color
import requests
from tqdm import tqdm
from Table import table

def download_file(s, local, v_local):
    while 1:
        if s:
            tt = []
            for i in s:tt.append(i[0])
            table(tt)
            num = input(color.blue('Please Enter The Download Number Or Type \'e\' To End The Download: '))
            if num == 'e':return s, local, v_local
            num=int(num)
            if 1<=num<=len(s):
                filename, url = s[num-1][0], s[num-1][2]
                folder = rf'models\{filename}'
                os.makedirs(folder, exist_ok=True, mode=0o755)
                response = requests.get(url, stream=True)
                total_size = int(response.headers['content-length'])
                downloaded_size = 0
                with open(folder+'\\'+filename+r'.exe', 'wb') as f:
                    with tqdm(total=total_size, unit='B', unit_scale=True, ncols=100) as pbar:
                        for chunk in response.iter_content(chunk_size=1024):
                            f.write(chunk)
                            downloaded_size += len(chunk)
                            pbar.update(len(chunk))
                local.append(s[num-1][0])
                v_local[s[num-1][0]] = s[num-1][1]
                with open(r'models\cfg\Map.txt', 'a', encoding='utf-8') as k:
                    k.write('\n'+s[num-1][0]+' '+s[num-1][1])
                s.remove(s[num-1])
                if input(color.blue('Continue With The Download?(Y/N) ')).lower()!='y':return s, local, v_local
        else:
            print(color.red('No Installable Modules Available.'))
            return s, local, v_local
