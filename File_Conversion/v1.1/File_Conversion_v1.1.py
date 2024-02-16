import time
from Progress_Bar import progress_bar
from subprocess import run
import argparse
import color
from datetime import datetime

def Version():
    print(color.cyan('Version: 1.1_Official'))
    time.sleep(1)

Version()
parser = argparse.ArgumentParser(description='ID Auth')
parser.add_argument('--id', type=str, help='ID', default=None)
parser.add_argument('--key', type=str, help='Key', default=None)
args = parser.parse_args()
import Identity
Identity.id_input(args.id)
if str(datetime.today().date())!=args.key:
    print(color.red('Key Error...'))
    exit()
identity=args.id
print('Loading Module...')
if identity=='guest':time.sleep(0.5)

import Convert_File as cf

mod={
    1   :   r'json      to    xlsx',
    2   :   r'parquet   to    xlsx',
    3   :   r'pcapng    to    pcap',
    4   :   r'tsv       to    xlsx',
    5   :   r'csv       to    xlsx',
    6   :   r'db        to    xlsx',
    7   :   r'feather   to    xlsx',
    8   :   r'avro      to    xlsx',
    9   :   r'jsonl     to    xlsx',
    10  :   r'sqlite    to    xlsx',
    11  :   r'orc       to    xlsx',
    12  :   r'msg       to    xlsx',
    13  :   r'dta       to    xlsx',
    14  :   r'sas7bdat  to    xlsx',
    15  :   r'pcap      to    txt',
    16  :   r'pcap      to    json',
    17  :   r'json      to    pcap'
}

List=(rf'''
{color.magenta('This Program Supports The Following File Conversions...')}
+--------+----------------------+
| {color.magenta('Number')} | {color.magenta('Function')}             |
+--------+----------------------+
|   {color.cyan('1')}    | json      to    xlsx |
+--------+----------------------+
|   {color.cyan('2')}    | parquet   to    xlsx |
+--------+----------------------+
|   {color.cyan('3')}    | pcapng    to    pcap |
+--------+----------------------+
|   {color.cyan('4')}    | tsv       to    xlsx |
+--------+----------------------+
|   {color.cyan('5')}    | csv       to    xlsx |
+--------+----------------------+
|   {color.cyan('6')}    | db        to    xlsx |
+--------+----------------------+
|   {color.cyan('7')}    | feather   to    xlsx |
+--------+----------------------+
|   {color.cyan('8')}    | avro      to    xlsx |
+--------+----------------------+
|   {color.cyan('9')}    | jsonl     to    xlsx |
+--------+----------------------+
|   {color.cyan('10')}   | sqlite    to    xlsx |
+--------+----------------------+
|   {color.cyan('11')}   | orc       to    xlsx |
+--------+----------------------+
|   {color.cyan('12')}   | msg       to    xlsx |
+--------+----------------------+
|   {color.cyan('13')}   | dta       to    xlsx |
+--------+----------------------+
|   {color.cyan('14')}   | sas7bdat  to    xlsx |
+--------+----------------------+
|   {color.cyan('15')}   | pcap      to    txt  |
+--------+----------------------+
|   {color.cyan('16')}   | pcap      to    json |
+--------+----------------------+
|   {color.cyan('17')}   | json      to    pcap |
+--------+----------------------+

{color.magenta('Other')}
+---------+-----------------------------------------------------+
| {color.magenta('Command')} | {color.magenta('Function')}                                            |
+---------+-----------------------------------------------------+
|    {color.cyan('s')}    | Search Format                                       |
+---------+-----------------------------------------------------+
|    {color.cyan('c')}    | Clear Screen                                        |
+---------+-----------------------------------------------------+
|    {color.cyan('l')}    | Re-list Supported Conversion Formats                |
+---------+-----------------------------------------------------+
|    {color.cyan('cl')}   | Clear Screen & Re-list Supported Conversion Formats |
+---------+-----------------------------------------------------+
|    {color.cyan('e')}    | Exit The Program                                    |
+---------+-----------------------------------------------------+
''')

def convert_file(s):
    if identity=='guest':
        print(color.yellow('Connecting To Related Modules...'))
        for i in range(1,1001):
            time.sleep(0.0006)
            progress_bar(i,1000,'Connecting:')
        print(color.green('\nConnection Completed!\n'))

    x=input(color.blue('Please Enter The Filename To Convert: '))
    y=input(color.blue('Please Enter The Filename After Conversion: '))
    print(color.yellow('Conversion In Progress(May Take Some Time)...'))
    if s==1:
        try:cf.json_to_xlsx_1(x,y)
        except:cf.json_to_xlsx_2(x,y)
    elif s==2:cf.parquet_to_xlsx(x,y)
    elif s==3:cf.pcapng_to_pcap(x,y)
    elif s==4:cf.tsv_to_xlsx(x,y)
    elif s==5:cf.csv_to_xlsx(x,y)
    elif s==6:cf.db_to_xlsx(x,y)
    elif s==7:cf.feather_to_xlsx(x,y)
    elif s==8:cf.avro_to_xlsx(x,y)
    elif s==9:cf.jsonl_to_xlsx(x,y)
    elif s==10:cf.sqlite_to_xlsx(x,y)
    elif s==11:cf.orc_to_xlsx(x,y)
    elif s==12:cf.msg_to_xlsx(x,y)
    elif s==13:cf.dta_to_xlsx(x,y)
    elif s==14:cf.sas7bdat_to_xlsx(x,y)
    elif s==15:cf.pcap_to_txt(x,y)
    elif s==16:cf.pcap_to_json(x,y)
    elif s==17:cf.json_to_pcap(x,y)
    print(color.green('\nConversion Completed!\n'))
    print(color.blue('Please Enter The Desired Number: '),end='')

print(List)
while 1:
    if identity=='guest':time.sleep(1.5)
    print(color.blue('Please Enter The Desired Number: '),end='')
    while 1:
        s=input()
        try:
            s=int(s)
            if 1<=s<=17:
                try:
                    convert_file(s)
                except:
                    print(color.red('\nConversion Failed...\n'))
                    break
            else:
                print(color.red('Input Error!'))
                print(color.blue('Please Enter Again: '), end='')
        except:
            if s=='c':run(r'cls', shell=True);break
            elif s=='l':print(List);break
            elif s=='cl':
                run(r'cls', shell=True)
                print(List+'\n')
                break
            elif s=='s':
                kw=input(color.blue('Please Enter Keywords: ')).split()
                kw_num=0
                for i in kw:
                    for j,k in mod.items():
                        if i in k:
                            kw_num+=1
                            print('%d.\t%s'%(j,k))
                if kw_num==0:
                    print(color.red('No Results Found For This Keyword...\n'))
                    break
                print(color.blue('Please Enter The Desired Number: '),end='')
            elif s=='e':exit()
            else:
                print(color.red('Input Error!'))
                print(color.blue('Please Enter Again: '), end='')