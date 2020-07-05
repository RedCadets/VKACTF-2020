from hashlib import md5, sha1
from secret import d, n
import re
from Crypto.Util.number import long_to_bytes, inverse

def check(file_name, received_signature, encrypted_key):

    f = open(file_name, "rb")
    file_content = f.read()
    hash = bytes_to_long(md5(file_content).digest())

    key = long_to_bytes(pow(int(encrypted_key), d, n)).decode('utf-8')

    params = re.findall("(\d+)", key)

    p_user = int(params[0])
    q_user = int(params[1])
    e = 65537
    
    if hash == pow(received_signature, e, p_user*q_user):
        return True
    else:
        return False
