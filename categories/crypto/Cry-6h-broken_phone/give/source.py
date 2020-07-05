#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, getPrime, isPrime
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import hashlib
import os

FLAG = open('flag.txt', 'rb').read()

def encrypt_flag(secret, text):
	KEY = hashlib.sha256(str(secret).encode('ascii')).digest()[:16]
	IV = os.urandom(16)
	cipher = AES.new(KEY, AES.MODE_CBC, IV)
	ciphertext = cipher.encrypt(pad(text, 16))
	data = {}
	data['iv'] = iv.hex()
	data['enc'] = ciphertext.hex()
	return data

def main():
	g = 2
	p = getPrime(1536)
	a = getPrime(1530)
	b = getPrime(1530)

	A = pow(g, a, p)
	B = pow(g, b, p)

	alice_send = {'p': hex(p), 'g': hex(g), 'A':hex(A)}
	print("[+] Alice send:", alice_send)

	bob_send = {'p': hex(p), 'g': hex(g), 'B':hex(B)}
	print("[+] Bob send:", bob_send)

	secret = pow(A, b, p)
	ciphertext = encrypt_flag(secret, FLAG)
	print("[+] Bob send:", ciphertext)

if __name__ == '__main__':
	main()