from hashlib import sha256

entry = ("file.txt")
sort = ("crypt.crypt")
key = ("test")

key = sha256(key.encode("utf-8")).digest()

#rb = read_binaire

with open(entry, "rb") as x:
	with open(sort, "wb") as y:
		cpt = 0
		while x.peek():
			c = ord(x.read(1))
			v = cpt % len(key)
			b = bytes([c^key[v]])
			y.write(b)
			cpt += 1