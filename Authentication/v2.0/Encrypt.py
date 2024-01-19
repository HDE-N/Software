#處理加密，不用動
import bcrypt

def Comparison(a,b):    #比對
    return bcrypt.checkpw(a.encode('utf-8'), b.encode('utf-8'))

def encrypt(value):     #加密
    salt = bcrypt.gensalt()
    hashed_value = bcrypt.hashpw(value.encode('utf-8'), salt)
    return hashed_value