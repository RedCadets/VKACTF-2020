from fastecdsa import keys, curve, ecdsa
from Crypto.Util.number import inverse, bytes_to_long
from hashlib import sha1
from base64 import b64encode
import json

r = 912719042079422742683986320822253038190261686077268486631582113900
m = 'eyJhbGciOiAiRUNEU0EiLCJ0eXAiOiAiUDIyNCIsICJtZXNzYWdlX2hhc2giOiAic2hhMSJ9.eyJ1c2VyIjogInp4YyIsICJhZG1pbiI6ICJ0cnVlIn0='  # Заголовок + требуемый пэйлоад (то есть "admin":"true") 

m1 = 'eyJhbGciOiAiRUNEU0EiLCJ0eXAiOiAiUDIyNCIsICJtZXNzYWdlX2hhc2giOiAic2hhMSJ9.eyJ1c2VyIjogImhqayIsICJhZG1pbiI6ICJmYWxzZSJ9' # Заголовок + пэйлоад первой куки
s1 = 18098997308518553606532432529702143474971296646413785094092523754893
m2 = 'eyJhbGciOiAiRUNEU0EiLCJ0eXAiOiAiUDIyNCIsICJtZXNzYWdlX2hhc2giOiAic2hhMSJ9.eyJ1c2VyIjogIm5ubiIsICJhZG1pbiI6ICJmYWxzZSJ9' # Заголовок + пэйлоад второй куки
s2 = 2727164974486634287660238409578870582182308301212888603566057662912



h = sha1(m.encode()).digest()
z = bytes_to_long(h)
h1 = sha1(m1.encode()).digest()
z1 = bytes_to_long(h1)
h2 = sha1(m2.encode()).digest()
z2 = bytes_to_long(h2)

n = curve.P224.q 

k = ((z1 - z2) * inverse(s1 - s2, n)) % n
print(k)

r_inv = inverse(r,n)
private_key = ((s1*k - z1) * r_inv) % n

s = (inverse(k,n) * (z + r*private_key)) % n
print("s: ", s)

#Формируем подпись
signature = {}
signature["r"] = r
signature["s"] = s

#Вывод требуемой куки
print(m+"."+b64encode(json.dumps(signature).encode()).decode("utf-8"))

#Используем эту куку для входа в личный кабинет:
#eyJhbGciOiAiRUNEU0EiLCJ0eXAiOiAiUDIyNCIsICJtZXNzYWdlX2hhc2giOiAic2hhMSJ9.eyJ1c2VyIjogInp4YyIsICJhZG1pbiI6ICJ0cnVlIn0=.eyJyIjogOTEyNzE5MDQyMDc5NDIyNzQyNjgzOTg2MzIwODIyMjUzMDM4MTkwMjYxNjg2MDc3MjY4NDg2NjMxNTgyMTEzOTAwLCAicyI6IDI2NjE3MjM4MzUwNTE2NDUwOTcyODg4OTM1MDE0MDgwMDg1MTgwODc2ODAwMTgzNTEzNDQxNTMyMjI0NDY3MDUwOTY5fQ==

