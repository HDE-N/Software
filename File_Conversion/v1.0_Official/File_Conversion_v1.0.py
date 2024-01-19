from Progress_Bar import progress_bar
import time

def Version():
    print('Version: 1.0_Official')
    time.sleep(1)

Version()
from Identity import id
identity=id()
print('Loading Module...')
if identity=='guest':time.sleep(0.5)

import Convert_File as cf

print(r'''
This Program Supports The Following File Conversions...
1.   json      to    xlsx
2.   parquet   to    xlsx
3.   pcapng    to    pcap
4.   tsv       to    xlsx
5.   csv       to    xlsx
6.   db        to    xlsx
7.   feather   to    xlsx
8.   avro      to    xlsx
9.   jsonl     to    xlsx
10.  sqlite    to    xlsx
11.  orc       to    xlsx
12.  msg       to    xlsx
13.  dta       to    xlsx
14.  sas7bdat  to    xlsx
15.  pcap      to    txt
16.  pcap      to    json
17.  json      to    pcap

0.   Exit The Program
''')
while 1:
    try:
        if identity=='guest':time.sleep(1.5)
        print('Please Enter The Desired Number: ',end='')
        while 1:
            try:
                s=int(input())
                while s<0 or s>17:
                    s=int(input('Input Error!\nPlease Enter Again: '))
                break
            except:print('Input Error!\nPlease Enter Again: ',end='')
        if s==0:
            break
        print('Connecting To Related Modules...')

        if identity=='guest':
            for i in range(1,1001):
                time.sleep(0.0004)
                progress_bar(i,1000,'Connecting:')
        print('\nConnection Completed!\n')

        x=input('Please Enter The Filename To Convert: ')
        y=input('Please Enter The Filename After Conversion: ')
        print('Conversion In Progress(May Take Some Time)...')
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
        print('\nConversion Completed!\n')
    except:
        print('\nConversion Failed...\n');pass