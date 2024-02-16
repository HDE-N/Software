import os
import time
import color
import shutil
import Inquire as iq
import Dowload  as dl
from Table import table
from subprocess import run
from datetime import datetime
from Authorized import Authorized
from Progress_Bar import progress_bar

def Version():
    version = 'v1.0'
    version = color.cyan(version)
    print(color.cyan('Version:'), version)
    time.sleep(1)

def auth():
    acc, pas = Authorized(None, None)
    if input(color.blue('Would You Like To Save The Username And Password?(Y/N) ')).lower()=='y':
        with open(r'models\cfg\Account.txt', "w", encoding="utf-8") as file:file.write(acc+' '+pas)
    return acc, pas

def init():
    if not os.path.isdir("models"):
        os.makedirs(r'models\cfg', exist_ok=True, mode=0o755)
        with open(r'models\cfg\Map.txt', 'w', encoding='utf-8') as k:k.write('')
    if os.path.exists(r'models\cfg\Account.txt'):
        if input(color.blue('Detected That You Have Saved An Account. Do You Want To Use This Account For Authentication?(Y/N) ')).lower()=='y':
            with open(r'models\cfg\Account.txt', 'r', encoding='utf-8') as k:
                acc, pas=k.read().split()
            acc, pas = Authorized(acc, pas)
        else:acc, pas = auth()
    else:acc, pas = auth()
    return acc, pas

def find_mod_local():
    if acc == 'guest':
        for i in range(1, 501):
            time.sleep(0.002)
            progress_bar(i, 1000, 'Verification')
        time.sleep(1)
        for i in range(501, 1001):
            time.sleep(0.003)
            progress_bar(i, 1000, 'Verification')
        time.sleep(1)
    Map, v = [], {}
    print(color.magenta('\nLocally Installed Modules.'))
    with open(r'models\cfg\Map.txt', 'r', encoding='utf-8') as k:
        for i in k.read().split('\n'):
            if i:
                a, b = i.split()
                Map.append(a)
                v[a] = b
    if Map:table(Map)
    else:print('None')
    return Map, v

def find_mod_internet(Map):
    s = iq.main(acc)
    if acc == 'guest':time.sleep(1.5)
    td, tt = [], []
    print(color.magenta('\nModules Available For Download'))
    for i in range(len(s)):
        if s[i][0] in Map:continue
        td.append(s[i])
        tt.append(s[i][0])
    if tt:table(tt)
    else:print('None')
    return td

def de(local, v):
    while 1:
        if local:
            table(local)
            num = input(color.blue('Please Enter The Module Number You Want To Delete, Or Type \'e\' To End The Deletion Process: '))
            if num == 'e':return local, v
            num = int(num)
            if 1<=num<=len(local):
                if input(color.blue('When Deleting The File, It Will Be Removed Along With The Files In Its Module Folder. Are You Sure You Want To Proceed?(Y/N) '))=='y':
                    shutil.rmtree(r'models'+'\\'+local[num-1])
                    del v[local[num-1]]
                    local.remove(local[num-1])
                    print(color.green('Deletion Successful.'))
                    if local:
                        with open(r'models\cfg\Map.txt', 'w', encoding='utf-8') as k:
                            for i in v:k.write(i+' '+v[i]+'\n')
                    else:
                        with open(r'models\cfg\Map.txt', 'w', encoding='utf-8') as k:k.write('')
                    if input(color.blue('Continue With The Deletion?(Y/N) ')).lower() != 'y':return local, v
                else:print(color.yellow('Deletion paused.'))
            else:print(color.red('Input Error!'))
        else:
            print(color.red('No Files To Delete.'))
            return local, v

code = f'''
{color.magenta('Supported Commands Are As Follows:')}
+---------+----------------------------------------------+
| {color.magenta('Command')} | {color.magenta('Function')}                                     |
+---------+----------------------------------------------+
| {color.cyan('use')}     | Invoke A Locally Installed Module.           |
+---------+----------------------------------------------+
| {color.cyan('f-l')}     | Find Modules - Local.                        |
+---------+----------------------------------------------+
| {color.cyan('f-i')}     | Find Modules - Online.                       |
+---------+----------------------------------------------+
| {color.cyan('dow')}     | Download And Install Modules.                |
+---------+----------------------------------------------+
| {color.cyan('del')}     | Delete Modul.                                |
+---------+----------------------------------------------+
| {color.cyan('c')}       | Clear The Screen.                            |
+---------+----------------------------------------------+
| {color.cyan('l')}       | List Available Commands.                     |
+---------+----------------------------------------------+
| {color.cyan('cl')}      | Clear The Screen. & List Available Commands. |
+---------+----------------------------------------------+
| {color.cyan('e')}       | End The Program.                             |
+---------+----------------------------------------------+
'''

Version()
acc, pas = init()
local, v_local = find_mod_local()
print()
s = find_mod_internet(local)
if acc == 'guest':time.sleep(1.5)
print(code)
while 1:
    if acc == 'guest':time.sleep(1.5)
    dire = input(color.blue('Please Enter A Command: '))
    if dire == 'f-l':local, v_local = find_mod_local()
    elif dire == 'f-i':s = find_mod_internet(local)
    elif dire == 'dow':
        s, local, v_local = dl.download_file(s, local, v_local)
    elif dire == 'del':local, v_local = de(local, v_local)
    elif dire == 'l':print(code)
    elif dire == 'c':run(r'cls', shell=True)
    elif dire == 'cl':
        run(r'cls', shell=True)
        print(code)
    elif dire == 'e':exit()
    elif dire == 'use':
        if local:
            table(local)
            num = input(color.blue('Please Enter The Module Number Or Type \'e\' To End Module Invocation: '))
            if num == 'e':pass
            else:
                num = int(num)
                if 1<=num<=len(local):
                    run(rf'.\models\{local[num-1]}\{local[num-1]}.exe --id {acc} --key {str(datetime.today().strftime("%Y-%m-%d"))}')
                    run(r'cls', shell=True)
                    print(color.green('The Module Has Been Successfully Closed...'))
                    print(code)
        else:print(color.red('No Available Modules!'))
    else:print(color.red('Input Error!'))