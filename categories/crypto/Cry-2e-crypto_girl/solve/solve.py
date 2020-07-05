from Crypto.Util.number import *

def lcg(m, a, c, x):
	return (a*x + c) % m

def crack_unknown_increment(states, modulus, multiplier):
	increment = (states[1] - states[0]*multiplier) % modulus
	return modulus, multiplier, increment

def crack_unknown_multiplier(states, modulus):
	multiplier = (states[2] - states[1]) * inverse(states[1] - states[0], modulus) % modulus
	return crack_unknown_increment(states, modulus, multiplier)


if __name__ == '__main__':
	m = pow(2, 32)
	 
	enc = open('image.png.enc', 'rb').read()
	enc = [enc[i:i+4] for i in range(0, len(enc), 4)]
	 
	p = b''
	x0 = 0x89504e47 ^ bytes_to_long(enc[0])
	x1 = 0x0d0a1a0a ^ bytes_to_long(enc[1])
	x2 = 0x0000000d ^ bytes_to_long(enc[2])
	x3 = 0x49484452 ^ bytes_to_long(enc[3])
	states = [x0, x1, x2, x3]
	 
	x = x0
	res = crack_unknown_multiplier(states, m)
	a = res[1]
	c = res[2]

	image = b''
	for i in range(len(enc)):
		temp = long_to_bytes(x ^ bytes_to_long(enc[i]))
		temp = b'\x00' * (-len(temp) % 4) + temp
		image += temp
		x = lcg(m, a, c, x)
		
	with open('flag.png', 'wb') as f:
		f.write(image)