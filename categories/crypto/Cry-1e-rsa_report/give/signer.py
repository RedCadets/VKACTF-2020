from hashlib import md5, sha1
from secret import d, n
import re
from Crypto.Util.number import long_to_bytes, inverse

def sign(sig, file_name):     # Зашифрованная подпись из бд и название полученного файла

    f = open(file_name, "rb") # Файл отправленный пользователем
    file_content = f.read()
    hash = bytes_to_long(md5(file_content).digest())
    user_key = long_to_bytes(pow(int(sig), d, n)).decode('utf-8')

    params = re.findall("(\d+)", user_key) #Берём p и q

    p_user = int(params[0])
    q_user = int(params[1])

    e_user = 65537 #Для всех одинаковая 
    d_user = inverse(e_user, (p_user-1)*(q_user-1))

    signature = str(pow(hash, d_user, p_user*q_user))

    return signature
