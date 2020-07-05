from Crypto.Util.number import *

pad = lambda s: s + b'\x00' * (4 - len(s) % 4)

def next_number(m, a, c, x):
	return (a*x + c) % m

m = pow(2, 32)

a = ?
c = ?
x = ?

if __name__ == '__main__':
	img = open('image.png', 'rb').read()
	img = pad(img)
	img = [img[i:i+4] for i in range(0, len(img), 4)]

	enc = b''
	for i in range(len(img)):
		temp = long_to_bytes(x ^ bytes_to_long(img[i]))
		temp = b'\x00' * (-len(temp) % 4) + temp
		enc += temp
		x = next_number(m, a, c, x)

	with open('image.png.enc', 'wb') as f:
		f.write(enc)