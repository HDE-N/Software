#生成身分檔案
#帳號密碼可更改成自己需要的
import argon2

def encrypt(password):
    hasher = argon2.PasswordHasher()
    hashed_password = hasher.hash(password)
    return hashed_password

#以下是帳號密碼
s = {
    'test-1'  :  '1-test',
    'test-2'  :  '2-test',
    'test-3'  :  '3-test'
}


with open('Account.txt', 'w', encoding='utf-8') as k:
    for i in s:
        k.write(encrypt(i)+' '+encrypt(s[i])+'\n')

with open('id.txt', 'w', encoding='utf-8') as k:
    for i in s:
        k.write(i+' '+s[i]+'\n')