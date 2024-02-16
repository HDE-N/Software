from time import sleep
from Progress_Bar import progress_bar
from Identity import id
import color

identity=id()
ssleep=0.002 if identity=='guest' else 0

def pb_1(i,sl):
    sl/=1000
    if identity=='guest':
        for k in range(1,1001):
            sleep(sl)
            progress_bar(k,1000,f'Module({i}/9)')
        print()
    print(color.green('Done---(%d/9)...\n'%i))

def pb_2(i, total):
        tt=float('%.2f'%(1000/total))
        i2=1000 if i==total else i*tt
        i1=0 if i==0 else (i-1)*tt
        for k in range(int(i1), int(i2+1)):
            sleep(ssleep)
            progress_bar(k, 1000, 'Progress')

try:
    import json;pb_1(1,0.8)
    import base64;pb_1(2,1)
    import sqlite3;pb_1(3,1.2)
    import pyshark;pb_1(4,2)
    import pandas as pd;pb_1(5,1.2)
    from avro.io import DatumReader;pb_1(6,2.5)
    from pandas import json_normalize;pb_1(7,3)
    from avro.datafile import DataFileReader;pb_1(8,4)
    from scapy.all import PcapReader, PcapWriter, rdpcap;pb_1(9,5)
    if identity=='guest':sleep(1);print(color.green('Done'+'-'*90))
    if identity=='guest':sleep(1.5)
    print(color.green('Module Loaded Successfully!'))
    sleep(0.5)
except:
    print('Module Loading Failed...')
    print('The Program Will Automatically Terminate In 5 Seconds...')
    sleep(5)
    exit()

def json_to_xlsx_1(a,b):
    pb_2(0, 3)
    with open(a + '.json', 'r', encoding='utf-8') as json_file:data = json.load(json_file)
    pb_2(1, 3)
    main_df = pd.json_normalize(data, 'data', sep='_')
    pb_2(2, 3)
    main_df.to_excel(b + '.xlsx', index=False)
    pb_2(3, 3)

def json_to_xlsx_2(a,b):
    pb_2(0, 3)
    with open(a+'.json', "r", encoding="utf-8") as file:json_data = json.load(file)
    pb_2(1, 3)
    df = json_normalize(json_data)
    pb_2(2, 3)
    df.to_excel(b+'.xlsx', index=False)
    pb_2(3, 3)

def parquet_to_xlsx(a,b):
    pb_2(0, 2)
    input_parquet_file = a+".parquet"
    output_xlsx_file = b+".xlsx"
    df_parquet = pd.read_parquet(input_parquet_file)
    pb_2(1, 2)
    df_parquet.to_excel(output_xlsx_file, index=False, engine='openpyxl')
    pb_2(2, 2)

def pcapng_to_pcap(a,b):
    pb_2(0, 4)
    input_file = a+".pcapng"
    output_file = b+".pcap"
    pcapng_reader = PcapReader(input_file)
    pb_2(1, 4)
    pcap_writer = PcapWriter(output_file)
    pb_2(2, 4)
    for packet in pcapng_reader:pcap_writer.write(packet)
    pb_2(3, 4)
    pcap_writer.close()
    pb_2(4, 4)

def tsv_to_xlsx(a,b):
    pb_2(0, 2)
    tsv_file_path = a+'.tsv'
    xlsx_file_path = b+'.xlsx'
    df = pd.read_csv(tsv_file_path, sep='\t')
    pb_2(1, 2)
    df.to_excel(xlsx_file_path, index=False)
    pb_2(2, 2)

def csv_to_xlsx(a,b):
    pb_2(0, 2)
    csv_file = a+'.csv'
    excel_file = b+'.xlsx'
    df = pd.read_csv(csv_file, encoding='latin1')
    pb_2(1, 2)
    df.to_excel(excel_file, index=False)
    pb_2(2, 2)

def db_to_xlsx(a,b):
    pb_2(0, 3)
    conn = sqlite3.connect(a+'.db')
    pb_2(1, 3)
    df = pd.read_sql('SELECT * FROM table_name', conn)
    pb_2(2, 3)
    df.to_excel(b+'.xlsx', index=False)
    pb_2(3, 3)

def feather_to_xlsx(a,b):
    pb_2(0, 2)
    input_file = a+'.feather'
    output_file = b+'.xlsx'
    df = pd.read_feather(input_file)
    pb_2(1, 2)
    df.to_excel(output_file, index=False)
    pb_2(2, 2)

def avro_to_xlsx(a,b):
    pb_2(0, 4)
    input_file = a+'.avro'
    output_file = b+'.xlsx'
    reader = DataFileReader(open(input_file, 'rb'), DatumReader())
    pb_2(1, 4)
    records = [record for record in reader]
    pb_2(2, 4)
    df = pd.DataFrame(records)
    pb_2(3, 4)
    df.to_excel(output_file, index=False)
    pb_2(4, 4)

def jsonl_to_xlsx(a,b):
    pb_2(0, 3)
    input_file = a+'.jsonl'
    output_file = b+'.xlsx'
    with open(input_file, 'r') as file:data = [json.loads(line) for line in file]
    pb_2(1, 3)
    df = pd.DataFrame(data)
    pb_2(2, 3)
    df.to_excel(output_file, index=False)
    pb_2(3, 3)

def sqlite_to_xlsx(a,b):
    pb_2(0, 4)
    input_file = a+'.sqlite'
    output_file = b+'.xlsx'
    conn = sqlite3.connect(input_file)
    pb_2(1, 4)
    query = "SELECT * FROM your_table"
    df = pd.read_sql_query(query, conn)
    pb_2(2, 4)
    conn.close()
    pb_2(3, 4)
    df.to_excel(output_file, index=False)
    pb_2(4, 4)

def orc_to_xlsx(a,b):
    pb_2(0, 2)
    input_file = a+'.orc'
    output_file = b+'.xlsx'
    df = pd.read_orc(input_file)
    pb_2(1, 2)
    df.to_excel(output_file, index=False, engine='openpyxl')
    pb_2(2, 2)

def msg_to_xlsx(a,b):
    pb_2(0, 2)
    input_file = a+'.msg'
    output_file = b+'.xlsx'
    df_msgpack = pd.read_msgpack(input_file)
    pb_2(1, 2)
    df_msgpack.to_excel(output_file, index=False, engine='openpyxl')
    pb_2(2, 2)

def dta_to_xlsx(a,b):
    pb_2(0, 2)
    input_file = a+'.dta'
    output_file = b+'.xlsx'
    df_stata = pd.read_stata(input_file)
    pb_2(1, 2)
    df_stata.to_excel(output_file, index=False, engine='openpyxl')
    pb_2(2, 2)

def sas7bdat_to_xlsx(a,b):
    pb_2(0, 2)
    input_file = a+'.sas7bdat'
    output_file = b+'.xlsx'
    df_sas = pd.read_sas(input_file)
    pb_2(1, 2)
    df_sas.to_excel(output_file, index=False, engine='openpyxl')
    pb_2(2, 2)

def pcap_to_txt(a,b):
    pb_2(0, 2)
    input_pcap = a+'.pcap'
    output_netflow = b+'.txt'
    packets = rdpcap(input_pcap)
    pb_2(1, 2)
    with open(output_netflow, 'w') as txt_file:
        for packet in packets:txt_file.write(str(packet) + '\n')
    pb_2(2, 2)

def pcap_to_json(a,b):
    pb_2(0, 2)
    input_pcap = a+'.pcap'
    output_json = b+'.json'
    cap = pyshark.FileCapture(input_pcap, use_json=True)
    pb_2(1, 2)
    with open(output_json, 'w') as output_file:
        for pkt in cap:output_file.write(pkt.json.dumps())
    pb_2(2, 2)

def json_to_pcap(a,b):
    pb_2(0, 5)
    input_zeek = a+'.json'
    output_pcap = b+'.pcap'
    with open(input_zeek, 'r') as input_file:
        pb_2(1, 5)
        zeek_data = json.load(input_file)
        pb_2(2, 5)
        pcap_data = base64.b64decode(zeek_data['pcap_base64'])
    pb_2(3, 5)
    with open(output_pcap, 'wb') as output_file:
        pb_2(4, 5)
        output_file.write(pcap_data)
    pb_2(5, 5)