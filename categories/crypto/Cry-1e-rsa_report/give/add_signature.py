from secret import n
from Crypto.Util.number import bytes_to_long

def add(user_key):

    if bytes_to_long(user_key.encode()) > n:
        return "Слишком длинный ключ"

    e = 257
    enc_key = str(pow(bytes_to_long(user_key.encode()), e, n))
    return enc_key
