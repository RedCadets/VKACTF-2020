
alfa = b"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_{}"

with open('Lorem ipsum.txt', 'rb') as file:
	plain_text = file.read()

with open('Lorem ipsum.txt.enc', 'rb') as file:
	enc_text = file.read()

tmp = [a ^ b for a, b in zip(enc_text, plain_text)]
used_keys = [bytes(tmp[i*2:(i+1)*2]) for i in range(len(tmp)//2)]
unequal_keys = set(used_keys)

#print(used_keys[:10])
print(unequal_keys)

with open('flag.txt.enc', 'rb') as file:
	data = file.read()
	blocks = [data[i*2:(i+1)*2] for i in range(len(data)//2)]

flag = [[] for _ in blocks]
for i, block in enumerate(blocks):
	for key in unequal_keys:
		tmp = bytes([key[0] ^ block[0], key[1] ^ block[1]])
		if bytes([tmp[0]]) in alfa and bytes([tmp[1]]) in alfa: 
			flag[i].append(tmp.decode()) 

for pos in flag:
	print(pos)
