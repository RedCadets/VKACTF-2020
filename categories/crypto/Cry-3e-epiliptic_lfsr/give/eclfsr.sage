from secret import gx, gy, secret_number

class eclfsr:
	def __init__(self, num = 101):
		m = 65537
		b = 1337
		E = EllipticCurve(GF(m), [0, b])
		G = E.point((gx, gy))
		inf = E.point((0, 1, 0))
		bin_n = bin(num % m)[2:]
		size = len(bin_n)

		self.polly = [i for i, x in enumerate(bin_n) if x == '1']
		self.state = [inf] * (size - 1) + [G]
		self.inf = inf
		
	def get_next(self):
		new = sum([self.state[i] for i in self.polly])
		self.state = self.state[1:] + [new]
		return 2**17 - 1 if new == self.inf else new.xy()[1]


class encryptor:
	def __init__(self, num):
		self.lfsr = eclfsr(num) 

	def enc(self, file_name):
		with open(file_name, 'rb') as input_file:
			data = input_file.read()
			data += b'\x00' * (len(data) % 2)
			blocks = [bytearray(data[i*2:(i+1)*2]) for i in range(len(data)//2)]

			with open(file_name + '.enc', 'wb') as output_file: 				
				for block in blocks:
					tmp = int(self.lfsr.get_next())
					key = bytearray([(tmp//255) % 255, tmp % 255])
					out = bytearray([key[0] ^^ block[0], key[1] ^^ block[1]])
					output_file.write(out)

		print('File "{}" encrypted'.format(file_name))


if __name__ == '__main__':
	a = encryptor(secret_number)
	a.enc('Lorem ipsum.txt')
	a.enc('flag.txt')

