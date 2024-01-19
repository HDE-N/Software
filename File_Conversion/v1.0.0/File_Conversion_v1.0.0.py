import time

def Authorized():
    print('Detecting Authorization...')
    time.sleep(2)
    from datetime import datetime
    today_date = datetime.now()
    formatted_date = today_date.strftime("%Y-%m")

    year,month=map(int,formatted_date.split('-'))

    if year==2023 or (year==2024 and month==1):print('Software Is Authorized...\n')
    else:
        print('Software Has Expired...')
        print('The Program Will Automatically Terminate In 5 Seconds...')
        time.sleep(5)
        exit()

def Version():
    print('Version: 1.0.0_test\n')
    time.sleep(2)

def t_s(i):
    print('Done---(%d/8)...'%i)
    time.sleep(1.5)

Version()
Authorized()
print('Loading Module...')
time.sleep(0.5)

try:
    import json
    t_s(1)
    import base64
    t_s(2)
    import sqlite3
    t_s(3)
    import pyshark
    t_s(4)
    import pandas as pd
    t_s(5)
    from avro.io import DatumReader
    t_s(6)
    from avro.datafile import DataFileReader
    t_s(7)
    from scapy.all import PcapReader, PcapWriter
    t_s(8)
    print('Done--------------------------------------------------------')
    print('Module Loaded Successfully!')
except:
    print('Module Loading Failed...')
    print('The Program Will Automatically Terminate In 5 Seconds...')
    time.sleep(5)
    exit()

def json_to_xlsx(a,b):
    # 讀取 JSON 檔案
    with open(a+'.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # 將 JSON 資料轉換成 DataFrame
    df = pd.json_normalize(data)

    # 將 DataFrame 寫入 Excel 檔案
    df.to_excel(b+'.xlsx', index=False)

def parquet_to_xlsx(a,b):
    # 輸入和輸出文件的路徑
    input_parquet_file = a+".parquet"
    output_xlsx_file = b+".xlsx"

    # 讀取 Parquet 檔案
    df_parquet = pd.read_parquet(input_parquet_file)

    # 將 DataFrame 保存為 Excel 檔案
    df_parquet.to_excel(output_xlsx_file, index=False, engine='openpyxl')

def pcapng_to_pcap(a,b):
    input_file = a+".pcapng"
    output_file = b+".pcap"
    # 開啟 PCAPNG 文件
    pcapng_reader = PcapReader(input_file)

    # 創建 PCAP 文件
    pcap_writer = PcapWriter(output_file)

    # 讀取 PCAPNG 文件的每個封包，然後寫入 PCAP 文件
    for packet in pcapng_reader:
        pcap_writer.write(packet)

    # 關閉文件
    pcap_writer.close()

def tsv_to_xlsx(a,b):
    tsv_file_path = a+'.tsv'
    xlsx_file_path = b+'.xlsx'
    # 讀取 TSV 檔案
    df = pd.read_csv(tsv_file_path, sep='\t')

    # 將 DataFrame 寫入 Excel 檔案
    df.to_excel(xlsx_file_path, index=False)

def csv_to_xlsx(a,b):
    csv_file = a+'.csv'
    excel_file = b+'.xlsx'

    # 讀取 CSV 檔案
    df = pd.read_csv(csv_file)

    # 寫入 Excel 檔案
    df.to_excel(excel_file, index=False)

def db_to_xlsx(a,b):
    # 連接到 SQLite 資料庫
    conn = sqlite3.connect(a+'.db')

    # 讀取資料到 DataFrame
    df = pd.read_sql('SELECT * FROM table_name', conn)

    # 寫入 Excel 檔案
    df.to_excel(b+'.xlsx', index=False)

def feather_to_xlsx(a,b):
    input_file = a+'.feather'
    output_file = b+'.xlsx'

    df = pd.read_feather(input_file)
    df.to_excel(output_file, index=False)

def avro_to_xlsx(a,b):
    input_file = a+'.avro'
    output_file = b+'.xlsx'

    reader = DataFileReader(open(input_file, 'rb'), DatumReader())
    records = [record for record in reader]
    df = pd.DataFrame(records)
    df.to_excel(output_file, index=False)

def jsonl_to_xlsx(a,b):
    input_file = a+'.jsonl'
    output_file = b+'.xlsx'

    # 讀取 JSON Lines 檔案
    with open(input_file, 'r') as file:
        data = [json.loads(line) for line in file]

    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)

def sqlite_to_xlsx(a,b):
    input_file = a+'.sqlite'
    output_file = b+'.xlsx'

    # 連接到 SQLite 數據庫
    conn = sqlite3.connect(input_file)

    # 使用 SQL 查詢獲取數據
    query = "SELECT * FROM your_table"
    df = pd.read_sql_query(query, conn)

    # 關閉數據庫連接
    conn.close()

    # 將數據保存為 xlsx
    df.to_excel(output_file, index=False)

def orc_to_xlsx(a,b):
    input_file = a+'.orc'
    output_file = b+'.xlsx'

    # 讀取 ORC 檔案
    df = pd.read_orc(input_file)

    # 將 DataFrame 保存為 xlsx 檔案
    df.to_excel(output_file, index=False, engine='openpyxl')

def msg_to_xlsx(a,b):
    input_file = a+'.msg'
    output_file = b+'.xlsx'

    # 使用 pd.read_msgpack() 從 Msgpack 檔案讀取數據
    df_msgpack = pd.read_msgpack(input_file)
    df_msgpack.to_excel(output_file, index=False, engine='openpyxl')

def dta_to_xlsx(a,b):
    input_file = a+'.dta'
    output_file = b+'.xlsx'

    # 使用 pd.read_stata() 從 Stata 檔案讀取數據
    df_stata = pd.read_stata(input_file)
    df_stata.to_excel(output_file, index=False, engine='openpyxl')

def sas7bdat_to_xlsx(a,b):
    input_file = a+'.sas7bdat'
    output_file = b+'.xlsx'

    # 使用 pd.read_sas() 從 SAS 檔案讀取數據
    df_sas = pd.read_sas(input_file)
    df_sas.to_excel(output_file, index=False, engine='openpyxl')

def pcap_to_txt(a,b):
    input_pcap = a+'.pacp'
    output_netflow = b+'.txt'

    # 使用 pyshark 將 pcap 轉換為 NetFlow
    cap = pyshark.FileCapture(input_pcap)
    with open(output_netflow, 'w') as output_file:
        for pkt in cap:
            output_file.write(pkt.flow)

def pcap_to_json(a,b):
    input_pcap = a+'.pacp'
    output_json = b+'.json'

    # 使用 pyshark 將 pcap 轉換為 JSON
    cap = pyshark.FileCapture(input_pcap, use_json=True)
    with open(output_json, 'w') as output_file:
        for pkt in cap:
            output_file.write(pkt.json.dumps())

def json_to_pcap(a,b):
    input_zeek = a+'.json'
    output_pcap = b+'.pcap'

    # 這裡假設 Zeek 格式是一個 JSON 文件，你可能需要根據實際情況進行修改
    # 假設 Zeek 格式的 JSON 文件包含 pcap 的 base64 編碼
    with open(input_zeek, 'r') as input_file:
        zeek_data = json.load(input_file)
        pcap_data = base64.b64decode(zeek_data['pcap_base64'])

    # 寫入 pcap 文件
    with open(output_pcap, 'wb') as output_file:
        output_file.write(pcap_data)

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
        print('Please Enter The Desired Number: ',end='')
        s=int(input())
        while s<0 or s>17:
            print('Input Error!\nPlease Enter Again:',end='')
            s=int(input())
        if s==0:
            print('Thank You for Your Usage!')
            print('The Program Will Automatically Terminate In 3 Seconds...')
            time.sleep(3)
            break
        print('Please Enter The Filename To Convert: ',end='')
        x=input()
        print('Please Enter The Filename After Conversion: ',end='')
        y=input()
        print('Conversion In Progress...')
        if s==1:json_to_xlsx(x,y)
        elif s==2:parquet_to_xlsx(x,y)
        elif s==3:pcapng_to_pcap(x,y)
        elif s==4:tsv_to_xlsx(x,y)
        elif s==5:csv_to_xlsx(x,y)
        elif s==6:db_to_xlsx(x,y)
        elif s==7:feather_to_xlsx(x,y)
        elif s==8:avro_to_xlsx(x,y)
        elif s==9:jsonl_to_xlsx(x,y)
        elif s==10:sqlite_to_xlsx(x,y)
        elif s==11:orc_to_xlsx(x,y)
        elif s==12:msg_to_xlsx(x,y)
        elif s==13:dta_to_xlsx(x,y)
        elif s==14:sas7bdat_to_xlsx(x,y)
        elif s==15:pcap_to_txt(x,y)
        elif s==16:pcap_to_json(x,y)
        elif s==17:json_to_pcap(x,y)
        print('Conversion Completed!\n')
    except:
        print('Conversion Failed...')
        pass