import sys;import time

def progress_bar(i, total, prefix, length=70, fill='=', print_end='\r'):
    percent = ("{0:.1f}").format(100 * (i / float(total)))
    filled_length = int(length * i // total)
    bar = fill * filled_length + ' ' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} [{bar}] {percent}% '),
    sys.stdout.flush()
    if i == total:
        sys.stdout.write(print_end)
        sys.stdout.flush()

def Authorized():
    print('Detecting Authorization...')
    for i in range(1,1001):
        time.sleep(0.001)
        progress_bar(i,1000,'Verification')
    print()
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
    print('Version: 1.0.1_test')
    time.sleep(2)

def t_s(i,sl):
    sl/=1000
    for k in range(1,1001):
        time.sleep(sl)
        progress_bar(k,1000,f'Module({i}/9):')
    print('\nDone---(%d/9)...\n'%i)

Version();Authorized()
print('Loading Module...')
time.sleep(0.5)

try:
    import json;t_s(1,0.5)
    import base64;t_s(2,0.8)
    import sqlite3;t_s(3,1)
    import pyshark;t_s(4,1.5)
    import pandas as pd;t_s(5,1.8)
    from avro.io import DatumReader;t_s(6,2)
    from pandas import json_normalize;t_s(7,2.4)
    from avro.datafile import DataFileReader;t_s(8,3)
    from scapy.all import PcapReader, PcapWriter;t_s(9,4)
    time.sleep(0.5);print('Done'+'-'*90);time.sleep(0.5)
    print('Module Loaded Successfully!')
    time.sleep(0.5)
except:
    print('Module Loading Failed...')
    print('The Program Will Automatically Terminate In 5 Seconds...')
    time.sleep(5)
    exit()

def json_to_xlsx_1(a,b):
    progress_bar(0, 3, 'Progress:')
    # 讀取 JSON 檔案
    with open(a + '.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    progress_bar(1, 3, 'Progress:')

    # 將 JSON 資料展開並連接到主 DataFrame
    main_df = pd.json_normalize(data, 'data', sep='_')
    progress_bar(2, 3, 'Progress:')

    # 將 DataFrame 寫入 Excel 檔案
    main_df.to_excel(b + '.xlsx', index=False)
    progress_bar(3, 3, 'Progress:')

def json_to_xlsx_2(a,b):
    progress_bar(0, 3, 'Progress:')
    # 从JSON文件中读取数据
    with open(a+'.json', "r", encoding="utf-8") as file:
        json_data = json.load(file)
    progress_bar(1, 3, 'Progress:')

    # 使用json_normalize将嵌套的JSON数据展平
    df = json_normalize(json_data)
    progress_bar(2, 3, 'Progress:')

    # 将数据写入Excel文件
    df.to_excel(b+'.xlsx', index=False)
    progress_bar(3, 3, 'Progress:')

def parquet_to_xlsx(a,b):
    progress_bar(0, 2, 'Progress:')
    # 輸入和輸出文件的路徑
    input_parquet_file = a+".parquet"
    output_xlsx_file = b+".xlsx"

    # 讀取 Parquet 檔案
    df_parquet = pd.read_parquet(input_parquet_file)
    progress_bar(1, 2, 'Progress:')

    # 將 DataFrame 保存為 Excel 檔案
    df_parquet.to_excel(output_xlsx_file, index=False, engine='openpyxl')
    progress_bar(2, 2, 'Progress:')

def pcapng_to_pcap(a,b):
    progress_bar(0, 4, 'Progress:')
    input_file = a+".pcapng"
    output_file = b+".pcap"
    # 開啟 PCAPNG 文件
    pcapng_reader = PcapReader(input_file)
    progress_bar(1, 4, 'Progress:')

    # 創建 PCAP 文件
    pcap_writer = PcapWriter(output_file)
    progress_bar(2, 4, 'Progress:')

    # 讀取 PCAPNG 文件的每個封包，然後寫入 PCAP 文件
    for packet in pcapng_reader:
        pcap_writer.write(packet)
    progress_bar(3, 4, 'Progress:')

    # 關閉文件
    pcap_writer.close()
    progress_bar(4, 4, 'Progress:')

def tsv_to_xlsx(a,b):
    progress_bar(0, 2, 'Progress:')
    tsv_file_path = a+'.tsv'
    xlsx_file_path = b+'.xlsx'
    # 讀取 TSV 檔案
    df = pd.read_csv(tsv_file_path, sep='\t')
    progress_bar(1, 2, 'Progress:')

    # 將 DataFrame 寫入 Excel 檔案
    df.to_excel(xlsx_file_path, index=False)
    progress_bar(2, 2, 'Progress:')

def csv_to_xlsx(a,b):
    progress_bar(0, 2, 'Progress:')
    csv_file = a+'.csv'
    excel_file = b+'.xlsx'

    # 讀取 CSV 檔案
    df = pd.read_csv(csv_file, encoding='latin1')
    progress_bar(1, 2, 'Progress:')

    # 寫入 Excel 檔案
    df.to_excel(excel_file, index=False)
    progress_bar(2, 2, 'Progress:')

def db_to_xlsx(a,b):
    progress_bar(0, 3, 'Progress:')
    # 連接到 SQLite 資料庫
    conn = sqlite3.connect(a+'.db')
    progress_bar(1, 3, 'Progress:')

    # 讀取資料到 DataFrame
    df = pd.read_sql('SELECT * FROM table_name', conn)
    progress_bar(2, 3, 'Progress:')

    # 寫入 Excel 檔案
    df.to_excel(b+'.xlsx', index=False)
    progress_bar(3, 3, 'Progress:')

def feather_to_xlsx(a,b):
    progress_bar(0, 2, 'Progress:')
    input_file = a+'.feather'
    output_file = b+'.xlsx'

    df = pd.read_feather(input_file)
    progress_bar(1, 2, 'Progress:')

    df.to_excel(output_file, index=False)
    progress_bar(2, 2, 'Progress:')

def avro_to_xlsx(a,b):
    progress_bar(0, 4, 'Progress:')
    input_file = a+'.avro'
    output_file = b+'.xlsx'

    reader = DataFileReader(open(input_file, 'rb'), DatumReader())
    progress_bar(1, 4, 'Progress:')
    records = [record for record in reader]
    progress_bar(2, 4, 'Progress:')
    df = pd.DataFrame(records)
    progress_bar(3, 4, 'Progress:')
    df.to_excel(output_file, index=False)
    progress_bar(4, 4, 'Progress:')

def jsonl_to_xlsx(a,b):
    progress_bar(0, 3, 'Progress:')
    input_file = a+'.jsonl'
    output_file = b+'.xlsx'

    # 讀取 JSON Lines 檔案
    with open(input_file, 'r') as file:
        data = [json.loads(line) for line in file]
    progress_bar(1, 3, 'Progress:')

    df = pd.DataFrame(data)
    progress_bar(2, 3, 'Progress:')

    df.to_excel(output_file, index=False)
    progress_bar(3, 3, 'Progress:')

def sqlite_to_xlsx(a,b):
    progress_bar(0, 4, 'Progress:')
    input_file = a+'.sqlite'
    output_file = b+'.xlsx'

    # 連接到 SQLite 數據庫
    conn = sqlite3.connect(input_file)
    progress_bar(1, 4, 'Progress:')

    # 使用 SQL 查詢獲取數據
    query = "SELECT * FROM your_table"
    df = pd.read_sql_query(query, conn)
    progress_bar(2, 4, 'Progress:')

    # 關閉數據庫連接
    conn.close()
    progress_bar(3, 4, 'Progress:')

    # 將數據保存為 xlsx
    df.to_excel(output_file, index=False)
    progress_bar(4, 4, 'Progress:')

def orc_to_xlsx(a,b):
    progress_bar(0, 2, 'Progress:')
    input_file = a+'.orc'
    output_file = b+'.xlsx'

    # 讀取 ORC 檔案
    df = pd.read_orc(input_file)
    progress_bar(1, 2, 'Progress:')

    # 將 DataFrame 保存為 xlsx 檔案
    df.to_excel(output_file, index=False, engine='openpyxl')
    progress_bar(2, 2, 'Progress:')

def msg_to_xlsx(a,b):
    progress_bar(0, 2, 'Progress:')
    input_file = a+'.msg'
    output_file = b+'.xlsx'

    # 使用 pd.read_msgpack() 從 Msgpack 檔案讀取數據
    df_msgpack = pd.read_msgpack(input_file)
    progress_bar(1, 2, 'Progress:')

    df_msgpack.to_excel(output_file, index=False, engine='openpyxl')
    progress_bar(2, 2, 'Progress:')

def dta_to_xlsx(a,b):
    progress_bar(0, 2, 'Progress:')
    input_file = a+'.dta'
    output_file = b+'.xlsx'

    # 使用 pd.read_stata() 從 Stata 檔案讀取數據
    df_stata = pd.read_stata(input_file)
    progress_bar(1, 2, 'Progress:')

    df_stata.to_excel(output_file, index=False, engine='openpyxl')
    progress_bar(2, 2, 'Progress:')

def sas7bdat_to_xlsx(a,b):
    progress_bar(0, 2, 'Progress:')
    input_file = a+'.sas7bdat'
    output_file = b+'.xlsx'

    # 使用 pd.read_sas() 從 SAS 檔案讀取數據
    df_sas = pd.read_sas(input_file)
    progress_bar(1, 2, 'Progress:')

    df_sas.to_excel(output_file, index=False, engine='openpyxl')
    progress_bar(2, 2, 'Progress:')

def pcap_to_txt(a,b):
    progress_bar(0, 2, 'Progress:')
    input_pcap = a+'.pacp'
    output_netflow = b+'.txt'

    # 使用 pyshark 將 pcap 轉換為 NetFlow
    cap = pyshark.FileCapture(input_pcap)
    progress_bar(1, 2, 'Progress:')
    with open(output_netflow, 'w') as output_file:
        for pkt in cap:
            output_file.write(pkt.flow)
    progress_bar(2, 2, 'Progress:')

def pcap_to_json(a,b):
    progress_bar(0, 2, 'Progress:')
    input_pcap = a+'.pacp'
    output_json = b+'.json'

    # 使用 pyshark 將 pcap 轉換為 JSON
    cap = pyshark.FileCapture(input_pcap, use_json=True)
    progress_bar(1, 2, 'Progress:')
    with open(output_json, 'w') as output_file:
        for pkt in cap:
            output_file.write(pkt.json.dumps())
    progress_bar(2, 2, 'Progress:')

def json_to_pcap(a,b):
    progress_bar(0, 5, 'Progress:')
    input_zeek = a+'.json'
    output_pcap = b+'.pcap'

    # 這裡假設 Zeek 格式是一個 JSON 文件，你可能需要根據實際情況進行修改
    # 假設 Zeek 格式的 JSON 文件包含 pcap 的 base64 編碼
    with open(input_zeek, 'r') as input_file:
        progress_bar(1, 5, 'Progress:')
        zeek_data = json.load(input_file)
        progress_bar(2, 5, 'Progress:')
        pcap_data = base64.b64decode(zeek_data['pcap_base64'])
    progress_bar(3, 5, 'Progress:')

    # 寫入 pcap 文件
    with open(output_pcap, 'wb') as output_file:
        progress_bar(4, 5, 'Progress:')
        output_file.write(pcap_data)
    progress_bar(5, 5, 'Progress:')

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
        time.sleep(1)
        print('Please Enter The Desired Number: ',end='')
        while 1:
            try:
                s=int(input())
                while s<0 or s>17:
                    print('Input Error!\nPlease Enter Again: ',end='')
                    s=int(input())
                break
            except:print('Input Error!\nPlease Enter Again: ',end='')
        if s==0:
            break
        print('Connecting To Related Modules...')

        for i in range(1,1001):
            time.sleep(0.0002)
            progress_bar(i,1000,'Connecting:')
        print('\nConnection Completed!\n')

        print('Please Enter The Filename To Convert: ',end='')
        x=input()
        print('Please Enter The Filename After Conversion: ',end='')
        y=input()
        print('Conversion In Progress(May Take Some Time)...')
        if s==1:
            try:json_to_xlsx_1(x,y)
            except:json_to_xlsx_2(x,y)
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
        print('\nConversion Completed!\n')
    except:
        print('\nConversion Failed...\n');pass