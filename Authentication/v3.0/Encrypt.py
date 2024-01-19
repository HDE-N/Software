import argon2
from getpass import getpass

# 加密
def encrypt(password):
    hasher = argon2.PasswordHasher()
    hashed_password = hasher.hash(password)
    return hashed_password

# 驗證
def verify(input_password, hashed_password):
    hasher = argon2.PasswordHasher()
    try:
        hasher.verify(hashed_password, input_password)
        return True
    except argon2.exceptions.VerifyMismatchError:
        return False
