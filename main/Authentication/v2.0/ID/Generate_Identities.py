#生成身分檔案
#帳號密碼可更改成自己需要的
import bcrypt

def encrypt(value):
    salt = bcrypt.gensalt()
    hashed_value = bcrypt.hashpw(value.encode('utf-8'), salt)
    return hashed_value

#以下是帳號密碼
s = {
    'test-1'  :  '1-test',
    'test-2'  :  '2-test',
    'test-3'  :  '3-test'
}


with open('Account.txt', 'w', encoding='utf-8') as k:
    for i in s:
        k.write(encrypt(i).decode('utf-8')+' '+encrypt(s[i]).decode('utf-8')+'\n')

with open('id.txt', 'w', encoding='utf-8') as k:
    for i in s:
        k.write(i+' '+s[i]+'\n')