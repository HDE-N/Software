import hashlib

def sha_256(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    hashed_data = sha256_hash.hexdigest()
    return hashed_data